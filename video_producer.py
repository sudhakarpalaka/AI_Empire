import os
import cv2
import numpy as np
from gtts import gTTS
from moviepy import AudioFileClip, VideoFileClip

def draw_cinematic_studio_frame(frame, part_name, description, scene_num, frame_idx):
    """Renders Hollywood-grade dark studio cinematic frames with glowing tech schematics"""
    # 1. High-End Dark Studio Gradient Background
    cv2.rectangle(frame, (0, 0), (1280, 720), (12, 18, 32), -1)
    
    # 2. Sleek Professional Header Bar
    cv2.rectangle(frame, (0, 0), (1280, 85), (24, 32, 54), -1)
    cv2.line(frame, (0, 85), (1280, 85), (56, 189, 248), 2)
    cv2.putText(frame, "⚡ AI EMPIRE | PROFESSIONAL HARDWARE REPAIR STUDIO", (40, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (56, 189, 248), 2)
    cv2.putText(frame, f"CINEMATIC MODULE 0{scene_num} / 03", (950, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (148, 163, 184), 2)
    
    # 3. Left Side: High-Tech 3D Holographic Visual Container Box
    box_x1, box_y1, box_x2, box_y2 = 60, 130, 560, 590
    cv2.rectangle(frame, (box_x1, box_y1), (box_x2, box_y2), (18, 25, 43), -1)
    cv2.rectangle(frame, (box_x1, box_y1), (box_x2, box_y2), (56, 189, 248), 2)
    
    # Render realistic animated technical component blueprints inside the box
    if scene_num == 1:
        # Dynamic Rotary Regulator Dial Graphic
        cv2.circle(frame, (310, 360), 120, (30, 41, 59), -1)
        cv2.circle(frame, (310, 360), 120, (250, 204, 21), 3)
        # Animated spinning indicator
        angle = (frame_idx * 3) % 360
        rad = np.deg2rad(angle)
        nx = int(310 + 85 * np.cos(rad))
        ny = int(360 + 85 * np.sin(rad))
        cv2.line(frame, (310, 360), (nx, ny), (74, 222, 128), 5)
        cv2.circle(frame, (310, 360), 18, (255, 255, 255), -1)
        cv2.putText(frame, "STATUS: SPEED LEVEL ACTIVE", (130, 530), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (250, 204, 21), 2)

    elif scene_num == 2:
        # Dynamic Resistor & Circuit Flow Graphic
        cv2.rectangle(frame, (160, 310), (460, 410), (74, 222, 128), -1)
        cv2.rectangle(frame, (220, 310), (250, 410), (248, 113, 113), -1)
        cv2.rectangle(frame, (320, 310), (350, 410), (56, 189, 248), -1)
        cv2.line(frame, (80, 360), (160, 360), (200, 200, 200), 3)
        cv2.line(frame, (460, 360), (540, 360), (200, 200, 200), 3)
        cv2.putText(frame, "STATUS: VOLTAGE DROP MANAGED", (140, 530), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (74, 222, 128), 2)

    else:
        # Dynamic Terminal Wiring Ports Graphic
        cv2.rectangle(frame, (110, 320), (510, 400), (40, 51, 75), -1)
        cv2.circle(frame, (200, 360), 22, (248, 113, 113), -1)
        cv2.circle(frame, (310, 360), 22, (248, 113, 113), -1)
        cv2.circle(frame, (420, 360), 22, (248, 113, 113), -1)
        cv2.putText(frame, "STATUS: 0% MISTAKE WIRING CHECK", (130, 530), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (248, 113, 113), 2)

    # Component Title Tag
    cv2.rectangle(frame, (box_x1, 590), (box_x2, 640), (24, 32, 54), -1)
    cv2.putText(frame, part_name, (80, 623), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # 4. Right Side: Cinematic Script & Technical Explanation Layout
    cv2.putText(frame, "Engineering Analysis & Breakdown", (600, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.95, (255, 255, 255), 2)
    cv2.line(frame, (600, 195), (1230, 195), (74, 222, 128), 2)

    cv2.putText(frame, "Target Component:", (600, 260), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (148, 163, 184), 1)
    cv2.putText(frame, part_name, (600, 305), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (56, 189, 248), 2)

    cv2.putText(frame, "Core Function & Operations:", (600, 395), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (148, 163, 184), 1)
    cv2.putText(frame, description[0], (600, 445), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (226, 232, 240), 1)
    cv2.putText(frame, description[1], (600, 490), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (226, 232, 240), 1)

    # 5. Bottom Status Compliance Bar
    cv2.rectangle(frame, (0, 655), (1280, 720), (15, 22, 38), -1)
    cv2.putText(frame, "Security Shield: Strict 0% Mistake Policy Enforced | Fully Verified Blueprint", (40, 695), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (148, 163, 184), 1)

def run_production_and_video_agent():
    print("--------------------------------------------------")
    print("   🎬 PRODUCTION AGENT: CINEMATIC STUDIO RENDER    ")
    print("--------------------------------------------------")
    
    script_path = "channels/channel_1_repair/drafts/fan_regulator_script.txt"
    output_dir = "channels/channel_1_repair/drafts"
    os.makedirs(output_dir, exist_ok=True)
    
    if not os.path.exists(script_path):
        print("[ERROR] Script nahi mili! Pehle script_generator.py run karein.")
        return

    # Generate Professional Voiceover Audio
    audio_path = os.path.join(output_dir, "voiceover.mp3")
    print("[INFO] Synthesizing professional studio voiceover...")
    
    voice_text = (
        "Welcome to AI Empire Professional Repair Academy. "
        "Let us examine the precise engineering mechanics on screen. "
        "First, the Rotary Speed Dial regulates multi-step voltage safely. "
        "Second, the Step Resistor manages current drop to protect internal coils. "
        "Third, the Live Terminal Block secures power connections under our strict zero percent mistake policy."
    )
    tts = gTTS(text=voice_text, lang='en', slow=False)
    tts.save(audio_path)

    audio_clip = AudioFileClip(audio_path)
    duration = audio_clip.duration

    video_path = os.path.join(output_dir, "fan_regulator_repair_draft.mp4")
    temp_silent = os.path.join(output_dir, "temp_cinematic_pro.mp4")
    
    fps = 24
    width, height = 1280, 720
    total_frames = int(duration * fps)
    scene_frames = total_frames // 3

    print("[INFO] Rendering high-definition cinematic studio frames...")
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(temp_silent, fourcc, fps, (width, height))

    for i in range(total_frames):
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        scene_frame_idx = i % scene_frames
        
        if i < scene_frames:
            draw_cinematic_studio_frame(
                frame,
                part_name="1. Rotary Speed Control Dial",
                description=[
                    "Interactive animated speed dial mechanism.",
                    "Regulates input voltage across levels 1 to 5."
                ],
                scene_num=1,
                frame_idx=scene_frame_idx
            )
        elif i < scene_frames * 2:
            draw_cinematic_frame = draw_cinematic_studio_frame(
                frame,
                part_name="2. Step Resistor Bank",
                description=[
                    "Active resistance and thermal drop management.",
                    "Prevents electrical overloads and motor humming."
                ],
                scene_num=2,
                frame_idx=scene_frame_idx
            )
        else:
            draw_cinematic_studio_frame(
                frame,
                part_name="3. Secure Terminal Block",
                description=[
                    "Heavy-duty live phase and neutral ports.",
                    "Inspected and locked under 0% mistake policy."
                ],
                scene_num=3,
                frame_idx=scene_frame_idx
            )

        out.write(frame)

    out.release()
    print("[SUCCESS] Cinematic video frames compiled.")

    print("[INFO] Synchronizing audio with cinematic video stream...")
    try:
        silent_clip = VideoFileClip(temp_silent)
        final_video = silent_clip.with_audio(audio_clip)
        final_video.write_videofile(video_path, fps=24, codec='libx264', audio_codec='aac', logger=None)
        
        if os.path.exists(temp_silent):
            os.remove(temp_silent)

        print("\n--------------------------------------------------")
        print("✅ [PRODUCTION SUCCESS]: CINEMATIC STUDIO VIDEO READY!")
        print(f" -> Playable Video Saved At : {video_path}")
        print("--------------------------------------------------")
    
    except Exception as e:
        print(f"[ERROR] Cinematic compilation error: {e}")

if __name__ == "__main__":
    run_production_and_video_agent()