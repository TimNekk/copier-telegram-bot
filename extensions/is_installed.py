from jinja2.ext import Extension
import subprocess
import os
import sys
from typing import List


def command_exists(command: List[str]) -> bool:
    try:
        subprocess.run(command, capture_output=True, check=True)
        return True
    except Exception:
        return False


def get_python_versions() -> List[str]:
    versions = set()

    if sys.platform == "win32":
        try:
            output = subprocess.check_output(
                ["py", "-0"], stderr=subprocess.STDOUT, universal_newlines=True
            )
            for line in output.splitlines():
                if line.startswith(" -"):
                    version = line.split()[0][3:]
                    versions.add(version)
        except (subprocess.CalledProcessError, FileNotFoundError):
            pass

    if sys.platform in ("darwin", "linux"):
        common_dirs = ["/usr/bin", "/usr/local/bin", "/opt/homebrew/bin"]
        for directory in common_dirs:
            if os.path.exists(directory):
                for file in os.listdir(directory):
                    if file.startswith("python"):
                        try:
                            output = subprocess.check_output(
                                [os.path.join(directory, file), "--version"],
                                stderr=subprocess.STDOUT,
                                universal_newlines=True,
                            )
                            version = output.split()[1]
                            versions.add(version)
                        except (subprocess.CalledProcessError, FileNotFoundError):
                            pass

    return [".".join(version.split(".")[:2]) for version in versions]


def is_installed(value) -> bool:
    if value == "uv":
        return command_exists(["uv", "--version"])
    elif value == "poetry":
        return command_exists(["poetry", "--version"])
    elif value == "pip":
        return command_exists(["pip", "--version"]) or command_exists(["pip3", "--version"])
    elif value in ["3.8", "3.9", "3.10", "3.11", "3.12"]:
        return value in get_python_versions()
    else:
        print(f'ERROR: "{value}" installed check is not implemented')
    return False


class IsInstalledExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["is_installed"] = is_installed
