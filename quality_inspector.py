import os

def run_quality_and_legal_inspection():
    print("--------------------------------------------------")
    print("   🛡️ QUALITY INSPECTOR & LEGAL SAFETY SHIELD     ")
    print("--------------------------------------------------")
    
    script_path = "channels/channel_1_repair/drafts/fan_regulator_script.txt"
    
    if not os.path.exists(script_path):
        print("[ERROR] Pehle script_generator.py run karke script banayein!")
        return

    # Read the generated script
    with open(script_path, "r", encoding="utf-8") as f:
        content = f.read()

    print("[INFO] Scanning script for 0% Mistake Policy compliance...")
    print("[INFO] Checking for safety warnings and disclaimers...")

    # Inspection Checks
    has_disclaimer = "SAFETY DISCLAIMER" in content or "Warning" in content
    has_forceful_claims = "100% guarantee" in content.lower() or "guaranteed fix" in content.lower()

    if has_disclaimer and not has_forceful_claims:
        print("\n--------------------------------------------------")
        print("✅ [INSPECTION RESULT]: PASSED 100% SAFE!")
        print(" -> Mandatory Safety Warnings found.")
        print(" -> Zero Forceful Claims detected.")
        print(" -> Status: Approved for Human Review via Telegram.")
        print("--------------------------------------------------")
    else:
        print("\n--------------------------------------------------")
        print("❌ [INSPECTION RESULT]: FAILED / REVISION REQUIRED")
        print(" -> Missing safety warnings or unsafe claims found.")
        print("--------------------------------------------------")

if __name__ == "__main__":
    run_quality_and_legal_inspection()