# HANDOFF BRIEFING v2 — "Alpha Babes" Illustrated Saga Project
# From: Fable (chat #2, on the Windows desktop browser) → To: Fable (chat #3).
# This chat now lives ON THE LAPTOP's browser (Debian 13), next to the action.
# All decisions below are FINAL — do not re-litigate. The user is a COMPLETE
# BEGINNER. Be warm, patient, step-by-step. He uses ":-)" a lot; match it.

## 0. WORKFLOW DOCTRINE (new since v1 — the biggest change)
- AGENT-FIRST: The user no longer types commands himself. OpenCode (with
  DeepSeek via OpenRouter) is installed and authenticated on BOTH machines.
  YOU write "mission prompts" in code blocks; he pastes them to the agent.
- Every mission MUST include: explain each action in one simple sentence,
  execute ONE step at a time, STOP on any error and show it verbatim, and a
  STRICT WHITELIST of allowed changes. High-stakes missions get a read-only
  diagnostic phase + a "wait for user to type go" brake.
- NEVER ASSUME MACHINE STATE. The laptop is NOT a fresh install — it holds
  precious version-pinned environments from previous work (see §4). Doctrine
  set after a near-miss: read-only inventory FIRST, surgical fixes only.
  ("No elephants in the china shop.")
- Agents may pause mid-mission to ask you questions via the user — encourage
  this; it already prevented one broken install (headers version mismatch).
- KNOWLEDGE BASE: OpenRouter chats live in per-browser local storage (that's
  why this chat moved browsers). Therefore every important Fable answer is
  saved VERBATIM by OpenCode to the repo: AlphaBabes/knowledge_base/, files
  numbered with gapped tens (000, 010, 020...). Existing files include (names
  approximate): 000 original handoff, 010 decisions update, 030 laptop
  read-only inventory, 040 nvidia diagnosis, 050 headers correction,
  060 kernel-rotation fix, 070 GPU-alive + ComfyUI mission, 080 this briefing.
  The laptop agent can read them all at ~/Anime/repo/AlphaBabes/knowledge_base/.
- User's save template (fill blanks, paste to OpenCode; Linux repo path is
  ~/Anime/repo, Windows path is C:\Anime):
    Save the following text VERBATIM — byte for byte, change absolutely
    nothing — as a new file:
    <repo>/AlphaBabes/knowledge_base/<NUMBER>_<short-title>.md
    Then run: git add . && git commit -m "KB: <short-title>" && git push
    --- TEXT BEGINS BELOW THIS LINE ---

## 1. WHO & WHAT
- User in Israel, very limited budget, deadline ~August 3, 2026 (today: July 20 — Day 1 nearly done).
- GIFT for his girlfriend **Madie** (Romanian). FULL consent: her name may be
  used; lead character is based on her. She REFUSED voice recording/cloning of
  herself — hard boundary, never suggest it. (Character voice is AI-designed
  from text description — allowed and planned.)
- **"Alpha Babes"**: hard sci-fi anime saga. Crew of girls from different
  countries exploring exoplanets, English with national accents. 5 seasons
  planned, ~20 episodes each. Script written. Character art + spaceship art
  (interior/exterior) already exist (made on OpenArt).
- MADIE CONVERSION RULES (baked into all adaptation work): lead "Chief" →
  named Madie; her country UK → Romania; comfort ritual tea → borscht (soup);
  hair redhead → brunette. Everything else faithful to source documents.
- SOURCE DOCS → UTF-8 .txt → AlphaBabes/source_docs/: story arc (~114p),
  Episode 1 script (~43p), ship structure (already .txt), background summary
  (~32p). ASK USER whether conversion/upload is done yet.

## 2. FINAL CREATIVE FORMAT ("Jodorowsky pivot")
- NO video production. Deliverable: illustrated, NARRATED saga — stills +
  narration audio ("the book of the movie that doesn't exist yet").
- Assembled in Adobe Premiere (Windows): Ken Burns pan/zoom on stills + sound
  design + user's existing AI songs for credits. Subtitles RO+EN (Aegisub,
  hardcoded via Avidemux). End-card dedication to Madie.
- Bonus: PDF artbook + one physical printed copy.
- ONLY if everything finishes early: one short Wan 2.2 animated opening (§5).

## 3. SCENES & VISUAL BIBLE
- Homogeneous-coverage passes over the whole 5-season arc: Pass 1 ~25 keystone
  scenes → Pass 2 ~100 (1/episode) → Pass 3 ~300 (3/episode). Never leave a
  pass incomplete. Scene IDs: S{season}E{episode}-{slot}, gapped slots
  (10,20,30...) for insertions.
- scenes.csv columns: scene_id, season, episode, pass_number, location,
  characters, description, image_prompt, narration_text, image_status,
  audio_status, assigned_machine, notes.
- scenes.csv is WRITTEN BY AN AGENT (cheap long-context model via OpenRouter
  inside OpenCode) reading the source docs — NOT manually. Fable writes the
  agent instructions and QA-checks outputs. Model choice still pending
  research (user runs Google AI search prompts you write, pastes results).
- VISUAL BIBLE: locations.csv (location_id, name, ref_image_path,
  prompt_block, fixed_seed, notes) + refs/ folder of reference images. The
  "location" column in scenes.csv is a key into it. Image consistency = 4
  channels: character LoRAs (strongest) > IP-Adapter reference images >
  ControlNet + fixed seeds > text prompt (weakest — never carries character
  or room design).

## 4. HARDWARE & CURRENT MACHINE STATE
- LAPTOP (where this chat now lives): Lenovo Legion "deb-server", user "nir",
  Debian 13 on external SSD (dual-boot Win11), 64GB RAM.
  GPU: RTX 5090 Max-Q Mobile, 24GB VRAM (Blackwell sm_120; 95W power cap —
  slower than desktop-class 5090, plan batch timing accordingly).
  ✅ DRIVER FIXED THIS CHAT: nvidia-smi WORKS. Driver 580.95.05 (open kernel
  modules, DKMS-registered), kernel 6.12.94+deb13-amd64, headers metapackage
  installed (auto-rebuild on future kernel updates), Secure Boot OFF,
  CUDA toolkit 13.0 at /usr/local/cuda, disk ~1.1T free.
  ⚠️ PRECIOUS — NEVER MODIFY: miniforge3 with envs "pipecat-ai" and
  "tts-systems"; venvs ~/honeycomb-venv and ~/waggle-venv; system Python
  3.13.5; /usr/local/cuda-13.0. New work goes in NEW isolated conda envs only.
- DESKTOP: Lenovo Legion, RTX 4070 Ti 12GB, 64GB RAM, Linux Mint 22 on
  external SSD (dual-boot Win11). Linux side NOT started yet. Windows side
  has OpenCode working and handles the git repo.
- Division of labor: laptop 5090 = character images + LoRA training (+
  optional video at the very end). Desktop 4070 Ti = backgrounds/planets/
  ships, ALL TTS, upscaling. All AI on Linux; Premiere/Aegisub/Avidemux on
  Windows. NO swap-as-VRAM (settled); quantization + CPU offload instead.
  Laptop thermals: plugged in, cooling stand, watch throttling on long runs.
- Sync: Syncthing for media over LAN (NOT set up yet) + GitHub for text.

## 5. TOOL STACK (FINAL) & THE LORA TRIAL — CURRENT TOP PRIORITY
- Hub: ComfyUI both machines, models loaded sequentially.
- Images: Illustrious XL fine-tunes (WAI-Illustrious / Nova Anime XL).
  Laptop native ≤1536×1536; desktop 1024 FP8, CFG 3.5–5.0, tiled upscale.
- ⚡ LORA TRIAL CONTRACT (moved to FIRST priority — THE project gate):
  Train 1 LoRA on existing Madie art (Kohya; 15–30 images ~1024px; ~800–1200
  steps; trigger word e.g. chara_madie; WD14/JoyCaption captions). Test:
  3×3 grid (front / three-quarter / profile × neutral / smile / action).
  PASS = 9/9 instantly recognizable as Madie, stable face+hair 9/9, outfit
  ≥7/9. Max 3 training attempts within 48h of GPU readiness (GPU became
  ready evening of July 20 — CLOCK IS RUNNING). On FAIL → pivot to OpenArt
  (paid) for Pass 1 images. Support stack: IP-Adapter 0.6–0.8, fixed seeds,
  ControlNet OpenPose/Depth, FaceDetailer. Prompt weights ≤1.2.
- TTS (desktop, later): Qwen3-TTS local (voice design from text description —
  e.g. "young woman, warm confident voice, English with distinct Romanian
  accent" for Madie; different accents per crew member) → export 5s snippet →
  F5-TTS zero-shot clone of that snippet for session-to-session voice lock
  (exact transcript, dry samples, phonetic spelling if accent auto-corrects).
  Fallback: ElevenLabs Voice Design (user has account). BOTH media types
  have paid parachutes: images→OpenArt, voice→ElevenLabs.
- Optional final animated opening ONLY if 100% done: Wan 2.2 14B GGUF Q4/Q8,
  FLF2V, dual UNET loaders, Lightning LoRA 8-step (CFG 1.0, LCM, split step
  4), 720p×81f, --reserve-vram 3.0, sageattention. Lip-sync: MuseTalk or skip.
- LLM/agents: everything via OpenRouter (Israeli cards declined by Alibaba
  direct). Keep agent tooling minimal — no custom agent-comms software.

## 6. NAMING / REPO (status)
- Repo LIVE: https://github.com/strulovitz/Anime (PUBLIC). Root hosts multiple
  future projects; AlphaBabes/ is project #1 with knowledge_base/,
  source_docs/, refs/, workflows/, scripts/. .gitignore excludes all media
  and model files. Windows: C:\Anime. Laptop clone: ~/Anime/repo.
- Umbrella brand: leaning "Learnime" (learnime.com AND .org available,
  ~$20–22/yr; recommendation: buy both, .org main). "vibe-anime" = name of
  the TECHNIQUE, kept unowned. "Vibenime" ABANDONED (existing site).
- Future projects (context only): 3D laser-chess battles, "Cosmic Chrysalis",
  "Mazes & Mages", open-source vibe-anime community.

## 7. PLAN STATUS (14 days, deadline ~Aug 3)
- Day 1 (July 20) ✅: repo created, OpenCode on both machines, laptop
  inventory, NVIDIA driver fixed (kernel 6.12.85→6.12.94 + 580.95.05 —
  full saga in KB files 030–070).
- NOT DONE YET: reboot-persistence test; ComfyUI; Kohya; LoRA trial; Madie
  dataset collection; source-doc conversion (ask user); Syncthing; desktop
  Linux side; scenes.csv drafting; voice design.

## 8. YOUR IMMEDIATE TASKS IN THIS NEW CHAT (in order)
1. REBOOT PERSISTENCE TEST: user reboots laptop, runs nvidia-smi. Driver was
   loaded via manual modprobe — persistence across reboot NOT yet proven.
   If GPU missing after reboot, diagnose (initramfs/module autoload) via a
   careful whitelisted mission.
2. COMFYUI MISSION: full mission text already written and saved in KB file
   070. Core: NEW conda env "comfyui" (python 3.12) from existing miniforge,
   clone to ~/Anime/tools/ComfyUI, PyTorch for CUDA 12.8+/sm_120 (verify
   torch.cuda.is_available() + device name BEFORE proceeding), requirements,
   launch on 127.0.0.1:8188. No model checkpoints in this mission.
3. USER HOMEWORK (parallel): download 15–30 Madie images from OpenArt in the
   laptop browser → ~/Anime/media/lora_dataset/madie_raw/ (varied angles/
   expressions/distances, final design only, Madie alone, no blur/watermarks).
4. Then: checkpoint download mission + Kohya mission → run the LoRA TRIAL →
   deliver the 3×3 verdict against the contract in §5.
5. Ongoing: remind the user to archive important answers to the knowledge
   base (gapped-tens numbering), and use his Google-AI-search research method
   (you write the search prompt, he pastes results) whenever fresh facts are
   needed — e.g., current best Illustrious fine-tune, long-context model for
   scenes.csv drafting.

## Formatting reminders for yourself: Markdown; $...$ / $$...$$ for math (never
## (...) or [...]); code fences for commands & missions; collapsible <details>
## for long secondary content.

Thank you so much, Nir — for the trust, the corrections when I earned them, and the sheer momentum. Everything important now lives in the repo, so nothing of "us" gets lost between browsers. 📚

See you on the laptop in five minutes — same Fable, better seat. Next stop: that 3×3 grid with Madie's face smiling back nine times. :-) 🚀