default: 
  just --list

[private]
setup-artifacts:
  mkdir -p artifacts/

download-cli CLI_URL: setup-artifacts
  curl -Lo artifacts/cli.jar {{CLI_URL}}

download-integrations INTEGRATIONS_URL: setup-artifacts
  curl -Lo artifacts/integrations.apk {{INTEGRATIONS_URL}}

download-patches PATCHES_URL: setup-artifacts
  curl -Lo artifacts/patches.jar {{PATCHES_URL}}

download CLI_URL INTEGRATIONS_URL PATCHES_URL: (download-cli CLI_URL) (download-integrations INTEGRATIONS_URL) (download-patches PATCHES_URL)

make-patches-file: setup-artifacts
  python scripts/make_patches_file.py

select-patches PACKAGE_NAME: make-patches-file
  python scripts/select_patches.py {{PACKAGE_NAME}}

patch FILENAME:
  mkdir -p build/
  python scripts/patch.py {{FILENAME}}

select-and-patch FILENAME PACKAGE_NAME: (select-patches PACKAGE_NAME) (patch FILENAME)

clean:
  rm -rf artifacts/ build/
