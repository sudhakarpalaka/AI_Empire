import json
import os

def send_telegram_simulation():
    config_path = "config.json"
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as file:
            config = json.load(file)
        
        bot_status = config["telegram_bot"]["status"]
        print("--------------------------------------------------")
        print("   🤖 TELEGRAM BOT NOTIFICATION BRIDGE (SIMULATOR) ")
        print("--------------------------------------------------")
        print(f"Bot Status : {bot_status}")
        print("[INFO] Connecting to Telegram Bot API...")
        print("[SUCCESS] Alert sent to Sudhakar's Phone!")
        print("\n[SAMPLE NOTIFICATION ON TELEGRAM]:")
        print("--------------------------------------------------")
        print("📢 New Draft Alert!")
        print("Channel: Electronics & Appliance Repair")
        print("Topic: Fan Regulator Repair Guide")
        print("Status: Passed 0% Mistake & Quality Check ✅")
        print("Action Required: Click below to Approve & Publish.")
        print("[ APPROVE & PUBLISH ] [ REJECT ]")
        print("--------------------------------------------------")
    else:
        print("[ERROR] Config file nahi mili!")

if __name__ == "__main__":
    send_telegram_simulation()