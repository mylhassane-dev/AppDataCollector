# App Data Collector

## Welkome

### Overview

This script collects information about installed apps on an Android device, including package name, installation time, app name, and category. It outputs a JSON file containing the collected data.

### **Prerequisites**

* **Android device** with USB debugging enabled.
* **ADB (Android Debug Bridge)** installed on your computer.
* **Python** environment with the following libraries:
  * `subprocess`
  * `json`
  * `datetime`
  * `logging` (optional for error handling)

### **Installation**

1. Clone this repository to your local machine.
2. Ensure you have Python and the required libraries installed.
3. Connect your Android device to your computer via USB.
4. Enable USB debugging on your device.

### **Usage**

1. Navigate to the project directory in your terminal.
2. Run the Python script: `python app_data_collector.py`
3. The script will generate a `app_install_data.json` file in the same directory.

### **Output**

The generated JSON file will contain a list of app objects, each with the following structure:

```json
{
  "package_name": "com.example.app",
  "install_time": "YYYY-MM-DD HH:MM:SS",
  "app_name": "Example App",
  "category": "Productivity"
}
