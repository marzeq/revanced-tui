#!/usr/bin/env python

from dialog import Dialog
import json
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <package-name>")
    sys.exit(1)

package_name = sys.argv[1]

def get_patches():
    with open("artifacts/patches.json", "r") as f:
        patches = json.load(f)
    
    filtered = [patch for patch in patches if
        package_name in patch["package_names"] or len(patch["package_names"]) == 0
    ]

    return filtered

def run_dialog():
    # Create a Dialog object
    d = Dialog(dialog="dialog")

    # Define the choices with names and descriptions
    choices = [(patch["name"], patch["description"] if patch["description"] != None else "-", patch["default_value"]) for patch in get_patches()]

    maxsize_ret = d.maxsize()
    maxlines: int = 10
    maxcols: int = 50

    if maxsize_ret != None:
        maxlines, maxcols = maxsize_ret
    
    code, tags = d.checklist("Select Options", choices=choices, height=maxlines, width=maxcols, list_height=min(len(choices), maxlines))

    if code != d.OK or not tags:
        print("Dialog exited with status:", code)
        sys.exit(1)

    with open("artifacts/options.json", "r") as f:
        options = json.load(f)

    filtered_options = [patch for patch in options if
        patch["patchName"] in tags
    ]

    if len(filtered_options) > 0:
        for patch in filtered_options:
            max_key_len = max([len(option["key"]) for option in patch["options"]])
            remaining_width = maxcols - max_key_len - 2
            code, values = d.form(
                f"Options for {patch['patchName']}\n\nNOTE: <none> is a special value",
                height=maxlines,
                width=maxcols,
                elements=[
                    (option["key"], i+1, 1,
                     option["value"] if option["value"] != None else "<none>", i+1, max_key_len + 2,
                     remaining_width, 0)
                    for i, option in enumerate(patch["options"])
                ]
            )

            if code != d.OK or not values:
                print("Dialog exited with status:", code)
                sys.exit(1)

            for i, option in enumerate(patch["options"]):
                option["value"] = values[i] if values[i] != "<none>" else None

    with open("artifacts/options.json", "w") as f:
        json.dump(filtered_options, f, indent=2)

    
    with open("artifacts/include.txt", "w") as f:
        for tag in tags:
            f.write(str(tag) + "\n")

    with open("artifacts/exclude.txt", "w") as f:
        for patch in get_patches():
            if patch["name"] not in tags:
                f.write(patch["name"] + "\n")

if __name__ == "__main__":
    run_dialog()
