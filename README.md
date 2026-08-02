<p align="center">
  <a href="https://gamemaker.io/en/showcase/climb-a-mountain-in-your-pocket">
    <img src="https://assets.gamemaker.io/climb_a_mountain_in_your_pocket_vid_climb_fda2281d28.jpg" alt="Climb! A Mountain in Your Pocket" width="760">
  </a>
</p>

<h1 align="center">Climb! A Mountain in Your Pocket — PortMaster</h1>

<p align="center">
  <img alt="Platform" src="https://img.shields.io/badge/platform-PortMaster-2ea44f">
  <img alt="Architecture" src="https://img.shields.io/badge/architecture-ARM-blue">
  <img alt="Game engine" src="https://img.shields.io/badge/engine-GameMaker-orange">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-yellow">
</p>

An unofficial PortMaster port of the Android release of **Climb! A Mountain in Your Pocket**. The GameMaker runtime is launched on Linux through **GMLoader**, making the game playable on compatible ARM handhelds such as the **R36S**.

> **BYO-data:** This repository does not include the game, APK, XAPK, copyrighted assets, or any other proprietary game data. You must provide your own legally obtained copy.

## About the game

**Climb! A Mountain in Your Pocket** is a challenging climbing game with controls that are easy to learn and difficult to master. Control each hand independently, swing from the rocks, use your momentum to jump, manage your stamina, and find a safe route toward the summit.

The original game was created by **Ivan Alcaide Ferrer** using **GameMaker**.

- [Official Google Play page](https://play.google.com/store/apps/details?id=com.IvanAF.ClimbAMIYPfree)
- [Official GameMaker showcase](https://gamemaker.io/en/showcase/climb-a-mountain-in-your-pocket)

## Port details

- Android GameMaker release running on Linux through GMLoader
- Designed for PortMaster-compatible ARM handhelds
- Tested on R36S with ArkOS and Mali-450 graphics
- Handheld controls supported
- No proprietary game data included
- Save data is stored separately from the original game files

## Requirements

- A PortMaster-compatible handheld
- PortMaster installed and updated
- A legally obtained Android APK of **Climb! A Mountain in Your Pocket**, specifically version **6.0.7**
- Enough free storage for the port and the required game data

## Installation

### 1. Download the port

Download the latest port package from this repository's **Releases** page. Extract it and copy the included port files to the `ports` directory of the SD card used by your handheld.

> Downloading this repository does **not** provide the game itself. The port package contains only the files created or distributed for compatibility with PortMaster.

### 2. Provide your own game APK

Obtain your own legal copy of **Climb! A Mountain in Your Pocket for Android, version 6.0.7**. The required file must be a complete `.apk` file.

For legal and licensing reasons:

- the APK is **not included** in this repository or in the port package;
- this project does not provide unofficial download links for the APK;
- you must obtain the game from an official or otherwise lawful source;
- do not upload, redistribute, or attach the APK to GitHub issues or releases.

> **Required version:** `6.0.7`  
> Other releases may contain different GameMaker data or libraries and are not guaranteed to work with this port.

### 3. Rename the APK

Locate the legally obtained APK on your computer. Make sure file extensions are visible, then rename the complete file to exactly:

```text
climb64.apk
```

The filename must be lowercase. Be careful not to accidentally create a name such as `climb64.apk.apk`.

### 4. Copy the APK into `gamedata`

Open the installed port directory and enter:

```text
climb_amy/gamedata
```

Copy `climb64.apk` into that folder. Do not extract the APK and do not place it beside the launcher script—the port expects the original APK at this exact path:

```text
climb_amy/gamedata/climb64.apk
```

### 5. Check the final structure

Before starting the game, confirm that the SD card contains a structure similar to this:

```text
ports/
├── climb_amy/
│   ├── gamedata/
│   │   └── climb64.apk
│   ├── libs/
│   └── controls.gptk
└── Climb! AMiYP.sh
```

The essential file location is:

```text
ports/climb_amy/gamedata/climb64.apk
```

If `climb64.apk` is outside `gamedata`, has a different name, is still inside a ZIP/XAPK archive, or is not version 6.0.7, the port may return to the menu or fail to start.

### 6. Launch the game

Safely eject the SD card, insert it into the handheld, and start **Climb! A Mountain in Your Pocket** from the Ports section. On first launch, allow a little extra time while the port prepares the required files.

If the game returns immediately to the menu, check these items first:

- the folder is named exactly `climb_amy`;
- the subfolder is named exactly `gamedata`;
- the file is named exactly `climb64.apk`;
- the APK is version `6.0.7`;
- the APK was copied as a file and was not extracted;
- the port package was fully extracted into the `ports` directory.

## Controls

The game uses separate actions for the climber's left and right hands. Hold a hand button to grip a rock, release it to let go, and combine both hands with the character's momentum to swing and jump.

| Action | Control |
| --- | --- |
| Left hand / grip | Left-hand action button |
| Right hand / grip | Right-hand action button |
| Navigate menus | D-pad / Analog stick |
| Confirm | Confirm button |
| Back | Back button |
| Exit the port | PortMaster exit combination |

## Compatibility

| Device / system | Status |
| --- | --- |
| R36S + ArkOS | Tested |
| Mali-450 GPU | Tested |
| Other PortMaster ARM devices | May work; testing is welcome |

Compatibility with an unlisted device is not guaranteed. When reporting a problem, include the handheld model, operating system, PortMaster version, and the complete runtime log.

## Troubleshooting

### The game returns to the menu

- Confirm that the APK exists at `ports/climb_amy/gamedata/climb64.apk`.
- Confirm that it is Android version `6.0.7` and that it was not extracted.
- Check that the file was not accidentally named `climb64.apk.apk`.
- Update PortMaster and its runtimes.
- Check the log file generated after launching the port.

### Controls do not respond

- Confirm that `controls.gptk` exists inside the port folder.
- Restore the original control configuration from the release package.
- Disconnect unsupported USB controllers and test with the handheld controls.

### The image is distorted or the game performs poorly

- Use the recommended system image and graphics configuration for your handheld.
- Close background services before launching the game.
- Report the device model and log so compatibility can be investigated.

## Bug reports

Before opening an issue, please verify that:

- you are using the latest release of the port;
- PortMaster is updated;
- your game data was obtained legally and copied correctly;
- the problem can be reproduced.

Do **not** upload or attach APKs, XAPKs, extracted game assets, or other copyrighted files to an issue.

## Credits

- **Ivan Alcaide Ferrer** — original game and artwork
- **YoYo Games** — GameMaker
- **GMLoader contributors** — GameMaker Android compatibility layer
- **PortMaster community** — platform, tools, runtimes, and documentation
- **Lucas Soares** — PortMaster port and configuration

## License

The original scripts, configuration files, patches, and documentation created specifically for this port are licensed under the [MIT License](LICENSE), unless a file states otherwise.

The MIT License applies **only** to original porting work contained in this repository. It does not apply to the original game, GameMaker runtime, GMLoader, third-party libraries, artwork, audio, trademarks, or proprietary game data. Those components remain subject to their respective owners and licenses.

## Legal notice

This is an unofficial, fan-made compatibility project. It is not affiliated with, sponsored by, approved by, or endorsed by Ivan Alcaide Ferrer, YoYo Games, or the original publishers and distributors.

All game names, trademarks, artwork, audio, code, and assets belong to their respective owners. This repository is intended to provide only the original scripts and configuration necessary to run a legally obtained copy of the game on compatible hardware.

If you enjoy the game, please support its original developer by obtaining it through an official store.
