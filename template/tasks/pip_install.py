import os
import subprocess
import sys

python_version = sys.argv[1]

print("Creating virtual environment...")
subprocess.run(["py", "-" + python_version, "-m", "venv", ".venv"])
print("Created virtual environment!")

print("Installing dependencies...")
pip_path = (
    os.path.join(".venv", "bin", "pip")
    if os.name != "nt"
    else os.path.join(".venv", "Scripts", "pip")
)
subprocess.run([pip_path, "install", "-r", "requirements.txt"])
subprocess.run([pip_path, "install", "-r", "dev-requirements.txt"])
print("Installed dependencies!")
