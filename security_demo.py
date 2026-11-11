# VejoEnergija - Task 3 CI/CD security demonstration
# Corrected version: no shell=True, no arbitrary shell commands.

import subprocess


def run_diagnostic():
    """Run a fixed, predefined diagnostic without invoking a shell."""
    result = subprocess.run(
        ["python3", "--version"],
        shell=False,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout or result.stderr
