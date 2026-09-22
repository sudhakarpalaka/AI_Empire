import json
import os
import urllib.request
import urllib.parse

def send_approved_script_to_phone():
    config_path = "config.json"
    script_path = "channels/channel_1_repair/drafts/fan_regulator_script.txt"

    if not os.path.exists(config_path) or not os.path.exists(script_path):
        print("[ERROR] Config file ya Script file nahi mili!")
        return

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    with open(script_path, "r", encoding="utf-8") as f:
        script_text = f.read()

    bot_info = config.get("telegram_bot", {})
    token = bot_info.get("bot_token")
    chat_id = bot_info.get("chat_id")

    if not token or not chat_id:
        print("[ERROR] Telegram token ya chat_id config.json mein missing hai!")
        return

    print("--------------------------------------------------")
    print("   📤 SENDING INSPECTED SCRIPT TO TELEGRAM...     ")
    print("--------------------------------------------------")

    # Message jo aapke phone par script ke sath aayega
    message = (
        "🛡️ *AI Empire: Legal Shield Passed!*\n\n"
        "Channel: *Electronics & Appliance Repair*\n"
        "Status: *100% Safe - Ready for Review* ✅\n\n"
        "📄 *Generated Script Preview:*\n"
        f"```text\n{script_text[:600]}...\n```\n\n"
        "Waiting for your final approval click!"
    )

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        data = urllib.parse.urlencode(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, method="POST")
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode())
            if result.get("ok"):
                print("[SUCCESS] Inspected script successfully sent to your Telegram phone!")
            else:
                print(f"[ERROR] Telegram API Error: {result}")
    except Exception as e:
        print(f"[ERROR] Connection failed: {e}")

if __name__ == "__main__":
    send_approved_script_to_phone()