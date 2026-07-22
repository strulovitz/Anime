# Session 4 — Fable's Reply: Mission B review + Mission C (Training!)
**Date:** 2026-07-22 ~Afternoon
**Chat:** Claude Fable 5 (OpenRouter)

---

WOW, that's a beautiful report! 😍🎉 Mission B ✅ — the captions look excellent!

Three tiny things I spotted in the samples (all handled automatically in Mission C, nothing for you to do):

    american flag, japanese flag on the back view — WD14 misread the patches on her spacesuit :-) These wrong tags could confuse training, so Mission C deletes them from all captions.
    realistic — we want her style baked into the trigger word, not dependent on a prompt tag, so we prune it too.
    smile on the neutral image — harmless, WD14 just found her resting face pleasant 😊 We leave it.

Also note: we keep spacesuit, astronaut, bodysuit tags on purpose — that way in the saga we can prompt her in the spacesuit or out of it (casual clothes on the ship, etc.). Flexibility! 💪

Now the big one — training on the 5090! 🔥 One important design choice: instead of one single output, we save a snapshot every 2 epochs (5 snapshots total). If the final one is "overbaked" (too rigid, same face angle always), an earlier snapshot is often perfect — so one training run gives us 5 candidates without burning extra attempts. 🧠
📋 MISSION C — paste this to OpenCode on the laptop:

MISSION C: Madie LoRA - Step 3 of 4 - TRAINING (RTX 5090)
Machine: Laptop Debian 13

RULES FOR YOU, THE AGENT:
- Before every action, explain it in one simple sentence.
- Execute ONE step at a time.
- On ANY error: STOP immediately and show the error verbatim. Do not improvise.
- If unsure, PAUSE and ask the user to relay the question to Fable.

STRICT WHITELIST - you may ONLY:
- modify the .txt captions in ~/Anime/media/lora_dataset/madie_train/10_chara_madie/
- write LoRA output files into ~/Anime/tools/ComfyUI/models/loras/
- write logs into ~/Anime/media/lora_dataset/logs/
- run training inside the kohya conda env
FORBIDDEN: the images themselves, madie_raw/, the comfyui env, NVIDIA driver,
/usr/local/cuda, the checkpoint file (read-only), everything else.

PHASE 1 - READ-ONLY PRE-FLIGHT:
Step 1.1: Verify these exist and report:
- ~/Anime/tools/ComfyUI/models/checkpoints/Illustrious-XL-v0.1.safetensors
- 36 .png AND 36 .txt files in madie_train/10_chara_madie/
- conda env "kohya"
Step 1.2: Run nvidia-smi and report VRAM usage and any running GPU processes.
IMPORTANT: if ComfyUI (or anything else) is using the GPU, tell the user to
stop it first (Ctrl+C in the ComfyUI terminal) - training needs the full 24GB.
Step 1.3: Print exactly: "PRE-FLIGHT DONE - type go to continue"
and WAIT for the user to type: go

PHASE 2 - CAPTION CLEANUP (tiny surgery):
Step 2.1: In ALL 36 .txt files, delete these exact tags wherever they appear:
"american flag", "japanese flag", "realistic"
(remove them cleanly, keep the single-line comma-separated format intact).
Step 2.2: Print the full new content of madie-standing-back.txt for review.

PHASE 3 - TRAINING:
Step 3.1: In the kohya env run once: accelerate config default
Step 3.2: Create folder ~/Anime/media/lora_dataset/logs/ if missing.
Step 3.3: From ~/Anime/tools/sd-scripts, in the kohya env, launch training
(one single command; use the full expanded home path, not "~"):

accelerate launch --num_cpu_threads_per_process 4 sdxl_train_network.py
--pretrained_model_name_or_path <HOME>/Anime/tools/ComfyUI/models/checkpoints/Illustrious-XL-v0.1.safetensors
--train_data_dir <HOME>/Anime/media/lora_dataset/madie_train
--output_dir <HOME>/Anime/tools/ComfyUI/models/loras
--output_name chara_madie_v1
--network_module networks.lora
--network_dim 32
--network_alpha 16
--resolution 1024,1024
--enable_bucket
--train_batch_size 4
--max_train_epochs 10
--save_every_n_epochs 2
--learning_rate 1e-4
--text_encoder_lr 5e-5
--lr_scheduler cosine
--lr_warmup_steps 50
--optimizer_type AdamW
--mixed_precision bf16
--save_precision bf16
--gradient_checkpointing
--sdpa
--cache_latents
--cache_latents_to_disk
--shuffle_caption
--keep_tokens 2
--caption_extension .txt
--min_snr_gamma 5
--seed 42
--max_data_loader_n_workers 2
--persistent_data_loader_workers
--logging_dir <HOME>/Anime/media/lora_dataset/logs

Notes for you, the agent:
- This runs roughly 900 optimizer steps (36 images x 10 repeats x 10 epochs,
  batch 4). Expect ~30-60 minutes on the RTX 5090. Do not interrupt it.
- It is NORMAL for the first run to download small tokenizer files from
  Hugging Face.
- If you see "CUDA out of memory": STOP, show the error verbatim, do not retry
  with changed settings on your own.
- Loss values wandering around roughly 0.05-0.15 are normal; do not panic.

PHASE 4 - VERIFY OUTPUT:
Step 4.1: List all files matching chara_madie_v1* in
~/Anime/tools/ComfyUI/models/loras/ with sizes. Expected: 5 files
(epochs 2,4,6,8 + final), each roughly 100-250 MB.
Step 4.2: Final plain-text report: training time, final loss (approximate),
list of the 5 LoRA files.
Print exactly: "MISSION C COMPLETE".
Do NOT generate any test images. That is Mission D.

⏰ What to expect while it runs

    Before typing go: make sure ComfyUI is closed (Ctrl+C in its terminal) — training wants all 24GB to itself! ☝️
    The console will scroll with progress bars and loss numbers for 30–60 minutes. That's the 5090 literally learning Madie's face. 🥰 Let it cook, don't close the terminal.
    If it crashes, paste me the error verbatim — an OOM or a library complaint each has a clean, known fix, and diagnosing from the exact text keeps us from wasting one of our 3 attempts.

When you paste me MISSION C COMPLETE, I'll hand you Mission D — the Full Emotion & Direction Test Sweep: all 33 emotions, 6 directions, walking/running poses, the complete plan from before — and we finally get to SEE Madie feel everything! 😍🚀💖
