#!/usr/bin/env python

import sys
import subprocess
import os

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <filename>")
    sys.exit(1)

filename = sys.argv[1]

if not os.path.exists(filename):
    print(f"Error: file '{filename}' not found")
    sys.exit(1)

with open("artifacts/include.txt") as f:
    include = f.read().splitlines()

with open("artifacts/exclude.txt") as f:
    exclude = f.read().splitlines()

base_cmd = [
    "java", "-jar", "artifacts/cli.jar", "patch",
        "-b", "artifacts/patches.jar",
        "-m", "artifacts/integrations.apk",
        "--options=artifacts/options.json",
        "-o", f"build/patched_{filename}", filename
]

for i in include:
    base_cmd.append("-i")
    base_cmd.append(i)

for e in exclude:
    base_cmd.append("-e")
    base_cmd.append(e)

subprocess.run(base_cmd)
