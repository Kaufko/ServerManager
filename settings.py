import json
import os

CONFIG_PATH = "/etc/servermanager/"

def write_config(form_dict):
    try:
        try:
            with open(CONFIG_PATH+"config.json", "r") as config:
                data = json.load(config)
        except PermissionError:
            raise Exception("Permission denied when writing to config file")
        except:
            data = {}
            print("file is empty")
        data.update(form_dict)
        with open(CONFIG_PATH+"config.json", "w") as config:
            json.dump(data, config, indent=4)

        return True

    except PermissionError:
        raise Exception("Permission denied when writing to config file")
    except Exception as e:
        raise Exception(f"Failed to save config: {str(e)}")

def get_config():
    try:
        with open(CONFIG_PATH+"config.json", 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}