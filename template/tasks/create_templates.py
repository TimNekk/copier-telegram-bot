from __future__ import annotations

import shutil

print("Creating .env template file...")
shutil.copyfile("./.env", "./.template.env")
print("Created .env template file!")
