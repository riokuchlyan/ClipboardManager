# Clipboard Manager README

## Overview
Welcome to **Clipboard Manager** – a lightweight and efficient clipboard manager designed exclusively for macOS users who value local storage and privacy. Built using Python and Tkinter, this application continuously monitors and saves your clipboard history, allowing easy access to previously copied items without relying on third-party cloud storage.

Created as a local alternative to cloud-based clipboard managers, this application currently supports text-based clipboard items. Planned enhancements will include support for images and other formats, as well as an “always-on-top” window feature for enhanced accessibility.

---

## Features
- **Continuous Clipboard Monitoring**: Automatically reads and stores every new clipboard entry, ensuring you have a full history of your copied items.
- **Local Storage**: All data is stored locally on your Mac, maintaining your privacy without syncing to the cloud.
- **User-Friendly Interface**: The application offers a simple and intuitive interface built with Tkinter, allowing easy navigation and access to clipboard history.
- **History Management**: Quickly access, view, and copy any previous clipboard items with just a few clicks.
  
---

## Installation Instructions
### Prerequisites
**Clipboard Manager** is currently available only on **macOS**. Ensure that you have:
- macOS (tested on macOS 10.15 and above)
- Python 3.8 or later (if you want to run the source code)

### Installation Steps
1. **Download the .dmg file**:
   - Visit the [Clipboard Manager release page] and download the latest `.dmg` file.
2. **Install the Application**:
   - Open the downloaded `.dmg` file.
   - Drag the Clipboard Manager application icon to your Applications folder.
3. **Open the Application**:
   - Locate the Clipboard Manager in your Applications folder.
   - Double-click to open it. You may need to go to **System Preferences > Security & Privacy** to allow it to open if macOS displays a security prompt.

---

## Usage
### Initial Setup
1. **Open the Clipboard Manager** by double-clicking the application icon in your Applications folder.
2. The application will automatically start monitoring your clipboard and save any new entries.

### Managing Clipboard History
- **View History**: Open the app window to view your full clipboard history, listed chronologically.
- **Copying Entries**: Select any item from the list and click **Copy** to place it back into your clipboard for easy pasting.
- **Deleting Entries**: To delete an item, right-click on it and select **Delete** to remove it from the history.

---

## Planned Improvements
The current version supports text-based clipboard data. In future updates, expect additional features, including:
- **Image and Rich Media Support**: Support for images, formatted text, and other non-text clipboard data.
- **Always-On-Top Window**: An option to keep the Clipboard Manager window always on top, making it easier to access without switching between applications.
- **Enhanced History Management**: Options to filter or search through clipboard history for faster retrieval of specific items.

---

## Troubleshooting
### Cannot Open Application
If macOS blocks the app, go to **System Preferences > Security & Privacy** to allow the application to open.

### Clipboard Monitoring Not Working
Ensure that **Clipboard Manager** has the necessary permissions. Go to **System Preferences > Security & Privacy > Accessibility** and check that Clipboard Manager is listed and enabled.

---

## Contributing
Contributions are welcome! If you’d like to report an issue, submit a feature request, or contribute code, please feel free to reach out or make a pull request (source code available soon).

---

## License
This project is licensed under the GPL-3.0 License. Please refer to the [LICENSE](./LICENSE) file for more details.

---

Thank you for using **Clipboard Manager**! Your feedback and suggestions are invaluable, so please don't hesitate to share them.
