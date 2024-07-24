#!/usr/bin/env python

import requests
import sys

from common import download

response = requests.get("https://api.github.com/repos/revanced/revanced-cli/tags")

if response.status_code != 200:
    print("Error: Failed to get the latest version")
    sys.exit(1)

try:
    json = response.json()
except ValueError:
    print("Error: Failed to parse the JSON response")
    sys.exit(1)

if not isinstance(json, list):
    print("Error: Malformed JSON response")
    sys.exit(1)

if len(json) == 0:
    print("Error: No tags found")
    sys.exit(1)

latest_tag = json[0]["name"].replace("v", "")

try:
    with open("artifacts/cli_version", "r") as file:
        cli_version = file.read().strip()
except FileNotFoundError:
    cli_version = ""

if cli_version == "custom":
    print("Custom version detected, skipping update check")
    sys.exit(0)

if cli_version == latest_tag:
    print("No new version available")
    sys.exit(0)


cli_url = f"https://github.com/ReVanced/revanced-cli/releases/download/v{latest_tag}/revanced-cli-{latest_tag}-all.jar"

download(cli_url, "artifacts/revanced-cli.jar")
