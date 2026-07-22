# Session 4 — Fable's Reply: Black BG Answer + Mission B
**Date:** 2026-07-22 ~Afternoon
**Chat:** Claude Fable 5 (OpenRouter)

---

Excellent work! Mission A ✅ — and GREAT question about the black background! 🎉
The black background answer: NO transparency! ⚫🚫

Do not make them transparent. Here's why, in simple terms :-)

    SDXL/Illustrious training cannot see transparency. The training script flattens the alpha channel anyway — usually to black or white — so you'd do work for nothing (or worse, get ugly edge halos around her hair from imperfect cutouts).
    The real risk with 36× identical black backgrounds is different: the LoRA might learn "Madie = always dark background" (this is called background bleed). The correct fix is captioning, not editing: we make sure every caption contains the tag black background. When the model reads that tag on every image, it learns "the blackness belongs to that tag, NOT to chara_madie" — and at generation time we simply prompt other backgrounds. 🧠✨
    Insurance policy: Phase 2 of our test sweep uses simple background, grey background on every image — so if any dark bleed survived, we'll see it instantly. If it's bad, Plan B is automated background replacement (rembg → paste onto varied backgrounds) and a retrain — that would be attempt 2 of our 3. But usually the caption trick is enough, so we don't burn an attempt preemptively.

Mission B below already bakes the black background tag into every caption automatically. 💪
📋 MISSION B — paste this to OpenCode on the laptop:

MISSION B: Madie LoRA - Step 2 of 4 - Kohya Install + Captions + Checkpoint
Machine: Laptop Debian 13 (RTX 5090)

RULES FOR YOU, THE AGENT:
- Before every action, explain it in one simple sentence.
- Execute ONE step at a time. Never batch steps.
- On ANY error: STOP immediately and show the error verbatim. Do not improvise.
- If unsure, PAUSE and ask the user to relay the question to Fable.

STRICT WHITELIST - you may ONLY:
- create ONE new conda env named: kohya
- clone into: ~/Anime/tools/sd-scripts
- create/modify .txt caption files inside:
  ~/Anime/media/lora_dataset/madie_train/10_chara_madie/
- download ONE checkpoint file into the ComfyUI models/checkpoints folder
  (you will locate it in Phase 1)
- READ ONLY: ~/Anime/tools/start_comfyui.sh, the dataset images
FORBIDDEN: NVIDIA driver, /usr/local/cuda, the comfyui conda env (never
modify it), the original images in madie_raw/, ~/.bashrc, everything else.

PHASE 1 - READ-ONLY DIAGNOSTICS:
Step 1.1: Run: df -h ~ (we need at least 30GB free; expected ~1.4TB).
Step 1.2: Read ~/Anime/tools/start_comfyui.sh and report the full path where
ComfyUI is installed. The checkpoint will go into <ComfyUI>/models/checkpoints/.
Step 1.3: Confirm internet works: curl -sI https://huggingface.co | head -n 1
Step 1.4: Report findings. Print exactly:
"DIAGNOSTICS DONE - type go to continue" and WAIT for the user to type: go

PHASE 2 - KOHYA ENVIRONMENT:
Step 2.1: conda create -n kohya python=3.10 -y
Step 2.2: git clone https://github.com/kohya-ss/sd-scripts.git
~/Anime/tools/sd-scripts (use the default main branch)
Step 2.3: Inside the kohya env, install PyTorch with CUDA 12.8 wheels
(the RTX 5090 is Blackwell architecture and REQUIRES cu128 wheels):
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128
Step 2.4: pip install -r ~/Anime/tools/sd-scripts/requirements.txt
then: pip install onnxruntime
Step 2.5: Verify in the kohya env python: import torch;
print(torch.__version__, torch.cuda.is_available(),
torch.cuda.get_device_name(0)). STOP if is_available is not True.

PHASE 3 - WD14 CAPTIONING + CAPTION SURGERY:
Step 3.1: From ~/Anime/tools/sd-scripts, run the WD14 tagger in the kohya env:
python finetune/tag_images_by_wd14_tagger.py
~/Anime/media/lora_dataset/madie_train/10_chara_madie
--repo_id SmilingWolf/wd-swinv2-tagger-v3 --onnx --batch_size 4
--caption_extension .txt --thresh 0.35 --remove_underscore
Step 3.2: Verify 36 .txt files were created (one per image).
Step 3.3: Write and run a small python script that post-processes EVERY .txt:
a) Derive the emotion/pose phrase from the image filename:
   strip the "madie-" prefix and the ".png", replace hyphens with spaces.
   Three special cases:
   "standing front"      -> use: "standing, front view"
   "standing back"       -> use: "standing, from behind"
   "standing right side" -> use: "standing, from side, profile"
   "sensory pleasure" stays as the two words: sensory pleasure
b) DELETE from the WD14 tags any tag describing her intrinsic appearance,
   so the trigger word absorbs her identity. Delete tags containing any of:
   "brown hair", "black hair", "brunette", "long hair", "short hair",
   "medium hair", "eyes" (any eye color tag), "lips", "bangs", "ponytail",
   "braid", "hair bun", "sidelocks".
   KEEP all expression, pose, camera, clothing and background tags.
c) Ensure the tag "black background" is present (add it if WD14 missed it).
d) Rebuild the caption as ONE line in this exact order:
   chara_madie, <emotion/pose phrase>, <remaining WD14 tags>
Step 3.4: Print the FULL final captions of exactly these 4 files for review:
madie-neutral.txt, madie-laughing.txt, madie-crying.txt,
madie-standing-back.txt
Then print: "CAPTIONS DONE - type go to continue" and WAIT for: go

PHASE 4 - CHECKPOINT DOWNLOAD (after user types go):
Step 4.1: Download the Illustrious-XL base-family checkpoint from Hugging Face
into <ComfyUI>/models/checkpoints/ :
huggingface.co/OnomaAIResearch/Illustrious-xl-early-release-v0
file: Illustrious-XL-v0.1.safetensors (about 6.5 GB). Use curl -L with the
resolve/main URL. If Hugging Face fails or the file is missing, STOP and ask
the user to relay the problem to Fable (we have a CivitAI plan B, but it may
need an API key, so do not attempt it on your own).
Step 4.2: Verify the downloaded file exists and its size is over 6 GB.
Step 4.3: Final plain-text report: env created, torch version + GPU check,
36 captions rebuilt, checkpoint path + size on disk.
Print exactly: "MISSION B COMPLETE".
Do NOT start training. That is Mission C.

👀 What YOU should check when the agent pauses at "CAPTIONS DONE"

The agent will show you 4 sample captions. A good one looks roughly like this (plain text example):

chara_madie, laughing, 1girl, solo, open mouth, closed eyes, smile, upper body, black background

Checklist for you, Nir :-)

    Every caption starts with chara_madie ✅
    The emotion word from the filename is there ✅
    black background is there ✅
    NO hair color / hair length / eye color tags remain (those must be gone — that's what glues her identity to the trigger word) ✅

If all 4 samples look right → type go and let it download the checkpoint. Then paste me the full MISSION B COMPLETE report (or any error, verbatim), and I'll hand you Mission C — the actual LoRA training on the 5090! 🚀🔥

We're getting really close to seeing Madie come alive in all 33 emotions 😍💖
