#!/usr/bin/env python3
"""
Madie LoRA Test Sweep — ComfyUI API Generator
Submits workflows to ComfyUI at http://127.0.0.1:8188
"""
import json, urllib.request, urllib.parse, time, os, sys, shutil

COMFY = "http://127.0.0.1:8188"
COMFY_OUTPUT = os.path.expanduser("~/Anime/tools/ComfyUI/output")
SWEEP = os.path.expanduser("~/Anime/media/tests/madie_sweep")
CHECKPOINT = "Illustrious-XL-v0.1.safetensors"

SEED = 123456789
STEPS = 28
CFG = 4.5

POS_BASE = "masterpiece, best quality, chara_madie, 1girl, solo, spacesuit"
NEG = "worst quality, low quality, bad anatomy, bad hands, extra digits, watermark, signature, text, black background"

def queue_prompt(prompt_data):
    req = urllib.request.Request(
        f"{COMFY}/prompt",
        data=json.dumps(prompt_data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    resp = json.loads(urllib.request.urlopen(req).read())
    return resp['prompt_id']

def get_history(prompt_id):
    with urllib.request.urlopen(f"{COMFY}/history/{prompt_id}") as f:
        return json.loads(f.read())

def wait_for_image(prompt_id, timeout=300):
    """Wait for image generation to complete, return output filename"""
    start = time.time()
    while time.time() - start < timeout:
        history = get_history(prompt_id)
        if prompt_id in history:
            outputs = history[prompt_id]['outputs']
            for node_id, output in outputs.items():
                if 'images' in output and len(output['images']) > 0:
                    return output['images'][0]['filename']
        time.sleep(2)
    raise TimeoutError(f"Timeout waiting for prompt {prompt_id}")

def build_workflow(lora_file, tags, prefix):
    """Build a ComfyUI workflow JSON for SDXL + LoRA generation"""
    prompt_text = f"{POS_BASE}, {tags}, simple background, grey background"

    workflow = {
        "1": {
            "class_type": "CheckpointLoaderSimple",
            "inputs": {"ckpt_name": CHECKPOINT}
        },
        "2": {
            "class_type": "LoraLoader",
            "inputs": {
                "model": ["1", 0],
                "clip": ["1", 1],
                "lora_name": lora_file,
                "strength_model": 0.9,
                "strength_clip": 0.9
            }
        },
        "3": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": prompt_text,
                "clip": ["2", 1]
            }
        },
        "4": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": NEG,
                "clip": ["2", 1]
            }
        },
        "5": {
            "class_type": "EmptyLatentImage",
            "inputs": {
                "width": 1024,
                "height": 1024,
                "batch_size": 1
            }
        },
        "6": {
            "class_type": "KSampler",
            "inputs": {
                "model": ["2", 0],
                "positive": ["3", 0],
                "negative": ["4", 0],
                "latent_image": ["5", 0],
                "seed": SEED,
                "steps": STEPS,
                "cfg": CFG,
                "sampler_name": "euler_ancestral",
                "scheduler": "normal",
                "denoise": 1.0
            }
        },
        "7": {
            "class_type": "VAEDecode",
            "inputs": {
                "samples": ["6", 0],
                "vae": ["1", 2]
            }
        },
        "8": {
            "class_type": "SaveImage",
            "inputs": {
                "images": ["7", 0],
                "filename_prefix": prefix
            }
        }
    }

    return workflow

def generate_one(lora_full, tags, prefix, output_dir):
    """Generate one image and copy to output folder"""
    lora_file = lora_full  # e.g. "chara_madie_v1-000004.safetensors"

    print(f"  Generating: {prefix} ...", end=" ", flush=True)
    workflow = build_workflow(lora_file, tags, prefix)
    prompt_id = queue_prompt({"prompt": workflow})
    filename = wait_for_image(prompt_id)

    # ComfyUI saves with prefix + number suffix
    src = os.path.join(COMFY_OUTPUT, filename)
    dst = os.path.join(output_dir, f"{prefix}.png")

    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"OK ({filename})")
    else:
        print(f"WARNING: file not found at {src}")
    return prompt_id

# ======== JOB DEFINITIONS ========

SHOOTOUT_SNAPSHOTS = {
    "epoch04": "chara_madie_v1-000004.safetensors",
    "epoch06": "chara_madie_v1-000006.safetensors",
    "epoch08": "chara_madie_v1-000008.safetensors",
    "epoch10": "chara_madie_v1.safetensors",
}

SHOOTOUT_JOBS = [
    ("A_neutral", "portrait, upper body, looking at viewer, neutral expression, closed mouth"),
    ("B_laughing", "portrait, upper body, looking at viewer, laughing, open mouth"),
    ("C_fullbody", "full body, standing, front view, smile, hand on hip"),
]

EMOTIONS = [
    ("neutral", "neutral expression, closed mouth"),
    ("happiness", "happy, smile"),
    ("sadness", "sad, frown"),
    ("anger", "angry, furrowed brow"),
    ("fear", "scared, wide eyes, trembling"),
    ("surprise", "surprised, open mouth, wide eyes"),
    ("disgust", "disgust, wavy mouth"),
    ("contempt", "smug, narrowed eyes, smirk"),
    ("joy", "joyful, grin, sparkling eyes"),
    ("love", "loving gaze, blush, smile"),
    ("hate", "glaring, hateful stare, shaded face"),
    ("hope", "hopeful, gentle smile, looking up"),
    ("boredom", "bored, half-closed eyes"),
    ("calmness", "calm, serene, soft smile, closed eyes"),
    ("excitement", "excited, open mouth smile, clenched hands"),
    ("interest", "curious, head tilt, bright eyes"),
    ("wonder", "wonder, parted lips, wide eyes, looking up"),
    ("awe", "awe, amazed, hand over own mouth"),
    ("adoration", "adoring gaze, sparkling eyes, own hands clasped"),
    ("amusement", "amused, giggling, hand over own mouth"),
    ("compassion", "compassionate, gentle expression, warm smile"),
    ("crying", "crying, tears, tearful eyes"),
    ("embarrassment", "embarrassed, full blush, averting gaze"),
    ("envy", "envious, pout, side glance"),
    ("gratitude", "grateful, warm smile, hand on own chest"),
    ("horror", "horrified, wide eyes, open mouth"),
    ("laughing", "laughing, open mouth, closed eyes"),
    ("rage", "enraged, clenched teeth, screaming"),
    ("relaxation", "relaxed, content, closed eyes"),
    ("sensory_pleasure", "blissful, closed eyes, content smile"),
    ("shame", "ashamed, looking down, downcast eyes"),
    ("depression", "depressed, empty eyes, head down"),
    ("arousal", "flustered, heavy blush, half-closed eyes"),
]

DIRECTIONS = [
    "front view",
    "three-quarter view",
    "from side, profile",
    "from side, profile, looking at viewer",
    "from behind, looking back",
    "from behind, facing away",
]

POSES = ["standing", "walking", "running"]

COMBOS = [
    ("combo01_laughing_walk", "walking, laughing, open mouth, full body"),
    ("combo02_scared_run", "running, scared, wide eyes, full body"),
    ("combo03_crying_side", "from side, profile, crying, tears, upper body"),
    ("combo04_bored_sit", "sitting, bored, head rest, full body"),
    ("combo05_crossed_smug", "standing, crossed arms, smug, smirk, full body"),
    ("combo06_back_look_smile", "from behind, looking back, smile, full body"),
    ("combo07_hips_angry", "hands on own hips, angry, full body"),
    ("combo08_waving_happy", "waving, happy, smile, full body"),
    ("combo09_kneel_depressed", "kneeling, depressed, head down, full body"),
    ("combo10_action_rage", "action pose, enraged, clenched fist, full body"),
]

# ======== RUN ========

def main():
    if len(sys.argv) < 2:
        print("Usage: madie_sweep.py [shootout|<epoch_number>]")
        print("  shootout - generate 12 comparison images")
        print("  <epoch>  - generate full sweep with chosen epoch (4, 6, 8, or 10)")
        sys.exit(1)

    mode = sys.argv[1]
    os.makedirs(SWEEP, exist_ok=True)

    if mode == "shootout":
        print("=== SNAPSHOT SHOOTOUT (12 images) ===")
        out = os.path.join(SWEEP, "shootout")
        os.makedirs(out, exist_ok=True)
        count = 0
        start = time.time()
        for label, lora in SHOOTOUT_SNAPSHOTS.items():
            for suffix, tags in SHOOTOUT_JOBS:
                prefix = f"{label}_{suffix}"
                generate_one(lora, tags, prefix, out)
                count += 1
        elapsed = time.time() - start
        print(f"\nDone! {count} images in {elapsed:.0f}s")
        print(f"Output: {out}")
        print(f"GOOD - which epoch wins? (4, 6, 8 or 10)")

    else:
        epoch = mode.lstrip("epoch")
        if epoch == "10":
            lora_file = "chara_madie_v1.safetensors"
        else:
            lora_file = f"chara_madie_v1-00000{epoch}.safetensors"

        start = time.time()
        total = 0

        # 4A - Emotions
        print(f"=== Phase 4A: EMOTIONS (33 images) ===")
        out = os.path.join(SWEEP, "emotions")
        os.makedirs(out, exist_ok=True)
        for name, tags in EMOTIONS:
            base_tags = "portrait, upper body, looking at viewer"
            generate_one(lora_file, f"{base_tags}, {tags}", name, out)
            total += 1

        # 4B - Directions
        print(f"\n=== Phase 4B: DIRECTIONS (18 images) ===")
        out = os.path.join(SWEEP, "directions")
        os.makedirs(out, exist_ok=True)
        for direction in DIRECTIONS:
            for pose in POSES:
                safe_dir = direction.replace(" ", "_").replace(",", "")
                prefix = f"{safe_dir}_{pose}"
                tags = f"full body, light smile, {direction}, {pose}"
                generate_one(lora_file, tags, prefix, out)
                total += 1

        # 4C - Combos
        print(f"\n=== Phase 4C: COMBOS (10 images) ===")
        out = os.path.join(SWEEP, "combos")
        os.makedirs(out, exist_ok=True)
        for prefix, tags in COMBOS:
            generate_one(lora_file, tags, prefix, out)
            total += 1

        elapsed = time.time() - start
        print(f"\nDone! {total} images in {elapsed:.0f}s (~{elapsed/total:.0f}s/image)")
        print(f"Output: {SWEEP}/")

        # Results checklist
        all_images = []
        for sub in ["emotions", "directions", "combos"]:
            d = os.path.join(SWEEP, sub)
            if os.path.exists(d):
                for f in sorted(os.listdir(d)):
                    if f.endswith(".png"):
                        all_images.append(os.path.join(sub, f))

        checklist = os.path.join(SWEEP, "madie_sweep_results.txt")
        with open(checklist, "w") as f:
            for img in all_images:
                f.write(f"{img}  face[ ] hair[ ] emotion/pose[ ] anatomy[ ]\n")

        print(f"Checklist: {checklist}")

if __name__ == "__main__":
    main()
