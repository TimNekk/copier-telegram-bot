from __future__ import annotations

import sys
from typing import List
from itertools import chain


BASE_REQUIREMENTS = [
    "aiogram",
    "loguru",
    "uvloop",
    "winloop",
]


def keep_requirements(requirements_to_keep: List[str], file_path: str) -> None:
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        updated_lines = [
            line
            for line in lines
            if any(
                req.strip().lower() == line.split("==")[0].strip().lower()
                for req in requirements_to_keep
            )
        ]
        with open(file_path, "w") as file:
            file.writelines(updated_lines)
    except Exception as e:
        sys.exit(f"Failed to keep only {requirements_to_keep} in {file_path}: {e}")


print("Removing unused requirements...")
requirements = list(chain(*[arg.split() for arg in sys.argv[1:]])) + BASE_REQUIREMENTS
keep_requirements(requirements, file_path="requirements.txt")
keep_requirements(requirements, file_path="dev-requirements.txt")
print("Removed unused requirements!")
