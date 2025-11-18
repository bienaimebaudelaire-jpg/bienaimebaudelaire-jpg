# fix_and_test_explicit.ps1
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

Write-Host "==> Running fix_and_test_explicit.ps1"

$proj = (Get-Location).Path
$venv_python = Join-Path $proj ".\.venv\Scripts\python.exe"

if (-Not (Test-Path $venv_python)) {
    Write-Error "Venv python not found. Run 1_setup.ps1 first."
    exit 1
}

Write-Host "Using venv python: $venv_python"
& $venv_python --version

Write-Host "Upgrading pip and tools..."
& $venv_python -m pip install --upgrade pip setuptools wheel

Write-Host "Installing requests..."
& $venv_python -m pip install requests

Write-Host "Checking requests installation..."
& $venv_python -m pip show requests

# Fix test file if exists
$target = Join-Path $proj "tests\test_auto_improvement.py"
if (Test-Path $target) {
    Write-Host "Patching $target"
    $text = Get-Content $target -Raw

    $bad = "from src.core.humean_auto_improvement import src.core.humean_auto_improver"
    $good = "from src.core.humean_auto_improvement import humean_auto_improver"

    if ($text.Contains($bad)) {
        Copy-Item $target "$target.bak" -Force
        $text.Replace($bad, $good) | Out-File -Encoding ASCII $target
        Write-Host "Patched. Backup created: $target.bak"
    } else {
        Write-Host "No broken import found in test_auto_improvement.py"
    }
} else {
    Write-Host "No test_auto_improvement.py found."
}

Write-Host "Running pytest..."
& $venv_python -m pytest -q

Write-Host "Done."
