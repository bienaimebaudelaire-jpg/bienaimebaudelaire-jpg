import math
import subprocess
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from os import PathLike


@dataclass(frozen=True)
class CommandResult:
    command: tuple[str, ...]
    stdout: str
    stderr: str
    returncode: int


def run_command(
    command: Sequence[str],
    *,
    timeout: float = 60.0,
    cwd: str | PathLike[str] | None = None,
) -> CommandResult:
    if isinstance(command, (str, bytes)) or not command:
        raise ValueError("command must be a non-empty sequence of arguments")
    if any(not isinstance(argument, str) or "\0" in argument for argument in command):
        raise ValueError("command arguments must be strings without NUL characters")
    if not command[0]:
        raise ValueError("command executable cannot be empty")
    if not math.isfinite(timeout) or timeout <= 0:
        raise ValueError("timeout must be a positive finite number")

    args = tuple(command)
    result = subprocess.run(
        args,
        capture_output=True,
        check=False,
        cwd=cwd,
        shell=False,
        text=True,
        timeout=timeout,
    )
    return CommandResult(args, result.stdout, result.stderr, result.returncode)


class OpenShellClient:
    def __init__(self, executable: str = "openshell", timeout: float = 60.0):
        self.executable = executable
        self.timeout = timeout

    def exec(
        self,
        sandbox: str,
        command: Sequence[str],
        *,
        timeout: float | None = None,
    ) -> CommandResult:
        if (
            not sandbox
            or sandbox.startswith("-")
            or sandbox.strip() != sandbox
            or any(character.isspace() for character in sandbox)
            or "\0" in sandbox
        ):
            raise ValueError("sandbox must be a non-empty sandbox name")
        if isinstance(command, (str, bytes)) or not command:
            raise ValueError("command must be a non-empty sequence of arguments")
        return run_command(
            [self.executable, "sandbox", "exec", sandbox, "--", *command],
            timeout=self.timeout if timeout is None else timeout,
        )


class WorkflowExecutionError(RuntimeError):
    def __init__(self, step: int, result: CommandResult):
        super().__init__(f"OpenShell workflow step {step} exited with status {result.returncode}")
        self.step = step
        self.result = result


def execute_workflow(
    client: OpenShellClient,
    sandbox: str,
    commands: Iterable[Sequence[str]],
    *,
    timeout: float | None = None,
) -> tuple[CommandResult, ...]:
    results = []
    for step, command in enumerate(commands, start=1):
        result = client.exec(sandbox, command, timeout=timeout)
        results.append(result)
        if result.returncode != 0:
            raise WorkflowExecutionError(step, result)
    return tuple(results)
