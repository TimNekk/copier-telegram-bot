from __future__ import annotations

import subprocess
import os

print("Creating virtual environment...")
subprocess.run(["uv", "venv"], check=True)
print("Created virtual environment!")

print("Installing dependencies...")
subprocess.run(["uv", "add", "-r", "requirements.txt"], check=True)
subprocess.run(["uv", "add", "-r", "dev-requirements.txt", "--dev"], check=True)
print("Installed dependencies!")

print("Removing requirements.txt...")
os.remove("./requirements.txt")
os.remove("./dev-requirements.txt")
print("Removed requirements.txt!")
