import json
import os
import urllib.request
import urllib.parse

def send_real_telegram_alert():
    config_path = "config.json"
    if not os.path.exists(config_path):
        print("[ERROR] config.json file nahi mili!")
        return

    with open(config_path, "r", encoding="utf-8") as file:
        config = json.load(file)

    bot_info = config.get("telegram_bot", {})
    token = bot_info.get("bot_token")
    chat_id = bot_info.get("chat_id")

    if not token or token == "YAHAN_APNA_BOT_TOKEN_DAALEIN":
        print("[ERROR] Pehle config.json mein apna asli bot_token dalein!")
        return

    # Message jo aapke phone par aayega
    message = (
        "🚨 *AI Empire Live Alert!*\n\n"
        "Channel: *Electronics & Appliance Repair*\n"
        "Topic: *Fan Regulator Repair Guide*\n"
        "Status: *Passed 0% Mistake & Quality Check* ✅\n\n"
        "System is waiting for Sudhakar's final approval click."
    )

    # Telegram API URL
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
                print("[SUCCESS] Asli live notification aapke Telegram phone par bhej diya gaya hai! Check your phone.")
            else:
                print(f"[ERROR] Telegram API Error: {result}")
    except Exception as e:
        print(f"[ERROR] Connection failed: {e}")

if __name__ == "__main__":
    send_real_telegram_alert()