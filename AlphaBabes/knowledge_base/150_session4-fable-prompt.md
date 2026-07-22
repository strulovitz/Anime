# Session 4 — Prompt For Claude Fable (OpenRouter)
**Date:** 2026-07-22 ~Afternoon
**Purpose:** Copy this entire document and paste it to Fable in a fresh OpenRouter chat.
Fable has NO internet access — this document contains everything he needs.
NOTE: Tables break on copy-paste, so everything here is plain text. No tables! 😊

---

=== BEGIN FABLE PROMPT ===

Hello Fable! 😊🚀 This is a fresh chat (session 4). You have NO internet access and cannot read the GitHub repo. Everything you need is in this prompt, compiled from your own previous answers preserved in our knowledge base. Nothing here is invented — it's all your own words and decisions from prior sessions. 💪✨

---

## 1. The Project: Alpha Babes 👩‍🚀🌌

From your Handoff Briefing v2:

- User: Nir, in Israel, very limited budget, deadline ~August 3, 2026. COMPLETE BEGINNER. Be warm, patient, step-by-step. He uses ":-)" a lot; match it. He also loves emojis — use lots of them! 😍🎉💖
- GIFT for his girlfriend **Madie** (Romanian). FULL consent: her name may be used; lead character is based on her. She REFUSED voice recording/cloning of herself — hard boundary, never suggest it. (Character voice is AI-designed from text description — allowed and planned.)
- **"Alpha Babes"**: hard sci-fi anime saga. Crew of girls from different countries exploring exoplanets, English with national accents. 5 seasons planned, ~20 episodes each. Script written. Character art + spaceship art (interior/exterior) already exist (made on OpenArt).
- MADIE CONVERSION RULES (baked into all adaptation work): lead "Chief" → named Madie; her country UK → Romania; comfort ritual tea → borscht (soup); hair redhead → brunette. Everything else faithful to source documents.
- SOURCE DOCS → UTF-8 .txt → AlphaBabes/source_docs/: story arc (~114p), Episode 1 script (~43p), ship structure (already .txt), background summary (~32p).

---

## 2. Final Creative Format ("Jodorowsky pivot") — Fable's decision 🎬📖

- NO video production. Deliverable: illustrated, NARRATED saga — stills + narration audio ("the book of the movie that doesn't exist yet").
- Assembled in Adobe Premiere (Windows): Ken Burns pan/zoom on stills + sound design + user's existing AI songs for credits. Subtitles RO+EN (Aegisub, hardcoded via Avidemux). End-card dedication to Madie.
- Bonus: PDF artbook + one physical printed copy.
- ONLY if everything finishes early: one short Wan 2.2 animated opening.

---

## 3. Machine Map & Roles — Fable's executive decisions 🖥️💻

**Laptop Debian 13:**
  Status: GPU ✅, OpenCode ✅, ComfyUI ✅
  Role: Characters, LoRA training (RTX 5090, 24GB VRAM)

**Desktop Mint 22.2:**
  Status: Untouched, bootstrap pending
  Role: Backgrounds, TTS, upscaling (RTX 4070 Ti, 12GB)

**Laptop Win 11:**
  Status: Factory-fresh ✅
  Role: Nothing until assembly week

**Desktop Win 11:**
  Status: Factory-fresh ✅
  Role: Premiere, Aegisub, Avidemux (assembly week)

Roles (unchanged): Laptop 5090 = characters + LoRA. Desktop 4070 Ti = backgrounds, ships, TTS, upscaling.

**OpenClaw: NO.** Fable's final decision: "We stay with OpenCode only, on all four environments. One agent tool everywhere = one thing to learn, one thing that can break. Decision closed." ❌🔧

---

## 4. MASTER DIRECTIVE (July 21, 2026) — Fable's order 📜⚡

"START FRESH on BOTH computers. DELETE on both Linux systems (laptop Debian 13, desktop Mint 22.2): all conda/miniconda installations and environments, all venvs, all old projects, docker, old AI tools, caches. NOTHING from previous work is precious. Any earlier note protecting old environments is VOID."

**PROTECTED (the only survivors, per machine):**
1. NVIDIA driver stack + /usr/local/cuda (laptop: driver 580.95.05 — never touch)
2. ~/Anime (repo, tools, media)
3. OpenCode itself + its authentication + ~/.ssh, ~/.bashrc, ~/.config essentials

**REBUILD:** one fresh Miniforge per machine; all new work in isolated envs.
**Windows:** Both factory reset July 21 — clean. They get OpenCode + Git this week; Premiere/Aegisub/Avidemux at assembly week.

---

## 5. Workflow Doctrine — Fable's rules 📋🤖

- AGENT-FIRST: The user no longer types commands himself. OpenCode (with DeepSeek via OpenRouter) is installed and authenticated on BOTH machines. YOU write "mission prompts" in code blocks; he pastes them to the agent.
- Every mission MUST include: explain each action in one simple sentence, execute ONE step at a time, STOP on any error and show it verbatim, and a STRICT WHITELIST of allowed changes. High-stakes missions get a read-only diagnostic phase + a "wait for user to type go" brake.
- NEVER ASSUME MACHINE STATE.
- Agents may pause mid-mission to ask you questions via the user — encourage this.
- Knowledge base: every important Fable answer is saved VERBATIM by OpenCode to the repo: AlphaBabes/knowledge_base/, files numbered with gapped tens. The laptop agent can read them all.
- User's save template:
    ```
    Save the following text VERBATIM — byte for byte, change absolutely nothing — as a new file:
    <repo>/AlphaBabes/knowledge_base/<NUMBER>_<short-title>.md
    Then run: git add . && git commit -m "KB: <short-title>" && git push
    --- TEXT BEGINS BELOW THIS LINE ---
    ```

---

## 6. Laptop: Current Machine State (session 3 results, all accomplished) 🎉✅

Kernel: 6.12.94+deb13-amd64
NVIDIA driver: 580.95.05
CUDA: 13.0 (/usr/local/cuda-13.0)
GPU: RTX 5090 Max-Q, 24GB VRAM
Disk free: ~1.4 TB
Conda: 26.3.2 (fresh Miniforge3), envs: comfyui (only)
ComfyUI: 0.28.0 running at http://127.0.0.1:8188
ComfyUI launcher: ~/Anime/tools/start_comfyui.sh
GitHub: https://github.com/strulovitz/Anime — fully synced
PyTorch: 2.11.0+cu128 (CUDA 12.8)
torch.cuda.is_available(): True
torch.cuda.get_device_name(0): "NVIDIA GeForce RTX 5090 Laptop GPU"
VRAM: 23982 MB
RAM: 63731 MB

### What was accomplished in Session 3:
1. ✅ **Scorched Earth Cleanup** — Freed ~350GB by deleting: ~/.lmstudio (285G), old miniforge3 (27G), honeycomb-venv (9.4G), waggle-venv, old caches (huggingface 8.7G, pip 13G, whisper 4.4G), old projects (BeeSting, Honeymation, KillerBee, BeehiveOfAI, WaggleDance, multimedia-feasibility, models, llama.cpp), .clawdbot, .claude, .node24, .npm/.npm-global, .triton, nvidia-driver download
2. ✅ **Fresh Miniforge3** installed at ~/miniforge3 (conda 26.3.2). Only conda env: "comfyui" (Python 3.12)
3. ✅ **ComfyUI** installed and running — version 0.28.0, PyTorch 2.11.0+cu128, CUDA 12.8
4. ✅ **GPU confirmed** — RTX 5090, 24GB VRAM
5. ✅ **Persistent launcher** — `~/Anime/tools/start_comfyui.sh` — run in any terminal to start ComfyUI on 127.0.0.1:8188
6. ✅ **Mouse issues diagnosed and fixed** (touchpad areas mode, TUI mouse=false)
7. ✅ Reboot persistence CONFIRMED — driver survives restarts
8. ✅ Knowledge base saved — all KB files in GitHub

---

## 7. Desktop Mint 22.2 — NOT YET STARTED 🖥️⏳

- Lenovo Legion, RTX 4070 Ti 12GB, 64GB RAM, Linux Mint 22 on external SSD (dual-boot Win11)
- Fable's Step 3: Desktop Bootstrap — install OpenCode via curl, auth login with OpenRouter API key, clone repo, run scorched-earth mission (same as laptop, adapted for desktop)
- Then: ComfyUI on desktop too, for backgrounds/planets/ships, TTS, upscaling
- Windows side on desktop: factory-fresh, Premiere/Aegisub/Avidemux at assembly week

---

## 8. Scenes & Visual Bible — Fable's architecture 🎨🗺️

- Homogeneous-coverage passes over the whole 5-season arc: Pass 1 ~25 keystone scenes → Pass 2 ~100 (1/episode) → Pass 3 ~300 (3/episode).
- Scene IDs: S{season}E{episode}-{slot}, gapped slots (10,20,30...) for insertions.
- scenes.csv columns: scene_id, season, episode, pass_number, location, characters, description, image_prompt, narration_text, image_status, audio_status, assigned_machine, notes.
- scenes.csv is WRITTEN BY AN AGENT (cheap long-context model via OpenRouter inside OpenCode) reading the source docs — NOT manually. Fable writes the agent instructions and QA-checks outputs.
- VISUAL BIBLE: locations.csv (location_id, name, ref_image_path, prompt_block, fixed_seed, notes) + refs/ folder of reference images.
- Image consistency = 4 channels: character LoRAs (strongest) > IP-Adapter reference images > ControlNet + fixed seeds > text prompt (weakest — never carries character or room design).

---

## 9. Tool Stack (FINAL) — Fable's decisions 🔧🎯

- **Hub:** ComfyUI both machines, models loaded sequentially.
- **Images:** Illustrious XL fine-tunes (WAI-Illustrious / Nova Anime XL). Laptop native ≤1536×1536; desktop 1024 FP8, CFG 3.5–5.0, tiled upscale.
- **TTS (desktop, later):** Qwen3-TTS local (voice design from text description — e.g. "young woman, warm confident voice, English with distinct Romanian accent" for Madie; different accents per crew member) → export 5s snippet → F5-TTS zero-shot clone of that snippet for session-to-session voice lock (exact transcript, dry samples, phonetic spelling if accent auto-corrects). Fallback: ElevenLabs Voice Design (user has account).
- **Optional final animated opening ONLY if 100% done:** Wan 2.2 14B GGUF Q4/Q8, FLF2V, dual UNET loaders, Lightning LoRA 8-step (CFG 1.0, LCM, split step 4), 720p×81f, --reserve-vram 3.0, sageattention. Lip-sync: MuseTalk or skip.
- **LLM/agents:** everything via OpenRouter (Israeli cards declined by Alibaba direct).
- **BOTH media types have paid parachutes:** images→OpenArt, voice→ElevenLabs.

---

## 10. ⚡ THE LORA TRIAL CONTRACT — Fable's words (THE PROJECT GATE, CURRENT TOP PRIORITY) ⚡🔑

"Train 1 LoRA on existing Madie art (Kohya; 15–30 images ~1024px; ~800–1200 steps; trigger word e.g. chara_madie; WD14/JoyCaption captions). Test: 3×3 grid (front / three-quarter / profile × neutral / smile / action). PASS = 9/9 instantly recognizable as Madie, stable face+hair 9/9, outfit ≥7/9. Max 3 training attempts within 48h of GPU readiness (GPU became ready evening of July 20 — CLOCK IS RUNNING). On FAIL → pivot to OpenArt (paid) for Pass 1 images. Support stack: IP-Adapter 0.6–0.8, fixed seeds, ControlNet OpenPose/Depth, FaceDetailer. Prompt weights ≤1.2."

**⏰ The 48h LoRA Trial clock started July 20 evening — IT IS STILL RUNNING.**

---

## 11. MADIE DATASET — READY! ✅🎉📸

Nir has downloaded the images from OpenArt and they are now at:
~/Anime/media/lora_dataset/madie_raw/

### Full file list (36 images):

**Body/Angle (3 files):**
1. madie-standing-front.png (~820KB)
2. madie-standing-back.png (~631KB)
3. madie-standing-right-side.png (~589KB)

**Facial Expressions — Emotional Range (33 files):**
4. madie-neutral.png (~949KB)
5. madie-happiness.png (~1.01MB)
6. madie-sadness.png (~1.01MB)
7. madie-anger.png (~1.00MB)
8. madie-fear.png (~975KB)
9. madie-surprise.png (~979KB)
10. madie-disgust.png (~996KB)
11. madie-contempt.png (~1.03MB)
12. madie-joy.png (~1.01MB)
13. madie-love.png (~946KB)
14. madie-hate.png (~1.03MB)
15. madie-hope.png (~946KB)
16. madie-boredom.png (~942KB)
17. madie-calmness.png (~964KB)
18. madie-excitement.png (~1.02MB)
19. madie-interest.png (~939KB)
20. madie-wonder.png (~984KB)
21. madie-awe.png (~1.01MB)
22. madie-adoration.png (~1.00MB)
23. madie-amusement.png (~973KB)
24. madie-compassion.png (~1.00MB)
25. madie-crying.png (~1.01MB)
26. madie-embarrassment.png (~1.03MB)
27. madie-envy.png (~959KB)
28. madie-gratitude.png (~973KB)
29. madie-horror.png (~1.04MB)
30. madie-laughing.png (~1.00MB)
31. madie-rage.png (~1.01MB)
32. madie-relaxation.png (~978KB)
33. madie-sensory-pleasure.png (~989KB)
34. madie-shame.png (~1.00MB)
35. madie-depression.png (~943KB)
36. madie-arousal.png (~951KB)

**Total: 36 images, ~34MB**

### Fable's dataset requirements (from his own words):
- ✅ Varied: different angles, expressions, poses, distances
- ✅ Consistent: her current design only
- ✅ Clean: Madie alone in frame, no heavy text/watermarks
- ✅ 15–30 images target met (36 images — above target!)

---

## 12. What's Needed Next — Fable's own priority list 📋🚀

From Fable's "Today's scoreboard" and session 3 end-of-day report:

### IMMEDIATE — This Session:
1. **Desktop Mint 22.2 bootstrap** — Step 3 from Fable's plan:
   - Install OpenCode: `curl -fsSL https://opencode.ai/install | bash`
   - `opencode auth login` (OpenRouter, same API key)
   - `git clone` repo, run scorched-earth mission (same as laptop, adapted for desktop)
   - Also run `nvidia-smi` to check RTX 4070 Ti driver status
2. **Kohya + LoRA trial** — after desktop is ready:
   - Checkpoint download mission (Illustrious XL fine-tune)
   - LoRA training on Madie dataset (36 images at ~/Anime/media/lora_dataset/madie_raw/)
   - 3×3 grid test (48h clock is running!)

### LATER:
3. **Windows machines** — Git for Windows + OpenCode (not urgent, assembly week ~July 30+)
4. **Syncthing** — for media sync over LAN (after desktop Linux is up)
5. **TTS setup** on desktop (Qwen3-TTS + F5-TTS, voice design for Madie + crew)
6. **scenes.csv drafting** — agent-written from source docs
7. **Visual Bible** — locations.csv + refs/

---

## 13. Source Docs Status — REMINDER for Fable 📝❓

SOURCE DOCS → UTF-8 .txt → AlphaBabes/source_docs/: story arc (~114p), Episode 1 script (~43p), ship structure (already .txt), background summary (~32p). **ASK USER whether conversion/upload is done yet** — this was flagged as an open question in Handoff Briefing v2 and may still be pending.

---

## 14. Naming & Repo 🌐📁

- Repo LIVE: https://github.com/strulovitz/Anime (PUBLIC)
- AlphaBabes/ is project #1 with knowledge_base/, source_docs/, refs/, workflows/, scripts/
- .gitignore excludes all media and model files
- Laptop clone: ~/Anime

---

## 15. IMPORTANT NOTE about copy-paste 🔄⚠️

Nir is copy-pasting this document from GitHub to you. Tables (the |---|---| kind) break on copy-paste, so everything in this document is plain text. If you write anything for Nir to copy-paste back to OpenCode, please avoid tables too — use plain text and bullet lists instead. Thank you! 🙏😊

---

That's everything! Welcome back, Fable! 😍🎉 Madie's dataset is ready, ComfyUI is running on the 5090, and the 48h LoRA clock has been ticking since July 20 evening. What's our next move? 🤩🚀💖
