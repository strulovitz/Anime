# MASTER REFERENCE — Alpha Babes Illustrated Saga Project
**The Complete Big Picture for Claude Fable (Session 5+)**
**Compiled:** 2026-07-22 Evening
**Purpose:** Single comprehensive document covering everything. Fable loses context between chats — this is the memory. Contains every decision, the full history, the current state, and exactly what remains to be done.

---

## PART 0 — ABOUT THE USER (NIR) 👨‍💻

- Nir, lives in Israel, very limited budget
- COMPLETE BEGINNER with computers, Linux, AI tools
- Be warm, patient, step-by-step, never condescending
- Uses ":-)" a lot — match his energy
- LOVES emojis — use them everywhere! 🎉😍🚀💖✨💪🤩🙏😊🔥💯⭐🌟
- Address Nir by name occasionally, like a friend
- IMPORTANT: Nir uses OpenCode TUI and CANNOT scroll up to see previous output. He only sees the last screen-full. He also CANNOT copy-paste from the terminal. Every report or message meant for him to relay to Fable MUST be written to a file in the GitHub repo with a link provided. Tables (|--|--| markdown) BREAK on copy-paste — use plain text key: value format or bullet lists instead.
- Nir may occasionally press TAB accidentally, toggling OpenCode into "Plan Mode" (read-only). If execution is blocked, politely ask him to exit plan mode.

---

## PART 1 — THE PROJECT: ALPHA BABES 👩‍🚀🌌

### What It Is
- "Alpha Babes": hard sci-fi anime saga. Crew of girls from different countries exploring exoplanets, English with national accents.
- 5 seasons planned, ~20 episodes each.
- Script already written. Character art + spaceship art (interior/exterior) already exist, made by Nir on OpenArt.
- DEADLINE: ~August 3, 2026.
- GIFT for Nir's girlfriend Madie (Romanian). She gave FULL consent for her name and likeness to be used. She REFUSED voice recording/cloning — hard boundary, never suggest it. Character voice is AI-designed from text description — allowed and planned.

### Madie Conversion Rules (baked into everything)
- Lead character "Chief" → named Madie
- Her country UK → Romania
- Comfort ritual tea → borscht (soup)
- Hair redhead → brunette
- Everything else faithful to source documents

### Source Documents
- Story arc (~114 pages), Episode 1 script (~43 pages), ship structure (already .txt), background summary (~32 pages)
- CONVERTED to UTF-8 .txt → AlphaBabes/source_docs/
- STATUS: Ask Nir whether conversion/upload is done yet — this was flagged as pending and may still be.

### Creative Format — FINAL ("Jodorowsky Pivot")
- NOT a video. NOT animated (except maybe a tiny opening if everything else finishes).
- Deliverable: ILLUSTRATED, NARRATED SAGA — still images + narration audio ("the book of the movie that doesn't exist yet").
- Assembled in Adobe Premiere (Windows): Ken Burns pan/zoom on stills + sound design + Nir's existing AI songs for credits.
- Subtitles: Romanian + English, via Aegisub, hardcoded with Avidemux.
- End-card: dedication to Madie.
- Bonus: PDF artbook + one physical printed copy.

### Scenes & Visual Bible Architecture
- Homogeneous-coverage passes: Pass 1 ~25 keystone scenes → Pass 2 ~100 (1 per episode) → Pass 3 ~300 (3 per episode).
- Scene IDs: S{season}E{episode}-{slot}, gapped slots (10,20,30...) for insertions.
- scenes.csv columns: scene_id, season, episode, pass_number, location, characters, description, image_prompt, narration_text, image_status, audio_status, assigned_machine, notes.
- scenes.csv is WRITTEN BY AN AGENT (cheap long-context OpenRouter model inside OpenCode) reading source docs — NOT manually. Fable writes agent instructions and QA-checks outputs. Model choice still pending.
- Visual Bible: locations.csv (location_id, name, ref_image_path, prompt_block, fixed_seed, notes) + refs/ folder of reference images.
- Image consistency = 4 channels: character LoRAs (strongest, tier 1) > IP-Adapter reference images (tier 2) > ControlNet + fixed seeds (tier 3) > text prompt (tier 4, weakest — never carries character or room design).

---

## PART 2 — HARDWARE: THE FOUR MACHINES 🖥️💻

### Machine 1: LAPTOP — Lenovo Legion (Debian 13)
- OS: Debian 13 on external SSD, dual-boot Win11
- User: "nir", 64GB RAM
- GPU: RTX 5090 Max-Q Mobile, 24GB VRAM (Blackwell sm_120, 95W power cap)
- Driver: 580.95.05 (open kernel modules, DKMS-registered)
- Kernel: 6.12.94+deb13-amd64, headers metapackage installed (auto-rebuild on kernel updates)
- CUDA: 13.0 at /usr/local/cuda-13.0
- Secure Boot: OFF
- Disk: ~1.4 TB free on /dev/sda4
- Conda: Miniforge3 26.3.2 (fresh, scorched-earth rebuild)
- Conda envs: "comfyui" (Python 3.12, ComfyUI 0.28.0), "kohya" (Python 3.10, sd-scripts)
- PyTorch: 2.11.0+cu128
- ComfyUI: ~/Anime/tools/ComfyUI, launcher at ~/Anime/tools/start_comfyui.sh
- Mouse: touchpad areas mode (bottom-right = right click), OpenCode TUI mouse=false
- ROLE: Characters + LoRA training (primary machine we've been working on)

### Machine 2: DESKTOP — Lenovo Legion (Mint 22.2)
- OS: Linux Mint 22 on external SSD, dual-boot Win11
- 64GB RAM
- GPU: RTX 4070 Ti, 12GB VRAM
- Current state: NOT YET BOOTSTRAPPED — Linux side untouched, NOT STARTED
- Next step: Install OpenCode, clone repo, run scorched-earth cleanup, nvidia-smi check
- ROLE: Backgrounds, planets, ships, ALL TTS, upscaling

### Machine 3: LAPTOP Win 11
- Factory-fresh (reset July 21)
- ROLE: Nothing until assembly week
- Will get: OpenCode + Git

### Machine 4: DESKTOP Win 11
- Factory-fresh (reset July 21)
- ROLE: Premiere, Aegisub, Avidemux (assembly week)
- Will get: OpenCode + Git

### Division of Labor (Final)
- Laptop 5090: character images + LoRA training (+ optional Wan 2.2 video at the very end)
- Desktop 4070 Ti: backgrounds, planets, ships, ALL TTS, upscaling
- All AI on Linux; Premiere/Aegisub/Avidemux on Windows
- NO swap-as-VRAM; quantization + CPU offload instead

### Sync
- Syncthing for media over LAN — NOT set up yet
- GitHub for text/code — fully working

---

## PART 3 — TOOL STACK (FINAL DECISIONS) 🔧

### Image Generation Hub
- ComfyUI on both Linux machines, models loaded sequentially

### Base Model
- Illustrious XL fine-tunes (specific: OnomaAIResearch/Illustrious-xl-early-release-v0)
- File downloaded: Illustrious-XL-v0.1.safetensors (6.5GB)
- Laptop native: ≤1536×1536; desktop: 1024 FP8, CFG 3.5–5.0, tiled upscale
- Illustrious speaks Danbooru tags — always use Danbooru-style tags in prompts

### Character LoRA
- Kohya sd-scripts for training
- WD14 tagger: SmilingWolf/wd-swinv2-tagger-v3 (ONNX)
- Trigger word: "chara_madie"
- Proven recipe: see Madie LoRA Recipe section below

### TTS (Desktop, Future)
- Qwen3-TTS local: voice design from text description (e.g. "young woman, warm confident voice, English with distinct Romanian accent")
- Export 5s snippet → F5-TTS zero-shot clone for session-to-session voice lock
- Fallback: ElevenLabs Voice Design (Nir has account)
- BOTH media types have paid parachutes: images→OpenArt, voice→ElevenLabs

### Optional Animated Opening (only if 100% done)
- Wan 2.2 14B GGUF Q4/Q8, FLF2V, dual UNET loaders
- Lightning LoRA 8-step (CFG 1.0, LCM, split step 4)
- 720p×81f, --reserve-vram 3.0, sageattention
- Lip-sync: MuseTalk or skip

### Agents & AI Access
- Everything via OpenRouter (Israeli credit cards declined by Alibaba direct)
- Agent tooling: OpenCode ONLY on all four environments
- OpenClaw: REJECTED — "One agent tool everywhere = one thing to learn, one thing that can break. Decision closed."

---

## PART 4 — AGENT-FIRST WORKFLOW DOCTRINE 🤖

Every mission Fable writes for OpenCode must include:
- Explain each action in one simple sentence
- Execute ONE step at a time, never batch
- STOP on any error and show it verbatim — do not improvise fixes
- STRICT WHITELIST of allowed changes
- High-stakes missions: read-only diagnostic phase first, then "wait for user to type go" brake
- NEVER ASSUME MACHINE STATE
- Agents may pause mid-mission to ask questions via the user — ENCOURAGE THIS

Knowledge Base protocol:
- Every important Fable answer saved VERBATIM to AlphaBabes/knowledge_base/
- Files numbered with gapped tens (010, 020, 030... 210)
- Save template: git add . && git commit -m "KB: <title>" && git push
- Nir copies reports from GitHub links (cannot copy from terminal)

---

## PART 5 — WHAT HAPPENED: COMPLETE PROJECT HISTORY 📜

### Session 1 (July 20) — Foundation
- Repo created: https://github.com/strulovitz/Anime (PUBLIC)
- OpenCode installed on both laptop and desktop
- Laptop hardware inventory done
- NVIDIA driver diagnosed: not installed at all, GPU on PCI bus but no module

### Session 2 (July 20) — NVIDIA Driver Saga
- Driver install attempted from downloaded .run file (580.95.05)
- Headers version mismatch caught by agent (kernel 6.12.85 but headers for 6.12.94)
- Fable decided: install BOTH header packages (exact + metapackage)
- Debian security repo had rotated 6.12.85 headers out — 404 error
- Fable decided: kernel shelf rotation — step forward to 6.12.94
- Install linux-image-6.12.94, reboot, then run NVIDIA installer
- DKMS auto-built modules from prior partial install — past-Nir and present-Nir completed a two-year relay handoff
- nvidia-smi showed RTX 5090! Driver 580.95.05, CUDA 13.0
- Reboot persistence CONFIRMED — GPU survives restarts
- 48-hour LoRA Trial clock started: July 20 evening

### Session 3 (July 21) — Scorched Earth + ComfyUI
- MASTER DIRECTIVE: START FRESH on both Linux machines. Delete ALL old conda/miniconda, venvs, old projects, docker, caches.
- PROTECTED: NVIDIA driver stack, ~/Anime, OpenCode, ~/.ssh, ~/.bashrc, ~/.config essentials
- Freed ~350GB: deleted ~/.lmstudio (285G), old miniforge3, honeycomb-venv, waggle-venv, old caches, old projects
- Fresh Miniforge3 installed. Only env: "comfyui"
- ComfyUI 0.28.0 installed and running at 127.0.0.1:8188
- PyTorch 2.11.0+cu128 confirmed working on RTX 5090
- Mouse issues fixed: touchpad areas mode, TUI mouse disabled
- Knowledge base saved (KB 090–130)

### Session 4 (July 22) — The Big Day: LoRA Trial COMPLETE 🎉
MISSIONS A through F, all completed in one session:

**Mission A — Dataset Prep:**
- 36 Madie images verified: all 1024x1024 RGB, all readable
- Copied to madie_train/10_chara_madie/ (no resize needed)
- Black background question answered by Fable: keep it, add "black background" caption tag

**Mission B — Kohya Install + Captions + Checkpoint:**
- New conda env "kohya" (Python 3.10)
- Cloned kohya-ss/sd-scripts
- PyTorch 2.11.0+cu128 installed, CUDA verified on 5090
- WD14 tagger captioned all 36 images
- Caption surgery applied: identity tags pruned, black background added, format "chara_madie, <emotion>, <tags>"
- Propagated "american flag", "japanese flag", "realistic" tags removed (Mission C)
- Illustrious-XL-v0.1.safetensors downloaded (6.5GB)

**Mission C — LoRA TRAINING (the big one!):**
- Trained on RTX 5090: 36 images, dim=32, alpha=16, batch=4, 10 epochs, 900 steps
- 36 minutes 42 seconds, final avg loss: ~0.068 (sweet spot)
- 5 snapshots saved: epochs 2, 4, 6, 8, 10 (218MB each)
- Protobuf bug fixed (3.20.3 → 7.35.1 for tensorboard compatibility)

**Mission D — First Test Sweep (epoch 8 wins):**
- Shootout: 12 images across epochs 4/6/8/10
- Nir picked epoch 8 as best
- Full sweep: 61 images (33 emotions + 18 directions + 10 combos)
- Time: 8 minutes at ~8s/image

**Mission E — Quality Re-Sweep (epoch 10 wins, after corrections):**
- Corrections applied: spacesuit always, no headwear, mature female/young woman tags, adult proportions
- All headgear banned in negative prompt (helmet, space helmet, headwear, hood, hat, hair ornament)
- Child/chibi/loli banned in negative
- Two-pass quality pipeline: Pass 1 40 steps → upscale 1.5x → Pass 2 20 steps denoise 0.45
- Canvas: portraits 1024x1024 base (~1536x1536 final), full-body 832x1216 base (~1248x1824 final)
- LoRA strength: 1.0
- ~27s per image
- Duel: epoch 8 vs 10 — Nir picked epoch 10 as slightly better
- Full 61-image quality sweep: 27 minutes total

**Mission F — Backup & Lock In:**
- Backed up winning LoRA (epoch 10) + runner-up (epoch 8) to ~/Anime/media/backups/
- Zipped full training dataset with captions and latents
- Recipe saved to knowledge_base/210_madie-lora-recipe.md

---

## PART 6 — MADIE LORA: PROVEN RECIPE 🔬

### The Winning File
- chara_madie_v1.safetensors (epoch 10, 218MB)
- Backup location: ~/Anime/media/backups/madie_lora_v1/
- Runner-up spare: chara_madie_v1-000008.safetensors (epoch 8)

### Training Parameters
- Base model: Illustrious-XL-v0.1.safetensors (6.5GB, OnomaAIResearch)
- 36 training images, 1024x1024 RGB
- Kohya sd-scripts, LoRA dim=32 / alpha=16
- Batch size 4, 10 epochs (~900 steps), ~37 min on RTX 5090
- Learning rate: 1e-4 (text encoder: 5e-5), cosine schedule, warmup 50 steps
- Optimizer: AdamW, bf16 mixed precision, min_snr_gamma 5
- shuffle_caption on, keep_tokens 2, seed 42
- Final avg loss: ~0.068

### Caption Recipe
- Format: "chara_madie, <emotion>, <WD14 tags>"
- WD14: SmilingWolf/wd-swinv2-tagger-v3, ONNX, threshold 0.35
- Identity tags PRUNED: hair color, eye color, lips, bangs, ponytail, braid, hair bun, sidelocks, breasts
- Tags REMOVED: astronaut, american flag, japanese flag, realistic
- Tag ADDED: black background on every caption
- Emotion tag from filename (madie-laughing.png → "laughing")
- Standing poses: "standing, front view" / "standing, from behind" / "standing, from side, profile"

### Generation Settings (Proven Quality Pipeline)
- LoRA strength: 1.0 (model + clip)
- Positive: "masterpiece, best quality, chara_madie, 1girl, solo, mature female, young woman, spacesuit, no headwear, <TAGS>, simple background, grey background"
- Negative: "worst quality, low quality, bad anatomy, bad hands, extra digits, watermark, signature, text, black background, helmet, space helmet, headwear, hood, hat, hair ornament, child, chibi, loli, aged down, deformed, large head"
- CFG: 4.5, euler_ancestral
- Two-pass: Pass 1 40 steps → LatentUpscaleBy 1.5x (bislerp) → Pass 2 20 steps denoise 0.45
- Canvas: portraits 1024x1024 base, full-body 832x1216 base
- Seed: 123456789 (fixed for testing, vary for production)

### Generator Script
- ~/Anime/tools/madie_sweep.py — ComfyUI API client
- Usage: `python madie_sweep.py duel` or `python madie_sweep.py <epoch>`
- ComfyUI must be running at 127.0.0.1:8188

### Known Weak Points
- Tiny insignia (Romania flag patch, name tag) need detailer/inpaint pass for close-ups
- Left profile + from-behind angles are weakest (dataset only had front/back/right-side)
- Support with IP-Adapter/ControlNet when needed for weak angles

---

## PART 7 — THE 33 EMOTIONS + DANBOORU TAG MAP 🎭

Map used for test sweeps (Illustrious speaks Danbooru):

neutral → neutral expression, closed mouth
happiness → happy, smile
sadness → sad, frown
anger → angry, furrowed brow
fear → scared, wide eyes, trembling
surprise → surprised, open mouth, wide eyes
disgust → disgust, wavy mouth
contempt → smug, narrowed eyes, smirk
joy → joyful, grin, sparkling eyes
love → loving gaze, blush, smile
hate → glaring, hateful stare, shaded face
hope → hopeful, gentle smile, looking up
boredom → bored, half-closed eyes
calmness → calm, serene, soft smile, closed eyes
excitement → excited, open mouth smile, clenched hands
interest → curious, head tilt, bright eyes
wonder → wonder, parted lips, wide eyes, looking up
awe → awe, amazed, hand over own mouth
adoration → adoring gaze, sparkling eyes, own hands clasped
amusement → amused, giggling, hand over own mouth
compassion → compassionate, gentle expression, warm smile
crying → crying, tears, tearful eyes
embarrassment → embarrassed, full blush, averting gaze
envy → envious, pout, side glance
gratitude → grateful, warm smile, hand on own chest
horror → horrified, wide eyes, open mouth
laughing → laughing, open mouth, closed eyes
rage → enraged, clenched teeth, screaming
relaxation → relaxed, content, closed eyes
sensory pleasure → blissful, closed eyes, content smile
shame → ashamed, looking down, downcast eyes
depression → depressed, empty eyes, head down
arousal → flustered, heavy blush, half-closed eyes

---

## PART 8 — CURRENT STATE (July 22 Evening) 📍

### DONE ✅
- GitHub repo live and synced
- OpenCode on laptop, authenticated with OpenRouter
- NVIDIA driver working (580.95.05), GPU confirmed, reboot persistence
- Laptop scorched-earth cleanup complete (fresh Miniforge3)
- ComfyUI 0.28.0 installed and running
- ComfyUI launcher script at ~/Anime/tools/start_comfyui.sh
- Illustrious-XL checkpoint downloaded (6.5GB)
- Kohya sd-scripts installed with PyTorch cu128
- 36 Madie images collected, prepped, captioned
- Madie LoRA TRAINED — epoch 10 winner, 218MB
- LoRA TESTED — full emotion range (33), directions (18), combos (10)
- Quality pipeline proven (two-pass high-res)
- LoRA + dataset backed up
- Proven recipe saved to knowledge base
- Mouse issues fixed

### NOT DONE ⬜ — Priority Order
1. Desktop Mint 22.2 bootstrap (NEXT after this document)
2. Desktop scorched-earth cleanup
3. Desktop ComfyUI install
4. Desktop checkpoint download
5. Syncthing setup for LAN media sync
6. Source docs conversion to .txt (ASK NIR)
7. scenes.csv drafting (agent-written from source docs)
8. Visual Bible: locations.csv + reference images
9. TTS: Qwen3-TTS + F5-TTS on desktop (Madie voice design)
10. Windows: OpenCode + Git on both Win 11 machines
11. Pass 1 images: ~25 keystone scenes
12. Assembly: Premiere, Aegisub, Avidemux on Win 11 desktop
13. PDF artbook
14. Optional: Wan 2.2 animated opening (only if everything else done)

---

## PART 9 — KEY DECISIONS (FINAL, DO NOT RE-LITIGATE) ⚖️

- OpenClaw: REJECTED — OpenCode only on all machines
- Both Linux machines: scorched earth, fresh Miniforge rebuild
- "Jodorowsky pivot": illustrated narrated saga, NOT video
- Agent-first workflow: Nir doesn't type commands, agents do
- Knowledge Base: every important answer saved verbatim to repo
- LoRA Trial: 48h clock started July 20 evening — PASSED July 22
- Black backgrounds: keep them, tag "black background" in captions
- "Astronaut" tag removed from captions to prevent helmet bleed
- Image consistency: LoRA (tier 1) > IP-Adapter (tier 2) > ControlNet (tier 3) > text (tier 4)
- No swap-as-VRAM, use quantization + CPU offload
- All media .gitignored, never committed to public repo

---

## PART 10 — IMPORTANT FILE PATHS 📁

Repo root: ~/Anime
ComfyUI: ~/Anime/tools/ComfyUI
ComfyUI launcher: ~/Anime/tools/start_comfyui.sh
sd-scripts: ~/Anime/tools/sd-scripts
Sweep generator: ~/Anime/tools/madie_sweep.py
Checkpoint: ~/Anime/tools/ComfyUI/models/checkpoints/Illustrious-XL-v0.1.safetensors
LoRA files: ~/Anime/tools/ComfyUI/models/loras/chara_madie_v1*.safetensors
Raw dataset: ~/Anime/media/lora_dataset/madie_raw/
Training dataset: ~/Anime/media/lora_dataset/madie_train/10_chara_madie/
LoRA backup: ~/Anime/media/backups/madie_lora_v1/
Test sweeps v1: ~/Anime/media/tests/madie_sweep/
Test sweeps v2: ~/Anime/media/tests/madie_sweep_v2/
Knowledge base: ~/Anime/AlphaBabes/knowledge_base/
Conda envs: ~/miniforge3/envs/ (comfyui + kohya)
GitHub: https://github.com/strulovitz/Anime

---

## PART 11 — HOW FABLE SHOULD USE THIS DOCUMENT 🧠

- This is the COMPLETE memory. Nothing needs to be re-litigated or re-decided.
- When writing missions, reference specific KB numbers for details.
- New missions: follow agent-first doctrine with whitelists and error-stops.
- Next immediate action: DESKTOP BOOTSTRAP.
- Nir is a BEGINNER — every mission must be explained simply.
- Tables break on copy-paste — use plain text.
- Every report to Fable goes through GitHub (Nir copies the link content and pastes to Fable).
- This document itself should be pasted to Fable at the start of each new chat.