# App Data Collector

## Overview

This script collects information about installed apps on an Android device, including package name, installation time, app name, and category. It outputs a JSON file containing the collected data.

## Prerequisites

* **Android device** with USB debugging enabled.
* **ADB (Android Debug Bridge)** installed on your computer.
* **Python** environment with the following libraries:
  * `subprocess`
  * `json`
  * `datetime`
  * `logging` (optional for error handling)

## Installation

1. Install ADB: [ADB](https://developer.android.com/studio/command-line/adb)

    * On Windows: [ADB](https://developer.android.com/studio/command-line/adb#windows)
      Or if you have installed android studio, you can add ADB to your PATH.

    ``` bash
    setx PATH "%PATH%;C:\Users\**YourUsername**\AppData\Local\Android\Sdk\platform-tools"

      ```

      * This will add `adb` to your PATH.
      * But you will need to restart your terminal.
      * Then you can run `adb` from any directory.

      ```bash

      adb devices

      ```

      * This will list all connected devices.
      * If you're incontring `unauthorized`
        In this case, the output shows that there is one device attached, but it is not authorized.

        To authorize the device, you need to allow the connection on the device itself. Here's how you can do it:

        Connect your Android device to your computer.
        On your Android device, you should see a notification asking for permission to allow USB debugging. Tap on the notification to start the authorization process.
        If you don't see the notification, go to your device's settings and look for the "Developer options" or "Developer settings" section.
        Enable the "USB debugging" option.
        Once USB debugging is enabled, you should see a prompt on your device asking for permission to allow the connection. Tap "OK" or "Allow" to authorize the connection.
        After authorizing the device, you can run the adb devices command again to verify that the device is now authorized.

        If you continue to experience issues with device authorization, please let me know and I'll be happy to help you further.

    * On macOS: [ADB](https://developer.android.com/studio/command-line/adb#macos)
    * On Linux: [ADB](https://developer.android.com/studio/command-line/adb#linux)

2. Ensure you have Git installed: [Git](https://git-scm.com/)
3. Clone this repository to your local machine:

    ```bash

    git clone https://github.com/mylhassane-dev/AppDataCollector.git

    ```

4. Navigate to the project directory:

    ```bash
    cd AppDataCollector
    ```

5. Ensure you have Python and the required libraries installed.

## Setting Up Python Environment

1. **Install Virtual Environment**:

    ```bash
    pip install virtualenv
    ```

2. **Create Python Environment**:

    ```bash
    virtualenv -p python3 venv
    ```

    * This command creates a Python environment in the `venv` directory that uses the `python3` interpreter.

3. **Activate Python Environment**:

    ```bash
    source venv/bin/activate
    ```

4. **Install Required Libraries**:

    * From `requirements.txt`:

      ```bash
      pip install -r requirements.txt
      ```

    * Or install directly:

      **Note**:
      We have to install the `datetime` and `logging` libraries manually.
      And the `subprocess` and `json` libraries are already installed.

      ```bash
      pip install datetime logging
      ```

## Usage

1. Connect your Android device to your computer via USB and enable USB debugging.
2. Navigate to the project directory in your terminal.
3. Run the Python script:

    ```bash
    python script.py
    ```

4. The script will generate a `app_install_data.json` file in the same directory.

## Output

The generated JSON file will contain a list of app objects, each with the following structure:

```json
{
  "package_name": "com.example.app",
  "install_time": "YYYY-MM-DD HH:MM:SS",
  "app_name": "Example App",
  "category": "Productivity"
}
```

## Full Script Code

```python
import subprocess
import json
import datetime
import logging

def get_installed_apps():
    """Gets a list of installed apps and their package names using ADB."""
    output = subprocess.check_output(["adb", "shell", "pm", "list", "packages", "-f"])
    apps = output.decode("utf-8").strip().split("\n")
    return apps

def get_app_install_time(package_name):
    """Gets the installation time of a specific app using ADB."""
    try:
        output = subprocess.check_output(["adb", "shell", "cmd", "package", "info", package_name])
        install_time_str = output.decode("utf-8").split("firstInstallTime=")[-1].split("\n")[0]
        install_time = datetime.datetime.fromtimestamp(int(install_time_str) / 1000)
        return install_time
    except subprocess.CalledProcessError as e:
        logging.error(f"Error getting install time for {package_name}: {e}")
        return None

def create_json_output(app_data):
    """Creates a JSON file containing app data."""
    with open("app_install_data.json", "w") as f:
        json.dump(app_data, f, indent=4)

def main():
    logging.basicConfig(filename='app_data_log.log', level=logging.INFO)
    apps = get_installed_apps()
    app_data = []
    for app in apps:
        try:
            package_name = app.split(":")[1]
            install_time = get_app_install_time(package_name)
            app_info = {
                "package_name": package_name,
                "install_time": install_time.strftime("%Y-%m-%d %H:%M:%S") if install_time else "Unknown"
            }
            # Add fields for app name, category, and other relevant data
            app_info["app_name"] = "Unknown"  # Placeholder for app name
            app_info["category"] = "Unknown"  # Placeholder for category
            app_data.append(app_info)
        except Exception as e:
            logging.error(f"Error processing app {package_name}: {str(e)}")

    create_json_output(app_data)

if __name__ == "__main__":
    main()
```
