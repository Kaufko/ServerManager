import json
import os
if os.access("config.json", os.W_OK):  # Check write permission
    print("Apache can write to this file")
else:
    print("Still no write access - check SELinux/AppArmor")

def handle_change(form_dict):
    try:
        with open("config.json", "w") as config:
            json.dump(form_dict, config, indent=4)

        return True

    except PermissionError:
        raise Exception("Permission denied when writing to config file")
    except Exception as e:
        raise Exception(f"Failed to save settings: {str(e)}")