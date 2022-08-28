import subprocess
from pathlib import Path

target_files = [
    "lssr/__init__.py",
    "tests/test_lssr.py",
    "pyproject.toml",
]

current_version = subprocess.run(
    ["poetry", "version"], capture_output=True, check=True, text=True
).stdout.split()[1]

print("current_version:", current_version)

new_version = input("? new_version: ")

for file in target_files:
    p = Path(file)
    p.write_text(p.read_text().replace(current_version, new_version))
