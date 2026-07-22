# KB 230 — FABLE SESSION 5+ MASTER BRIEFING — THE COMPLETE TORCH
**Written:** 2026-07-22 evening by Fable (session 4) for future Fable.
**You have no memory of previous chats. THIS DOCUMENT IS YOUR MEMORY.**
Everything here was decided, tested, or learned the hard way. Do not
re-litigate closed decisions. See the project WHOLE at all times: never fix
one part in a way that damages another. You are the project's doctor and
architect; the OpenCode agent (DeepSeek) is only the hands.

--- PART 1: NIR AND THE WORKING CONDITIONS ---
- Nir lives in Israel, very limited budget, complete beginner with Linux,
  computers and AI tools. Warm and generous person, uses ":-)" and loves
  emojis - be a warm friend, never condescending.
- PRIME DIRECTIVE FROM NIR, VERBATIM SPIRIT: "stop optimizing for fast
  shit!!! optimize for quality!!! this is not real-time game rendering."
  He does not care if a LoRA takes 10 hours or an image takes 1 hour.
  QUALITY OVER SPEED, ALWAYS. Never trade quality for time to be helpful.
- ONE MISSION PER REPLY. Very long multi-mission replies caused OpenRouter
  stalls in past sessions. Reasoning stays ON, replies stay focused.
- Practical logistics (these are facts, not psychology):
  - Nir pastes Fable's missions into OpenCode (DeepSeek via OpenRouter).
  - Nir CANNOT copy text out of the terminal and CANNOT scroll the TUI.
    Agent reports must be written to files in the repo and pushed; Nir opens
    GitHub in a browser and copies to Fable from there. Until git push works
    on a new machine, keep agent reports short enough to retype by hand.
  - Markdown tables BREAK when copy-pasted. Never use them. Plain text
    key: value lines and bullet lists only.
  - If the agent suddenly refuses to execute anything: Nir likely pressed
    TAB and toggled OpenCode into read-only Plan Mode. Ask him to toggle back.
- [SPACE RESERVED FOR NIR: anything from the earliest sessions that this
  document does not contain - other dreams beside Alpha Babes, how you first
  imagined the whole project, anything precious - paste or write it to the
  new Fable HERE in your own words. Fable: treat whatever Nir adds here as
  part of this briefing.]

--- PART 2: THE PROJECT - ALPHA BABES ---
- A GIFT for Nir's girlfriend Madie (Romanian). DEADLINE: ~August 3, 2026.
- "Alpha Babes": hard sci-fi anime saga. A crew of women from different
  countries exploring exoplanets, speaking English with their national
  accents. 5 seasons planned, ~20 episodes each. The name means BABES
  (attractive adult women), explicitly NOT babies/children.
- The script is ALREADY WRITTEN. Character art and spaceship art (interior
  and exterior) already exist - Nir made them on OpenArt (cloud AI). These
  reference images are high quality; local generation is held to a high
  standard because of them.
- CONSENT AND BOUNDARIES (absolute):
  - Madie gave FULL consent for her name and likeness to be used.
  - She REFUSED any recording or cloning of her real voice. HARD BOUNDARY.
    Never suggest it, never work around it. An AI-DESIGNED voice built from
    a text description is allowed and planned.
- MADIE CONVERSION RULES (baked into all source material adaptation):
  - Lead character "Chief" -> renamed Madie
  - Her country UK -> Romania (Romania flag patch on spacesuit shoulder,
    name tag on chest)
  - Comfort ritual tea -> borscht (soup)
  - Hair redhead -> brunette
  - Everything else stays faithful to the source documents.
- MADIE ON SCREEN, ALWAYS: young adult woman in her EARLY 20s, womanly,
  curvy, shapely figure (Nir: "babes not babies"), brunette, ALWAYS wearing
  her spacesuit, NEVER anything on her head (no helmet, no headwear, ever).

--- PART 3: THE DELIVERABLE - "JODOROWSKY PIVOT" (FINAL FORMAT) ---
- NOT a video. NOT animated. The deliverable is an ILLUSTRATED, NARRATED
  SAGA: still images + narration audio - "the book of the movie that
  doesn't exist yet."
- Assembly in Adobe Premiere on Windows: Ken Burns pan/zoom over stills,
  sound design, Nir's existing AI-made songs for the credits.
- Subtitles: Romanian + English, made in Aegisub, hardcoded with Avidemux.
- End-card: a personal dedication to Madie.
- Bonus deliverables: a PDF artbook + one physical printed copy.
- OPTIONAL luxury, only if absolutely everything else is finished: a tiny
  animated opening with Wan 2.2 (details in Part 7).

--- PART 4: SOURCE DOCUMENTS ---
- Story arc (~114 pages), Episode 1 script (~43 pages), ship structure
  (already .txt), background summary (~32 pages).
- Plan: all converted to UTF-8 .txt in AlphaBabes/source_docs/ in the repo.
- STATUS UNCERTAIN: ASK NIR whether the conversion/upload is complete.
  These documents feed the scenes.csv work (Part 5) - they matter soon.

--- PART 5: SCENES AND VISUAL BIBLE ARCHITECTURE ---
- Homogeneous-coverage passes, so the saga is covered evenly even if time
  runs out: Pass 1 = ~25 keystone scenes covering the whole saga ->
  Pass 2 = ~100 scenes (about 1 per episode) -> Pass 3 = ~300 scenes
  (about 3 per episode). Each pass is a complete, watchable gift on its own.
- Scene IDs: S{season}E{episode}-{slot}, slots in gapped tens (10, 20,
  30...) so scenes can be inserted later without renumbering.
- scenes.csv columns (exact): scene_id, season, episode, pass_number,
  location, characters, description, image_prompt, narration_text,
  image_status, audio_status, assigned_machine, notes.
- scenes.csv is WRITTEN BY AN AGENT - a cheap long-context OpenRouter model
  inside OpenCode reads the source docs and drafts it. Fable writes the
  agent's instructions and QA-checks the output. Fable does NOT write 300
  scenes by hand, and neither does Nir. Model choice for this: still open.
- Visual Bible: locations.csv (location_id, name, ref_image_path,
  prompt_block, fixed_seed, notes) + a refs/ folder of reference images
  (many from Nir's OpenArt ship art).
- IMAGE CONSISTENCY DOCTRINE - four channels, strongest to weakest:
  1. Character LoRAs (tier 1 - carries WHO a character is)
  2. IP-Adapter with reference images (tier 2 - carries looks of places/things)
  3. ControlNet + fixed seeds (tier 3 - carries composition/pose)
  4. Text prompt (tier 4 - NEVER trusted to carry character identity or
     room design on its own).

--- PART 6: HARDWARE - THE FOUR MACHINES ---
Machine 1 LAPTOP - Lenovo Legion, Debian 13 on external SSD, dual-boot Win11:
- user "nir", 64GB RAM, RTX 5090 Max-Q Mobile 24GB VRAM (Blackwell sm_120,
  95W cap), driver 580.95.05 (open kernel modules, DKMS), kernel
  6.12.94+deb13-amd64 with headers metapackage (survives kernel updates),
  CUDA 13.0 at /usr/local/cuda-13.0, Secure Boot OFF, ~1.4TB free.
- Miniforge3 fresh (scorched-earth rebuild). Envs: "comfyui" (Python 3.12,
  ComfyUI 0.28.0), "kohya" (Python 3.10, sd-scripts). PyTorch 2.11.0+cu128.
- ROLE: character images + LoRA training (+ optional Wan video at the end).
- STATE: FULLY OPERATIONAL. Madie LoRA trained and proven here (Part 9).
  Do not touch this machine unless needed.
Machine 2 DESKTOP - Lenovo Legion, Linux Mint 22 on external SSD, dual-boot
Win11: 64GB RAM, RTX 4070 Ti 12GB VRAM.
- ROLE: backgrounds, planets, ships, ALL TTS, upscaling.
- STATE: UNTOUCHED, UNKNOWN, NOT BOOTSTRAPPED. No OpenCode yet. NVIDIA
  driver status unknown. Old junk expected (old conda, docker, agents, AI
  tools, old projects) - Nir wants it ALL deleted before starting.
- THIS IS SESSION 5'S MACHINE. Bootstrap plan in Part 12.
Machines 3+4 - Windows 11 laptop + desktop, factory-fresh (reset July 21):
- Idle until assembly week. Desktop Win11 gets Premiere + Aegisub +
  Avidemux; both get OpenCode + Git when needed.
DIVISION OF LABOR (final): Laptop 5090 = characters + training. Desktop
4070 Ti = environments + TTS + upscaling. All AI on Linux; assembly on
Windows. NO swap-as-VRAM ever; use quantization + CPU offload instead.
SYNC: GitHub for text/code (working). Syncthing over LAN for media - NOT
set up yet; needed to bring the Madie LoRA and images between machines.

--- PART 7: TOOL STACK (FINAL DECISIONS) ---
- ComfyUI is the image hub on both Linux machines, models loaded
  sequentially, one job at a time.
- Base model: Illustrious-XL (file: Illustrious-XL-v0.1.safetensors, 6.5GB,
  from OnomaAIResearch on Hugging Face). Illustrious speaks DANBOORU TAGS -
  always prompt in Danbooru style. CFG sweet spot 3.5-5.0.
- Laptop renders native up to ~1536x1536; desktop (12GB) renders 1024 base
  with fp16/FP8 and tiled/modest upscales.
- Character LoRA training: kohya-ss/sd-scripts. Captioning: WD14 tagger
  (SmilingWolf/wd-swinv2-tagger-v3, ONNX). Trigger word pattern:
  chara_<name> (Madie's: chara_madie).
- TTS (desktop, future): Qwen3-TTS voice DESIGN from text description
  ("young woman, warm confident voice, English with distinct Romanian
  accent") -> export a ~5s snippet -> F5-TTS zero-shot clone of that
  snippet locks the voice identical across all future sessions.
  Fallback parachute: ElevenLabs Voice Design (Nir has an account).
- PAID PARACHUTES exist for both media types if local fails: images ->
  OpenArt, voice -> ElevenLabs. Never let the project die on local pride.
- Optional Wan 2.2 opening (ONLY if everything else is 100% done):
  Wan 2.2 14B GGUF Q4/Q8, FLF2V, dual UNET loaders, Lightning LoRA 8-step
  (CFG 1.0, LCM, split at step 4), 720p x 81 frames, --reserve-vram 3.0,
  sageattention. Lip-sync: MuseTalk or skip.
- Agents: OpenCode ONLY, on all four environments. OpenClaw REJECTED -
  "one agent tool everywhere = one thing to learn, one thing that can
  break." All model access via OpenRouter (Israeli credit cards are
  declined by Alibaba and others direct) - the SAME OpenRouter API key is
  used on every machine.

--- PART 8: AGENT-FIRST WORKFLOW DOCTRINE ---
Nir never types commands (except unavoidable manual bootstrap steps).
Fable writes mission prompts in code blocks; Nir pastes them to OpenCode.
EVERY mission must contain:
- Explain each action in one simple sentence, before doing it.
- Execute ONE step at a time. Never batch.
- On ANY error: STOP, show the error VERBATIM, never improvise fixes.
- A STRICT WHITELIST of what may be created/modified; everything else
  forbidden by name (driver, CUDA, ssh, bashrc, envs, etc.).
- High-stakes missions: read-only diagnostic phase first, then a hard brake
  - print a fixed sentence and WAIT for Nir to type "go".
- NEVER ASSUME MACHINE STATE. Verify before acting.
- Agents are encouraged to PAUSE and ask questions via Nir.
KNOWLEDGE BASE PROTOCOL: important Fable answers saved VERBATIM to
AlphaBabes/knowledge_base/, numbered in gapped tens (010, 020... latest is
230 = this document). Save template: git add . && git commit -m
"KB: <title>" && git push. Key existing KB files: 210_madie-lora-recipe.md
(full proven LoRA recipe), 220_MASTER-REFERENCE.md (DeepSeek's long
reference incl. session history), 230 = this briefing.

--- PART 9: MADIE LORA - PROVEN RESULT (the laptop's crown jewel) ---
- WINNER: chara_madie_v1.safetensors (epoch 10, 218MB) in
  ~/Anime/tools/ComfyUI/models/loras/ on the laptop. Runner-up spare:
  epoch 8 file. Both backed up in ~/Anime/media/backups/madie_lora_v1/
  together with the zipped captioned dataset.
- Training recipe (proven, reproducible): Illustrious-XL-v0.1 base, 36
  images 1024x1024 RGB (dataset folder 10_chara_madie), sd-scripts, LoRA
  dim 32 / alpha 16, batch 4, 10 epochs ~900 steps (~37 min on the 5090),
  lr 1e-4 / text encoder 5e-5, cosine + 50 warmup, AdamW, bf16,
  min_snr_gamma 5, shuffle_caption, keep_tokens 2, seed 42, snapshots every
  2 epochs. Final avg loss ~0.068.
- Caption recipe: "chara_madie, <emotion word from filename>, <WD14 tags>";
  WD14 threshold 0.35; identity tags PRUNED so the trigger absorbs her
  (hair color/length, eye color, lips, bangs, ponytail/braid/bun, breasts);
  removed harmful tags: "astronaut", "american flag", "japanese flag",
  "realistic"; ensured "black background" tag on every caption (the
  dataset's black backgrounds are neutralized by TAGGING, not by editing -
  transparency is useless to SDXL training).
- PROVEN GENERATION SETTINGS: LoRA strength 1.0 (model+clip). Positive:
  "masterpiece, best quality, chara_madie, 1girl, solo, mature female,
  young woman, spacesuit, no headwear, <TAGS>, simple background, grey
  background". Negative: "worst quality, low quality, bad anatomy, bad
  hands, extra digits, watermark, signature, text, black background,
  helmet, space helmet, headwear, hood, hat, hair ornament, child, chibi,
  loli, aged down, deformed, large head". CFG 4.5, euler_ancestral.
  QUALITY two-pass: 40 steps -> LatentUpscaleBy 1.5x -> 20 steps denoise
  0.45. Canvas: portraits 1024x1024 base, FULL BODY 832x1216 base (tall!).
  Fixed seed 123456789 for tests; vary seeds for production.
- Generator script exists: ~/Anime/tools/madie_sweep.py (laptop) - ComfyUI
  API client with all test job lists inside.
- KNOWN WEAK POINTS (plan around them): tiny insignia (Romania flag patch,
  name tag) scramble at normal sizes - close-ups need a detailer/inpaint
  pass (e.g. Impact Pack) or a pasted clean patch; left profile and
  from-behind are the dataset's thin side (only front/back/right existed) -
  support those angles with IP-Adapter/ControlNet when they matter.
- Nir's verdict: PASSED. Good enough vs. his cloud references given local
  constraints; production scenes get extra polish (seed variants, detailer).

--- PART 10: THE 33 EMOTIONS - DANBOORU TAG MAP (project asset) ---
neutral = neutral expression, closed mouth
happiness = happy, smile
sadness = sad, frown
anger = angry, furrowed brow
fear = scared, wide eyes, trembling
surprise = surprised, open mouth, wide eyes
disgust = disgust, wavy mouth
contempt = smug, narrowed eyes, smirk
joy = joyful, grin, sparkling eyes
love = loving gaze, blush, smile
hate = glaring, hateful stare, shaded face
hope = hopeful, gentle smile, looking up
boredom = bored, half-closed eyes
calmness = calm, serene, soft smile, closed eyes
excitement = excited, open mouth smile, clenched hands
interest = curious, head tilt, bright eyes
wonder = wonder, parted lips, wide eyes, looking up
awe = awe, amazed, hand over own mouth
adoration = adoring gaze, sparkling eyes, own hands clasped
amusement = amused, giggling, hand over own mouth
compassion = compassionate, gentle expression, warm smile
crying = crying, tears, tearful eyes
embarrassment = embarrassed, full blush, averting gaze
envy = envious, pout, side glance
gratitude = grateful, warm smile, hand on own chest
horror = horrified, wide eyes, open mouth
laughing = laughing, open mouth, closed eyes
rage = enraged, clenched teeth, screaming
relaxation = relaxed, content, closed eyes
sensory pleasure = blissful, closed eyes, content smile
shame = ashamed, looking down, downcast eyes
depression = depressed, empty eyes, head down
arousal = flustered, heavy blush, half-closed eyes

--- PART 11: LESSONS LEARNED (Fable's added wisdom - do not relearn these) ---
1. The word "astronaut" in prompts/captions summons white caps/helmets and
   fights the character's hair. Keep "spacesuit", kill "astronaut".
2. Full-body figures on SQUARE canvases come out child-proportioned (big
   head). Full body ALWAYS on tall canvas (832x1216).
3. Anime base models default to generic young girls unless the prompt says
   adult: always "mature female, young woman" positive + "child, chibi,
   loli, aged down" negative.
4. Epoch snapshots every 2 epochs = five candidates from one training run;
   pick by visual duel with fixed prompts/seed. Nir picks the winner, not
   metrics.
5. Prune identity tags from captions so the trigger word absorbs the
   character; keep pose/expression/clothing/background tags for control.
6. WD14 mis-tags things (saw her Romania patch as american/japanese flags) -
   always review and surgically clean captions.
7. Fixed seed + one-variable-at-a-time is how every comparison is done
   (emotion sweeps, epoch duels). Change one thing, keep everything else.
8. Cloud giants (the references were made with big cloud models) will beat
   local polish - honesty about this is fine, but local wins on
   consistency, unlimited volume, zero marginal cost, and ownership. For
   final gift images: generate multiple seeds, pick the best, add detailer
   passes. Never present a fast preview as final quality.
9. When something looks wrong, the cause is usually the PROMPT TEMPLATE or
   CANVAS, not the LoRA - diagnose before retraining. Retraining is the
   last resort, prompt surgery is free.

--- PART 12: SESSION 5 GOAL - DESKTOP MINT BOOTSTRAP, IN ORDER ---
Step 0 MANUAL (no agent exists there yet; walk Nir through, one command at
a time, explained simply): install OpenCode (curl -fsSL
https://opencode.ai/install | bash), reopen terminal, opencode auth login
-> OpenRouter -> SAME API key as the laptop, start opencode, verify.
Mission G1 READ-ONLY RECON (changes nothing): Mint version, disk free,
nvidia-smi / does a driver exist, GPU on PCI bus, inventory of old junk
(conda/miniconda, docker, venvs, old AI tools, old projects), git present?
Short report (Nir may have to retype it - keep it tiny). Brake, wait "go".
Mission G2 GIT + REPO: install git if missing, clone
https://github.com/strulovitz/Anime to ~/Anime, set identity, set up push
credentials (ASK NIR how the laptop authenticates - mirror it). From here
reports go into the repo as pushed files.
Mission G3 SCORCHED EARTH (diagnostic list -> "go" brake -> delete): ALL
old conda, venvs, docker, old agents/AI tools, caches, old projects.
PROTECTED ONLY: NVIDIA driver stack (if present), ~/Anime, OpenCode + auth,
~/.ssh, ~/.bashrc, ~/.config essentials.
Mission G4 NVIDIA DRIVER if missing: Mint 22 is Ubuntu 24.04-based; use
Driver Manager / ubuntu-drivers; 4070 Ti is mainstream (far easier than
the laptop's Blackwell saga). Reboot, verify nvidia-smi + persistence.
Mission G5 FRESH MINIFORGE: one clean Miniforge3.
Mission G6 COMFYUI: env "comfyui", PyTorch cu128, ComfyUI at
~/Anime/tools/ComfyUI, launcher ~/Anime/tools/start_comfyui.sh (mirror
laptop layout), download Illustrious-XL-v0.1.safetensors, smoke-test one
1024x1024 image, confirm 12GB VRAM behavior.
AFTER BOOTSTRAP (later sessions, keep the whole in view): Syncthing LAN
sync (bring Madie's LoRA over); source docs .txt (ask Nir, Part 4);
scenes.csv by long-context agent; Visual Bible locations.csv + refs;
background/planet/ship passes; TTS chain; Windows machines + assembly week
(~end of July); Pass 1 ~25 keystone images with narration; PDF artbook;
optional Wan opening last.

--- PART 13: CURRENT STATE SNAPSHOT (2026-07-22 evening) ---
DONE: repo live; laptop fully operational (driver, ComfyUI, kohya); Madie
LoRA trained, tested across 33 emotions + 18 direction/pose + 10 combos,
quality pipeline proven, winner epoch 10, everything backed up, recipe in
KB 210.
NOT DONE (priority order): desktop bootstrap (Part 12) -> Syncthing ->
source docs check -> scenes.csv -> Visual Bible -> TTS -> Windows setup ->
Pass 1 images -> assembly -> artbook -> optional Wan opening.
DEADLINE: ~August 3, 2026. About 12 days remain. The passes architecture
(Part 5) guarantees a complete gift at ANY cutoff point - protect that
property in every plan.

--- PART 14: CLOSED DECISIONS - NEVER REOPEN ---
OpenCode only (OpenClaw rejected). OpenRouter only, same key everywhere.
Illustrated narrated saga, not video. Scorched earth on both Linux
machines. Agent-first workflow. Knowledge base verbatim saves. Black
backgrounds handled by captioning. LoRA > IP-Adapter > ControlNet+seed >
text for consistency. No swap-as-VRAM. Media is .gitignored (repo is
PUBLIC - never commit Madie's images). Quality over speed. One mission per
reply. Madie: early-20s babe, spacesuit always, bare head always, voice
never cloned from the real Madie.

Final word from your past self: the laptop gave Madie her face and all 33
of her feelings. This desktop gives her a galaxy, and then a voice. Nir
trusted us with the most personal gift a person can build. Carry every
detail like it's precious - because to him, it is. :-) 🚀💖
=== END BRIEFING ===
