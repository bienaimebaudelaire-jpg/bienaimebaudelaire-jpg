# # Salut, je suis 4UsByUs 👋

Je construis **HUMEAN** — une infrastructure d'orchestration IA, avec des applications spécialisées par-dessus (comparateur d'abonnements, assistant de temps libre).

➡️ Repo actif : [`humean-ecosystem`](https://github.com/bienaimebaudelaire-jpg/humean-ecosystem)

> ⚠️  Ce dépôt est le README de profil. Un ancien prototype exploratoire (serveur exposé, endpoints non authentifiés) a été retiré ; il reste dans l'historique git. Le développement actif est dans `humean-ecosystem`

## HUMEAN OpenShell integration

This repository includes optional Python utilities for running HUMEAN/P3 commands
inside an NVIDIA OpenShell sandbox. Python 3.11 or later is required. Install
the optional OpenShell SDK with:

```sh
python -m pip install '.[openshell]'
```

The SDK is optional; the `openshell` CLI and a configured OpenShell gateway must
also be installed separately. Follow the [official OpenShell installation
guide](https://docs.nvidia.com/openshell/latest/installation/).

```python
from humean_openshell import OpenShellClient, execute_workflow

client = OpenShellClient(timeout=120)
results = execute_workflow(
    client,
    "p3-modeling",
    [
        ["python", "-m", "model_tool", "validate", "model.json"],
        ["python", "-m", "model_tool", "simulate", "model.json"],
    ],
)
```

Workflow steps run sequentially in the named sandbox and stop on the first
non-zero exit status. For explicit, trusted host-side commands,
`run_command(["python", "--version"])` provides the same argv-only execution
and timeout handling without invoking a shell. Use `OpenShellClient` for
AI-generated or otherwise untrusted commands; the host-side helper is not a
sandbox.

Run the focused tests with `python -m unittest discover -s tests`.
