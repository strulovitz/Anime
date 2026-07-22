#!/usr/bin/env python3
"""
Madie LoRA v2 QUALITY Sweep — Two-pass high-res ComfyUI API Generator
"""
import json, urllib.request, time, os, sys, shutil

COMFY = "http://127.0.0.1:8188"
COMFY_OUTPUT = os.path.expanduser("~/Anime/tools/ComfyUI/output")
SWEEP = os.path.expanduser("~/Anime/media/tests/madie_sweep_v2")
CHECKPOINT = "Illustrious-XL-v0.1.safetensors"

SEED = 123456789
CFG = 4.5

POS_BASE = "masterpiece, best quality, chara_madie, 1girl, solo, mature female, young woman, spacesuit, no headwear"
NEG = "worst quality, low quality, bad anatomy, bad hands, extra digits, watermark, signature, text, black background, helmet, space helmet, headwear, hood, hat, hair ornament, child, chibi, loli, aged down, deformed, large head"

def queue_prompt(prompt_data):
    req = urllib.request.Request(f"{COMFY}/prompt", data=json.dumps(prompt_data).encode('utf-8'),
                                 headers={'Content-Type': 'application/json'})
    return json.loads(urllib.request.urlopen(req).read())['prompt_id']

def get_history(prompt_id):
    with urllib.request.urlopen(f"{COMFY}/history/{prompt_id}") as f:
        return json.loads(f.read())

def wait_for_image(prompt_id, timeout=600):
    start = time.time()
    while time.time() - start < timeout:
        history = get_history(prompt_id)
        if prompt_id in history:
            outputs = history[prompt_id]['outputs']
            for node_id, output in outputs.items():
                if 'images' in output and len(output['images']) > 0:
                    return output['images'][0]['filename']
        time.sleep(3)
    raise TimeoutError(f"Timeout waiting for prompt {prompt_id}")

def build_workflow(lora_file, tags, prefix, canvas_w, canvas_h):
    """Build two-pass quality pipeline workflow"""
    prompt_text = f"{POS_BASE}, {tags}, simple background, grey background"
    upscale_w = int(canvas_w * 1.5)
    upscale_h = int(canvas_h * 1.5)

    return {
        "1": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": CHECKPOINT}},
        "2": {"class_type": "LoraLoader", "inputs": {"model": ["1",0], "clip": ["1",1], "lora_name": lora_file, "strength_model": 1.0, "strength_clip": 1.0}},
        "3": {"class_type": "CLIPTextEncode", "inputs": {"text": prompt_text, "clip": ["2",1]}},
        "4": {"class_type": "CLIPTextEncode", "inputs": {"text": NEG, "clip": ["2",1]}},
        "5": {"class_type": "EmptyLatentImage", "inputs": {"width": canvas_w, "height": canvas_h, "batch_size": 1}},
        "6": {"class_type": "KSampler", "inputs": {"model": ["2",0], "positive": ["3",0], "negative": ["4",0], "latent_image": ["5",0], "seed": SEED, "steps": 40, "cfg": CFG, "sampler_name": "euler_ancestral", "scheduler": "normal", "denoise": 1.0}},
        "7": {"class_type": "LatentUpscaleBy", "inputs": {"samples": ["6",0], "scale_by": 1.5, "upscale_method": "bislerp"}},
        "8": {"class_type": "KSampler", "inputs": {"model": ["2",0], "positive": ["3",0], "negative": ["4",0], "latent_image": ["7",0], "seed": SEED, "steps": 20, "cfg": CFG, "sampler_name": "euler_ancestral", "scheduler": "normal", "denoise": 0.45}},
        "9": {"class_type": "VAEDecode", "inputs": {"samples": ["8",0], "vae": ["1",2]}},
        "10": {"class_type": "SaveImage", "inputs": {"images": ["9",0], "filename_prefix": prefix}}
    }

def generate_one(lora_file, tags, prefix, output_dir, canvas_w, canvas_h):
    print(f"  {prefix} ...", end=" ", flush=True)
    workflow = build_workflow(lora_file, tags, prefix, canvas_w, canvas_h)
    t0 = time.time()
    prompt_id = queue_prompt({"prompt": workflow})
    filename = wait_for_image(prompt_id)
    elapsed = time.time() - t0
    src = os.path.join(COMFY_OUTPUT, filename)
    dst = os.path.join(output_dir, f"{prefix}.png")
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"OK ({elapsed:.0f}s)")
    else:
        print(f"WARNING: missing {filename}")
    return prompt_id

# ---- JOB DATA (unchanged from Mission D) ----

EMOTIONS = [
    ("neutral","neutral expression, closed mouth"),("happiness","happy, smile"),("sadness","sad, frown"),
    ("anger","angry, furrowed brow"),("fear","scared, wide eyes, trembling"),("surprise","surprised, open mouth, wide eyes"),
    ("disgust","disgust, wavy mouth"),("contempt","smug, narrowed eyes, smirk"),("joy","joyful, grin, sparkling eyes"),
    ("love","loving gaze, blush, smile"),("hate","glaring, hateful stare, shaded face"),("hope","hopeful, gentle smile, looking up"),
    ("boredom","bored, half-closed eyes"),("calmness","calm, serene, soft smile, closed eyes"),
    ("excitement","excited, open mouth smile, clenched hands"),("interest","curious, head tilt, bright eyes"),
    ("wonder","wonder, parted lips, wide eyes, looking up"),("awe","awe, amazed, hand over own mouth"),
    ("adoration","adoring gaze, sparkling eyes, own hands clasped"),("amusement","amused, giggling, hand over own mouth"),
    ("compassion","compassionate, gentle expression, warm smile"),("crying","crying, tears, tearful eyes"),
    ("embarrassment","embarrassed, full blush, averting gaze"),("envy","envious, pout, side glance"),
    ("gratitude","grateful, warm smile, hand on own chest"),("horror","horrified, wide eyes, open mouth"),
    ("laughing","laughing, open mouth, closed eyes"),("rage","enraged, clenched teeth, screaming"),
    ("relaxation","relaxed, content, closed eyes"),("sensory_pleasure","blissful, closed eyes, content smile"),
    ("shame","ashamed, looking down, downcast eyes"),("depression","depressed, empty eyes, head down"),
    ("arousal","flustered, heavy blush, half-closed eyes"),
]

DIRECTIONS = ["front view","three-quarter view","from side, profile","from side, profile, looking at viewer","from behind, looking back","from behind, facing away"]
POSES = ["standing","walking","running"]

COMBOS = [
    ("combo01_laughing_walk","walking, laughing, open mouth, full body"),
    ("combo02_scared_run","running, scared, wide eyes, full body"),
    ("combo03_crying_side","from side, profile, crying, tears, upper body"),
    ("combo04_bored_sit","sitting, bored, head rest, full body"),
    ("combo05_crossed_smug","standing, crossed arms, smug, smirk, full body"),
    ("combo06_back_look_smile","from behind, looking back, smile, full body"),
    ("combo07_hips_angry","hands on own hips, angry, full body"),
    ("combo08_waving_happy","waving, happy, smile, full body"),
    ("combo09_kneel_depressed","kneeling, depressed, head down, full body"),
    ("combo10_action_rage","action pose, enraged, clenched fist, full body"),
]

DUEL_JOBS = [
    ("1_neutral","portrait, upper body, looking at viewer, neutral expression"),
    ("2_calm","portrait, upper body, looking at viewer, calm, serene, closed eyes"),
    ("3_front_smile","full body, standing, front view, smile, hand on hip"),
    ("4_behind","full body, from behind, facing away, standing"),
]

def main():
    if len(sys.argv) < 2:
        print("Usage: madie_sweep.py [duel|<epoch_number>]")
        sys.exit(1)

    mode = sys.argv[1]
    os.makedirs(SWEEP, exist_ok=True)

    if mode == "duel":
        print("=== EPOCH DUEL (8 vs 10, 8 images, QUALITY) ===")
        out = os.path.join(SWEEP, "duel")
        os.makedirs(out, exist_ok=True)
        start = time.time()
        count = 0
        for epoch_label, lora_file in [("epoch08","chara_madie_v1-000008.safetensors"),("epoch10","chara_madie_v1.safetensors")]:
            for suffix, tags in DUEL_JOBS:
                prefix = f"{epoch_label}_{suffix}"
                if "portrait" in tags or "upper body" in tags:
                    canvas = (1024, 1024)
                else:
                    canvas = (832, 1216)
                generate_one(lora_file, tags, prefix, out, *canvas)
                count += 1
        elapsed = time.time() - start
        print(f"\nDuel done! {count} images in {elapsed:.0f}s (~{elapsed/count:.0f}s/image). Output: {out}")
        print("BUILD GRID — which epoch wins? (8 or 10)")

    else:
        epoch_num = mode.lstrip("epoch")
        lora_file = "chara_madie_v1.safetensors" if epoch_num == "10" else f"chara_madie_v1-00000{epoch_num}.safetensors"
        start = time.time()
        total = 0

        # 4A
        print("=== EMOTIONS (33) ===")
        out = os.path.join(SWEEP, "emotions"); os.makedirs(out, exist_ok=True)
        for name, tags in EMOTIONS:
            generate_one(lora_file, f"portrait, upper body, looking at viewer, {tags}", name, out, 1024, 1024)
            total += 1

        # 4B
        print("\n=== DIRECTIONS (18) ===")
        out = os.path.join(SWEEP, "directions"); os.makedirs(out, exist_ok=True)
        for direction in DIRECTIONS:
            for pose in POSES:
                safe = direction.replace(" ","_").replace(",","")
                prefix = f"{safe}_{pose}"
                generate_one(lora_file, f"full body, light smile, {direction}, {pose}", prefix, out, 832, 1216)
                total += 1

        # 4C
        print("\n=== COMBOS (10) ===")
        out = os.path.join(SWEEP, "combos"); os.makedirs(out, exist_ok=True)
        for prefix, tags in COMBOS:
            generate_one(lora_file, tags, prefix, out, 832, 1216)
            total += 1

        elapsed = time.time() - start
        print(f"\nDone! {total} images in {elapsed:.0f}s (~{elapsed/total:.0f}s/image). Output: {SWEEP}/")

        # Checklist
        all_images = []
        for sub in ["emotions","directions","combos"]:
            d = os.path.join(SWEEP, sub)
            if os.path.exists(d):
                for f in sorted(os.listdir(d)):
                    if f.endswith(".png"):
                        all_images.append(os.path.join(sub, f))
        checklist = os.path.join(SWEEP, "madie_sweep_v2_results.txt")
        with open(checklist, "w") as f:
            for img in all_images:
                f.write(f"{img}  face[ ] hair[ ] emotion/pose[ ] anatomy[ ]\n")
        print(f"Checklist: {checklist}")

if __name__ == "__main__":
    main()
