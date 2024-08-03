# revanced-tui

A simple TUI alternative for [ReVanced](https://revanced.app/). Allows you to select each patch you want, configure their options and patch an app all in your terminal.

Note: This project is designed only with Linux in mind. Though, it may work in macOS. Usage on Windows is outlined in the [Usage on Windows](#usage-on-windows) section.

## Requirements

- `dialog` command (`cdialog` is the most common implementation)
- `curl`
- [`just`](https://github.com/casey/just)
- Latest python version
- pip
    * [pythondialog](https://pypi.org/project/pythondialog/)
    * [requests](https://pypi.org/project/requests/)
    * [tqdm](https://pypi.org/project/tqdm/)
- Java >= 17

## Usage

This is an example of how to use this script:

```bash
git clone https://github.com/marzeq/revanced-tui
cd revanced-tui

just select-and-patch FILE_PATH PACKAGE_NAME # for example: just select-and-patch youtube.apk com.google.android.youtube
```

If you want to only select the patches and not patch the app, you can use the `select-patches` command like this:

```bash
just select-patches PACKAGE_NAME
```

That will produce three files in the `artifacts` directory: `include.txt`, `exclude.txt` and `options.json`. You can back up these files somewhere else so they don't get overwritten when you patch another app.

Then, later down the line, you can put these files back in the `artifacts` directory and use the `patch` command to patch the app without having to select the patches again:

```bash
just patch FILE_PATH PACKAGE_NAME
```

Every time you run either of these commands, the script will check for updates for the CLI, integrations and patches and download new versions if necessary.

### Custom integrations, patches and CLI

You can download custom integrations and patches by using the `download-custom-integrations` and `download-custom-patches` commands:

```bash
just download-custom-integrations INTEGRATIONS_FILE_URL
just download-custom-patches PATCHES_FILE_URL
```

The upside of manually downloading the integrations and patches is that you can use your own custom versions, like [crimera/piko](https://github.com/crimera/piko).

If for some reason you want to install a custom version of the CLI, you can use the `download-custom-cli` command:

```bash
just download-custom-cli CLI_FILE_URL
```

NOTE: Installing custom versions of the CLI, integrations and patches will disable the automatic update checking. If you ever want to re-enable it, you need to delete the `artifacts/cli_version` and/or `artifacts/patches_integrations_version` files.

### Usage on Windows

I strongly recommend using WSL to run this just like you would on Linux.

Alternatively, you can run the Python scripts in the scripts folder directly. But you will somehow have to figure out how to install dialog on Windows (you're on your own with that).

## Missing/planned features

- [ ] Version protection (stopping you from patching an app with a patch for a different version of the app) \[unsure if I will ever implement this\]
- [x] Separate downloading custom integrations and patches from the official ones
- [x] Checking updates for official patches and integrations

Suggest more features in the issues tab (see [Issues & Contributing](#issues--contributing)).

## Issues & Contributing

I do not guarantee I will fix any issues you may encounter, you may need to troubleshoot on your own, but I will try to help you as much as I can.

Keep in mind I am not a godly being with infinite time and so will not implement every feature that you ask for. If you want to contribute, feel free to open a pull request, I'll look at it in my spare time.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. Credits greatly appreciated.

## Acknowledgments

- [The ReVanced contributors](https://revanced.app/contributors) for the awesome project
- [SodaWithoutSparkles](https://github.com/SodaWithoutSparkles) for the [ReVanced CLI guide](https://sodawithoutsparkles.github.io/revanced-troubleshooting-guide/06-revanced-cli/) because I couldn't figure out how to use it without it :')
