# revanced-tui

A simple TUI alternative for [ReVanced](https://revanced.app/). Allows you to select each patch you want, configure their options and patch an app all in your terminal.

Note: This project is designed only with Linux in mind. It may work in macOS, and it definitely won't work in Windows.

## Requirements

- dialog
- curl
- [just](https://github.com/casey/just)
- Latest python version
- pip
    * [pythondialog](https://pypi.org/project/pythondialog/)
- Java >= 17

## Usage

This is an example of how to use this script:

```bash
git clone https://github.com/marzeq/revanced-tui
cd revanced-tui

# download revanced files

just download-cli CLI_URL # for example: just download-cli https://github.com/ReVanced/revanced-cli/releases/download/v4.6.0/revanced-cli-4.6.0-all.jar
just download-integrations INTEGRATIONS_URL # for example: just download-integrations https://github.com/ReVanced/revanced-integrations/releases/download/v1.11.1/revanced-integrations-1.11.1.apk
just download-patches PATCHES_URL # for example: just download-patches https://github.com/ReVanced/revanced-patches/releases/download/v4.11.0/revanced-patches-4.11.0.jar

# run the script

just select-and-patch FILE_PATH PACKAGE_NAME # for example: just select-and-patch youtube.apk com.google.android.youtube
```

You don't have to re-download the files every time you want to patch an app. But make sure you do so every once in a while.

If you want to only select the patches and not patch the app, you can use the `select-patches` command like this:

```bash
just select-patches PACKAGE_NAME
```

That will produce three files in the `artifacts` directory: `include.txt`, `exclude.txt` and `options.json`. You can back up these files somewhere else so they don't get overwritten when you patch another app.

Then, later down the line, you can put these files back in the `artifacts` directory and use the `patch` command to patch the app without having to select the patches again:

```bash
just patch FILE_PATH PACKAGE_NAME
```

### Custom integrations and patches

The upside of manually downloading the integrations and patches is that you can use your own custom versions, like [crimera/pico](https://github.com/crimera/pico).

## Missing/planned features

- [ ] Version protection (stopping you from patching an app with a patch for a different version of the app) \[unsure if I will ever implement this\]
- [ ] Separate downloading custom integrations and patches from the official ones
- [ ] Checking updates for official patches and integrations

Suggest more features in the issues tab (see [Issues & Contributing](#issues--contributing)).

## Issues & Contributing

I do not guarantee I will fix any issues you may encounter, you may need to troubleshoot on your own, but I will try to help you as much as I can.

Keep in mind I am not a godly being with infinite time and so will not implement every feature that you ask for. If you want to contribute, feel free to open a pull request, I'll look at it in my spare time.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. Credits greatly appreciated.

## Acknowledgments

- [The ReVanced contributors](https://revanced.app/contributors) for the awesome project
- [SodaWithoutSparkles](https://github.com/SodaWithoutSparkles) for the [ReVanced CLI guide](https://sodawithoutsparkles.github.io/revanced-troubleshooting-guide/06-revanced-cli/) because I couldn't figure out how to use it without it :')
