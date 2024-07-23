default: download
  just --list

[private]
setup-artifacts:
  mkdir -p artifacts/

# DOWNLOADS

[private]
custom-patches-integrations: setup-artifacts
  echo "custom" > artifacts/patches_integrations_version

[private]
custom-cli: setup-artifacts
  echo "custom" > artifacts/cli_version

download-custom-cli CLI_URL: custom-cli setup-artifacts
  curl -Lo artifacts/cli.jar {{CLI_URL}}

download-custom-integrations INTEGRATIONS_URL: custom-patches-integrations setup-artifacts
  curl -Lo artifacts/integrations.apk {{INTEGRATIONS_URL}}

download-custom-patches PATCHES_URL: custom-patches-integrations setup-artifacts
  curl -Lo artifacts/patches.jar {{PATCHES_URL}}


[private]
download-default-cli: setup-artifacts
  python scripts/get_default_cli.py

[private]
download-default-patches-integrations: setup-artifacts
  python scripts/get_default_patches_integrations.py

download: download-default-cli download-default-patches-integrations

# PATCHING AND SELECTING

make-patches-file: download setup-artifacts
  python scripts/make_patches_file.py

select-patches PACKAGE_NAME: download make-patches-file
  python scripts/select_patches.py {{PACKAGE_NAME}}

patch FILENAME: download
  mkdir -p build/
  python scripts/patch.py {{FILENAME}}

select-and-patch FILENAME PACKAGE_NAME: download (select-patches PACKAGE_NAME) (patch FILENAME)

clean:
  rm -rf artifacts/ build/
