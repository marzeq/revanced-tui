#!/usr/bin/env python

import subprocess
import json

def list_patches() -> str:
    command = "java -jar artifacts/cli.jar list-patches -p artifacts/patches.jar".split(" ")
    output = subprocess.check_output(command, text=True)
    return output

def make_options_file():
    command = "java -jar artifacts/cli.jar options -o -p artifacts/options.json artifacts/patches.jar".split(" ")
    subprocess.run(command)

def sanitise_output(output: str):
    output = output.replace("INFO: ", "")
    return output.split("\n\n")

def parse_patch(patch: str):
    split = patch.split("\n")

    ret = {
        "name": "",
        "description": "",
        "package_names": [],
        "default_value": True
    }

    for line in split:
        if "Name: " in line:
            ret["name"] = line.replace("Name: ", "")
        elif "Description: " in line:
            replaced = line.replace("Description: ", "")
            ret["description"] = replaced if replaced != "null" else None
        elif "Package name: " in line:
            ret["package_names"].append(line.replace("Package name: ", "").strip())

    if len(ret["package_names"]) == 0:
        ret["default_value"] = False

    return ret

output = list_patches()
output = sanitise_output(output)
patches = [parse_patch(patch) for patch in output]

with open("artifacts/patches.json", "w") as f:
    json.dump(patches, f, indent=4)

