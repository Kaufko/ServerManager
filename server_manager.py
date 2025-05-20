import os
import json
from settings import get_config, CONFIG_PATH, write_config

def load_servers():
    if not os.path.exists(CONFIG_PATH+"server_configs"):
        os.mkdir(CONFIG_PATH+"server_configs")
    config = get_config()
    servers = {"servers": set()} 
    if config.get('default_server_path') != None:
        for item in os.listdir(config.get('default_server_path')): #lists all item names in the default server path
            if os.path.isdir(os.path.join(config.get('default_server_path', item))): #passes only dirs
                if "servers" not in config or item not in config["servers"]: #checks if item is already in config (if yes skip)
                    #generate config and add to existing for each server
                    servers["servers"].add(os.path.basename(item))
                    server_config_path = CONFIG_PATH+f"server_configs/{item}.json"
                    try:
                        with open(server_config_path, 'r') as server_config:
                            current_server_config = json.load(server_config)
                        server_config.close()
                    except:
                        current_server_config = {}
                    current_server_config["name"] = item #server display name
                    current_server_config["type"] = "" #game name etc,
                    current_server_config["exec"] = "" #executable path
                    current_server_config["icon"] = "" #icon to display
                    with open(server_config_path, 'w') as server_config:
                        json.dump(current_server_config, server_config, indent=4)
                    server_config.close()

    write_config({"servers": list(servers["servers"])})  # ✅ Correct

load_servers()