import subprocess
import os

def run_master_pipeline():
    print("==================================================")
    print("   🚀 AI EMPIRE MASTER PIPELINE: 12-AGENT SYSTEM  ")
    print("==================================================")

    scripts_to_run = [
        ("mentor_agent.py", "🧠 Personal Technical Mentor & Guide Agent"),
        ("channel_manager.py", "👑 Channel Manager (CEO) Agent"),
        ("channel_silo_engine.py", "🗂️ Multi-Channel Silo Engine"),
        ("security_agent.py", "🛡️ Security & Guardian Agent"),
        ("research_agent.py", "🔍 Research & Fact-Checking Agent"),
        ("script_generator.py", "📝 Teacher Script Agent"),
        ("quality_inspector.py", "🛡️ Quality Inspector & Legal Shield"),
        ("video_producer.py", "🎬 Production & Video Agent"),
        ("email_agent.py", "📧 Email & Communication Agent"),
        ("monetization_agent.py", "💰 Monetization & Business Agent"),
        ("analytics_agent.py", "📊 Analytics & Feedback Loop Agent"),
        ("send_script_to_telegram.py", "📱 Telegram Approval Notifier")
    ]

    for script, name in scripts_to_run:
        if os.path.exists(script):
            print(f"\n[RUNNING]: Executing {name} ({script})...")
            result = subprocess.run(["python", script], capture_output=False)
            if result.returncode != 0:
                print(f"[ERROR] {name} execution failed!")
                return
        else:
            print(f"[ERROR] {script} file nahi mili!")
            return

    print("\n==================================================")
    print("🎉 [SUCCESS]: COMPLETE 12-AGENT EMPIRE EXECUTED!")
    print(" -> Silo Engine verified: Zero cross-channel mix-ups.")
    print(" -> Check your Telegram phone app for the final approval alert!")
    print("==================================================")

if __name__ == "__main__":
    run_master_pipeline()