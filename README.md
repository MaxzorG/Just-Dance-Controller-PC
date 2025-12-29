# Just Dance Controller PC

A custom smartphone controller application for Just Dance 2017 on PC. This tool allows you to use your mobile device as a motion controller, replacing the discontinued official application.

It runs as a standalone server on your PC and provides a web interface on your phone to interact with the game in real-time.

## Features

- **Motion Tracking:** Uses the smartphone accelerometer to track dance moves and score points in the game.
- **Lobby Control:** Select your coach (dancer) directly from the phone screen before the song starts.
- **Visual Feedback:** Displays the active coach avatar on the phone while dancing.
- **Scoreboard:** Shows your current score, star rating immediately after the song ends.
- **Zero Installation:** Runs as a portable executable file.

## Requirements

- Just Dance 2017 installed on your PC.
- PC and Smartphone must be connected to the same Wi-Fi network.
- A modern web browser on your smartphone (Recommended: Firefox).

## How to Use

1. Download the latest release (`main.exe`).
2. Run the executable on your PC.
3. If Windows Firewall prompts for access, select "Allow" (Private and Public networks) to let the phone connect.
4. Open the Just Dance 2017 game on your PC.
5. On your smartphone, scan the QR code displayed in the application window or manually enter the IP address provided.
6. Select a song in the game and start dancing.

## Browser Compatibility Note

Due to security policies in modern browsers regarding local network sensor access:

- **Android:** It is highly recommended to use **Firefox**. If you use Chrome or Brave, you may need to enable specific flags for "insecure origins" to allow accelerometer access.
- **iOS:** Safari requires user interaction to grant sensor permissions (tap the "Connect" button).

## Build from Source

If you want to modify the code or compile the executable yourself, follow these steps:

1. Install **Python** (version 3.8 or higher is recommended).
2. Install the required dependencies using pip:
   ```bash
   pip install qrcode pillow pyinstaller
   ```
3. Run the PyInstaller command in the project directory to generate the executable:
   ```bash
   python -m PyInstaller --noconsole --onefile --add-data "index.html;." --add-data "favicon.ico;." --icon=favicon.ico main.py
   ```
   *(Note: If you do not have a favicon.ico file, you can remove the icon parameters).*

4. The compiled application will appear in the `dist` folder.

## Credits

- Developed by **MAXZØR**. If you use the code please credit me.
- Portions of the code and protocol logic were adapted from the [JDWebcam](https://github.com/comeraperuibe944/JDWebcam) repository by **comeraperuibe944**.
```
