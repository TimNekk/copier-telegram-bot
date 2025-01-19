import subprocess
import os
import re
import sys

python_version = sys.argv[1]

def get_python_path(version: str) -> str | None:
    if sys.version.startswith(version):
        return sys.executable

    if sys.platform == "win32":
        try:
            result = subprocess.run(
                ["py", f"-{version}", "-c", "import sys; print(sys.executable)"],
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError:
            pass

    version_parts = version.split(".")
    version_commands = [
        f"python{version}",
        f"python{version_parts[0]}.{version_parts[1]}",
        f"python{version_parts[0]}{version_parts[1]}",
    ]

    for cmd in version_commands:
        try:
            result = subprocess.run(
                [cmd, "-c", "import sys; print(sys.executable)"],
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout.strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass

    return None


print("Creating virtual environment...")
subprocess.run(["poetry", "env", "use", get_python_path(python_version)], check=True)
print("Created virtual environment!")

print("Installing dependencies...")
with open("requirements.txt", "r") as file:
    requirements = file.readlines()
cleaned_requirements = []
for req in requirements:
    req = req.strip()
    if req and not req.strip().startswith("#"):
        req = re.sub(r';sys_platform\s*==\s*"[^"]*"', "", req)
        req = re.sub(r';sys_platform\s*!=\s*"[^"]*"', "", req)
        cleaned_requirements.append(req.strip())

if cleaned_requirements:
    subprocess.run(["poetry", "add"] + cleaned_requirements, check=True)
print("Installed dependencies!")

print("Removing requirements.txt...")
os.remove("./requirements.txt")
print("Removed requirements.txt!")
