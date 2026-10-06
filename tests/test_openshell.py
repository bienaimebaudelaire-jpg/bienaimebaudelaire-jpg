import subprocess
import unittest
from unittest.mock import patch

from humean_openshell import (
    OpenShellClient,
    WorkflowExecutionError,
    execute_workflow,
    run_command,
)


class RunCommandTests(unittest.TestCase):
    @patch("humean_openshell.execution.subprocess.run")
    def test_runs_argv_without_a_shell(self, run):
        run.return_value = subprocess.CompletedProcess(
            ["python", "--version"], 0, "Python 3\n", ""
        )

        result = run_command(["python", "--version"])

        self.assertEqual(result.stdout, "Python 3\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(run.call_args.kwargs["shell"], False)

    def test_rejects_shell_strings_and_invalid_timeout(self):
        with self.assertRaises(ValueError):
            run_command("echo unsafe")
        with self.assertRaises(ValueError):
            run_command(["echo", "safe"], timeout=0)


class OpenShellClientTests(unittest.TestCase):
    @patch("humean_openshell.execution.subprocess.run")
    def test_exec_uses_open_shell_sandbox_command(self, run):
        run.return_value = subprocess.CompletedProcess([], 0, "ok", "")

        result = OpenShellClient().exec(
            "p3-modeling", ["python", "-m", "model_tool", "validate"]
        )

        self.assertEqual(result.returncode, 0)
        self.assertEqual(
            run.call_args.args[0],
            (
                "openshell",
                "sandbox",
                "exec",
                "p3-modeling",
                "--",
                "python",
                "-m",
                "model_tool",
                "validate",
            ),
        )

    def test_rejects_invalid_sandbox_names(self):
        with self.assertRaises(ValueError):
            OpenShellClient().exec("--help", ["echo", "unexpected"])

    def test_rejects_shell_string_commands(self):
        with self.assertRaises(ValueError):
            OpenShellClient().exec("p3-modeling", "echo unsafe")

    @patch("humean_openshell.execution.subprocess.run")
    def test_workflow_stops_at_first_failed_step(self, run):
        run.return_value = subprocess.CompletedProcess([], 1, "", "validation failed")
        client = OpenShellClient()

        with self.assertRaises(WorkflowExecutionError) as raised:
            execute_workflow(client, "p3-modeling", [["tool", "validate"], ["tool", "run"]])

        self.assertEqual(raised.exception.step, 1)
        run.assert_called_once()


if __name__ == "__main__":
    unittest.main()
