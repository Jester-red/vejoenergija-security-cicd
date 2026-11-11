
# VejoEnergija - Task 3 CI/CD security demonstration
# Intentionally insecure test code for Bandit.
# This file is not used by the Flask application.

import subprocess

def run_diagnostic(command):
    subprocess.run(command, shell=True, check=True)
