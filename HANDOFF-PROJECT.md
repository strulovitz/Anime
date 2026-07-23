# HANDOFF: Nir's AI art project — FULL INSTALLATION PLAN
# Written by Fable (Claude) 2026-07-23. For a fresh Fable session tomorrow.
# This file supersedes ALL previous plans.

## NIR'S FINAL DECISIONS — NOT OPEN FOR DISCUSSION
1. NO partition resizing. NO touching swap. NO disk surgery of any kind. Final.
2. EVERYTHING installs under /home/nir/ (the 1.7T partition, 1.4T free).
3. Fable (you) is the brain and gives orders. DeepSeek (coding agent in
   OpenCode) is HANDS ONLY — it executes exactly what you dictate, nothing more.
4. NEVER touch nvme0n1 (Windows, BitLocker) or sdb (EXTERNAL12). Ever.

## WHO NIR IS — READ CAREFULLY
- Highly intelligent inventor. NOT technical: no Linux, no Python knowledge.
- ADHD: ONE step per message. Short messages. NO long documents to follow.
  Wait for his pasted output before giving the next step. Never assume success.
- He pays per token. Be concise. No filler, no cheerleading, no re-explaining.
- He copy-pastes between you, the terminal, and DeepSeek. Respect him;
  he catches flawed logic instantly. If unsure, say so plainly.

## SYSTEM FACTS (verified 2026-07-23)
- Linux Mint desktop, 64 GB RAM.
- sda = WD P40 external 2TB, Linux only:
  sda2 93G ext4 = / (47G free) | sda3 61G swap (DO NOT TOUCH)
  sda4 1.7T ext4 = /home (1.4T FREE) ← everything goes here
- GPU: unverified. VERIFY IN PHASE 0 before choosing PyTorch build.
- Status: DeepSeek holds an OLD mission ("Ready. Type go"). CANCEL it and
  issue fresh missions per this plan — the old one measured the wrong partition.

## HONESTY CLAUSE (tell Nir once, then proceed)
Tiny system packages installed via apt (e.g. python3-venv, GPU driver if
missing) physically live on / by OS design — they are megabytes, and 47G free
is ample. Every large item (>100MB) — PyTorch, ComfyUI, models, caches — goes
under /home/nir/. Show df -h /home before and after every big download.

## THE COMPLETE INSTALL LIST — E-V-E-R-Y-T-H-I-N-G

### PHASE 0 — Verify before installing anything
- GPU:  nvidia-smi   (if missing: lspci | grep -i vga) → determines PyTorch build
- git --version ; python3 --version
- df -h /home   → confirm ~1.4T free
- If NVIDIA driver missing: install via Mint Driver Manager (small, on /, allowed)

### PHASE 1 — Foundation (all under /home/nir/ai-art/)
- mkdir -p /home/nir/ai-art
- apt install python3-venv python3-pip (only if missing; tiny)
- Create venv:  python3 -m venv /home/nir/ai-art/venv
- Set HuggingFace cache into the project (add to ~/.bashrc):
  export HF_HOME=/home/nir/ai-art/hf-cache

### PHASE 2 — PyTorch (~10 GB, into the venv → lands on /home)
- Activate venv, install torch/torchvision matching the GPU found in Phase 0
  (CUDA build for NVIDIA; otherwise adapt).
- Verify:  python -c "import torch; print(torch.cuda.is_available())"

### PHASE 3 — ComfyUI (the art application)
- git clone ComfyUI into /home/nir/ai-art/ComfyUI
- pip install its requirements.txt inside the venv

### PHASE 4 — Models (into /home/nir/ai-art/ComfyUI/models/checkpoints/)
- Stable Diffusion XL base 1.0 (~7 GB) — the main image model
- SDXL VAE if not bundled
- (More models later only if Nir asks — do not pile on)

### PHASE 5 — Make it easy to start
- Create /home/nir/ai-art/start.sh : activates venv, launches ComfyUI,
  prints "open http://127.0.0.1:8188 in your browser"
- chmod +x, and give Nir the one line to run it.

### PHASE 6 — Prove it works
- Launch, open browser, generate one test image. That image = mission complete.

### PHASE 7 — Permanent law
DeepSeek adds to AGENTS.md, commits, pushes:
"RULE: All installs, venvs, models, downloads go under /home/nir/ — never on
the root partition. Before any download >1GB run df -h /home and show it.
Report every step. Stop on any error. Never touch nvme0n1, sdb, or swap."

## METHOD OF WORK
- You dictate each DeepSeek instruction verbatim in a copy-paste block.
- Nir pastes it, pastes back the result. You verify, then next step.
- Any error or unexpected output: STOP, explain in plain words, no improvising.
- One phase at a time. Long downloads = tell Nir to get coffee.

## HOW TOMORROW STARTS
Nir pastes this file into a fresh chat and says "continue".
You greet him in ONE sentence and immediately give Phase 0, step 1.