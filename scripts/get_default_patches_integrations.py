#!/usr/bin/env python

import requests
import sys

from common import download

response = requests.get("https://api.revanced.app/v3/patches/latest")

if response.status_code != 200:
    print("Error: Failed to get the latest patches")
    sys.exit(1)

try:
    json = response.json()
except ValueError:
    print("Error: Failed to parse the JSON response")
    sys.exit(1)

if "assets" not in json:
    print("Error: Malformed JSON response")
    sys.exit(1)

if not isinstance(json["assets"], list):
    print("Error: Malformed JSON response")
    sys.exit(1)

if "version" not in json or not isinstance(json["version"], str):
    print("Error: Malformed JSON response")
    sys.exit(1)

try:
    with open("artifacts/patches_integrations_version", "r") as file:
        patches_integrations_version = file.read().strip()
except FileNotFoundError:
    patches_integrations_version = ""

if patches_integrations_version == "custom":
    print("Custom version detected, skipping update check")
    sys.exit(0)

if patches_integrations_version == json["version"]:
    print("No new version available")
    sys.exit(0)


patches_url = None
integrations_url = None

for asset in json["assets"]:
    if "download_url" not in asset and "name" not in asset:
        print("Error: Malformed JSON response")
        sys.exit(1)
    if not isinstance(asset["download_url"], str) or not isinstance(asset["name"], str):
        print("Error: Malformed JSON response")
        sys.exit(1)

    if asset["name"] == "PATCHES":
        patches_url = asset["download_url"]
    elif asset["name"] == "INTEGRATION":
        integrations_url = asset["download_url"]
    else:
        print("Error: Malformed JSON response")
        sys.exit(1)

if patches_url is None or integrations_url is None:
    print("Error: Malformed JSON response")
    sys.exit(1)

download(patches_url, "artifacts/patches.jar")
download(integrations_url, "artifacts/integrations.apk")
