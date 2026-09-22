import os
import time
import requests
import replicate
from gtts import gTTS
from moviepy import AudioFileClip, VideoFileClip, concatenate_videoclips

# DIRECT TOKEN SETTLED HERE TO FIX 401 ERROR
os.environ["REPLICATE_API_TOKEN"] = "r8_UiPiWod3Ks7Aws6bkbH9EqbVS7lKWIq402hL2"

print("--------------------------------------------------")
print("   🚀 AI EMPIRE: BADA LEVEL SCALE-UP STUDIO ENGINE  ")
print("--------------------------------------------------")

output_dir = "empire_masterclass_output"
os.makedirs(output_dir, exist_ok=True)
final_master_video = os.path.join(output_dir, "ai_empire_masterclass_full.mp4")

scenes = [
    {
        "id": 1,
        "script": "Welcome to AI Empire Advanced Masterclass. Today, we are conducting a complete professional teardown and repair of a ceiling fan regulator. Safety is our top priority, adhering strictly to our zero percent mistake policy.",
        "prompt": "Cinematic wide shot of a professional repair masterclass studio, high-tech engineering workbench, hyper-detailed, 4k resolution."
    },
    {
        "id": 2,
        "script": "First step: Isolate power by shutting off the main circuit breaker. Always use a digital multimeter or voltage tester to verify absolute zero live current before touching any internal wiring.",
        "prompt": "Close-up of a technician's gloved hands using a professional multimeter on a wall electrical switch panel, glowing LED display, photorealistic."
    },
    {
        "id": 3,
        "script": "Next, remove the outer cover plate carefully using insulated screwdrivers. Take a high-resolution photo of the existing terminal connections to ensure correct wire placement during reassembly.",
        "prompt": "Macro close-up shot of hands using an insulated screwdriver to unscrew a wall switch cover plate, high-end professional lighting, 4k."
    },
    {
        "id": 4,
        "script": "Finally, detach the faulty regulator wires from the live and load terminals, mount the new unit securely, and recheck all connections. Your masterclass repair is now complete and fully tested.",
        "prompt": "Detailed cinematic view of internal wiring terminals, copper wires, professional technician hands securing components, studio depth of field."
    }
]

video_clips = []

for scene in scenes:
    print(f"\n[INFO] Processing Scene 0{scene['id']} / 04...")
    
    scene_audio_path = os.path.join(output_dir, f"scene_{scene['id']}_audio.mp3")
    tts = gTTS(text=scene['script'], lang='en', slow=False)
    tts.save(scene_audio_path)
    scene_audio = AudioFileClip(scene_audio_path)
    
    print(f"[AI AGENT] Generating 3D video clip for Scene {scene['id']}...")
    try:
        prediction = replicate.predictions.create(
            model="minimax/video-01",
            input={
                "prompt": scene['prompt'],
                "prompt_optimizer": True
            }
        )
        
        while prediction.status not in ["succeeded", "failed"]:
            time.sleep(4)
            prediction.reload()
            
        if prediction.status == "succeeded":
            output_url = prediction.output
            if isinstance(output_url, list):
                output_url = output_url[0]
                
            clip_path = os.path.join(output_dir, f"scene_{scene['id']}_video.mp4")
            vid_data = requests.get(output_url).content
            with open(clip_path, "wb") as f:
                f.write(vid_data)
                
            v_clip = VideoFileClip(clip_path)
            v_clip = v_clip.with_audio(scene_audio)
            scene_final_path = os.path.join(output_dir, f"scene_{scene['id']}_final.mp4")
            v_clip.write_videofile(scene_final_path, fps=24, codec='libx264', audio_codec='aac', logger=None)
            
            video_clips.append(VideoFileClip(scene_final_path))
            print(f"[SUCCESS] Scene {scene['id']} rendered successfully!")
        else:
            print(f"[ERROR] Scene {scene['id']} AI generation failed.")
            
    except Exception as e:
        print(f"[ERROR] Exception in scene {scene['id']}: {e}")

if video_clips:
    print("\n[INFO] Stitching all scenes together into a grand Masterclass video...")
    master_video = concatenate_videoclips(video_clips)
    master_video.write_videofile(final_master_video, fps=24, codec='libx264', audio_codec='aac', logger=None)
    
    print(f"\n--------------------------------------------------")
    print(f"✅ [EMPIRE MILESTONE REACHED]: BADE LEVEL KA MASTERCLASS READY!")
    print(f" -> Master Video Saved At: {final_master_video}")
    print(f"--------------------------------------------------")
    
    from google.colab import files
    files.download(final_master_video)
else:
    print("[ERROR] No video clips were successfully generated.")
