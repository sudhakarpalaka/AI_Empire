import os
import json

def run_script_generator():
    print("--------------------------------------------------")
    print("   📝 TEACHER SCRIPT AGENT: ADVANCED & DETAILED   ")
    print("--------------------------------------------------")
    
    print("[SCRIPT] Generating an extended, comprehensive step-by-step script...")

    # Extended, detailed educational script with 0% Mistake Policy
    extended_script = (
        "=== AI EMPIRE MASTER EDUCATIONAL SCRIPT (EXTENDED EDITION) ===\n"
        "Channel: Electronics & Appliance Repair\n"
        "Topic: Complete Safe Ceiling Fan Regulator Repair Guide\n\n"
        
        "1. INTRODUCTION & SYMPTOM ANALYSIS:\n"
        "   - Welcome back students to the AI Empire Self-Repair Academy.\n"
        "   - Today we are diving deep into diagnosing why a ceiling fan regulator fails.\n"
        "   - Common symptoms: Humming noise, speed steps 1-4 not changing speeds properly, or total regulator burnout.\n\n"
        
        "2. MANDATORY SAFETY & PRECAUTIONS (0% MISTAKE POLICY):\n"
        "   - Rule Number 1: Always shut off the main distribution board circuit breaker.\n"
        "   - Use a digital voltage tester to double-check zero live current.\n"
        "   - Always wear insulated rubber gloves and use VDE-certified insulated screwdrivers.\n\n"
        
        "3. STEP-BY-STEP DISASSEMBLY & REPLACEMENT:\n"
        "   - Step A: Carefully remove the switchboard outer cover plate using a flathead screwdriver.\n"
        "   - Step B: Locate the faulty rotary or electronic regulator wiring terminals.\n"
        "   - Step C: Take a reference photo of the wire connections before loosening any screw.\n"
        "   - Step D: Detach the old regulator wires from the live line and switch bridge.\n"
        "   - Step E: Install the new high-grade capacitor/electronic regulator and secure terminal screws tightly to prevent sparking.\n\n"
        
        "4. TESTING & FINAL RE-ASSEMBLY:\n"
        "   - Reattach the switchboard cover securely.\n"
        "   - Turn the main power back ON.\n"
        "   - Test each speed level from 1 to 5 to ensure smooth, hum-free operation.\n\n"
        
        "5. OUTRO & COMPLIANCE:\n"
        "   - If you found this detailed guide helpful, check the description for legal safety notes.\n"
        "   - Like, subscribe, and stay tuned for the next automated repair tutorial!\n"
        "===============================================================\n"
    )

    # Save extended script inside the silo folder
    draft_dir = "channels/channel_1_repair/drafts"
    os.makedirs(draft_dir, exist_ok=True)
    script_path = os.path.join(draft_dir, "fan_regulator_script.txt")

    with open(script_path, "w", encoding="utf-8") as f:
        f.write(extended_script)

    print(f"[SUCCESS] Extended detailed script saved at: {script_path}")
    print("--------------------------------------------------")

if __name__ == "__main__":
    run_script_generator()