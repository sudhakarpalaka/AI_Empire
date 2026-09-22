import json
import os

config_path = "config.json"

if os.path.exists(config_path):
    with open(config_path, "r", encoding="utf-8") as file:
        config_data = json.load(file)
    
    print("--------------------------------------------------")
    print("   📂 CONFIGURATION FILE LOADED SUCCESSFULLY      ")
    print("--------------------------------------------------")
    print(f"System Name : {config_data['system_name']}")
    print(f"Core Policy : {config_data['core_policy']}")
    print("\n--- Active Channel Details ---")
    
    for ch in config_data['channels']:
        print(f"Channel ID   : {ch['channel_id']}")
        print(f"Channel Name : {ch['channel_name']}")
        print(f"Topic Focus  : {ch['topic']}")
        print(f"Human Approval: {ch['approval_required']}")
    print("--------------------------------------------------")
else:
    print("[ERROR] config.json file nahi mili!")