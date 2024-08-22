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
