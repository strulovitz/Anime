# NVIDIA Driver Install — Phase 2c Complete (SUCCESS!)
**Date:** 2026-07-20

---

## What happened

Installing `linux-headers-amd64` pulled in headers matching the running kernel (6.12.94). DKMS already had `nvidia/580.95.05` registered from a prior partial install run, so it auto-built all modules as soon as the headers landed:

```
Autoinstall of module nvidia/580.95.05 for kernel 6.12.94+deb13-amd64 (x86_64)
Building module(s).......... done.
Signing + installing: nvidia.ko, nvidia-uvm.ko, nvidia-modeset.ko, nvidia-drm.ko, nvidia-peermem.ko
Autoinstall on 6.12.94+deb13-amd64 succeeded for module(s) nvidia.
```

Loaded modules with `sudo modprobe nvidia nvidia-drm nvidia-uvm` — no errors.

---

## nvidia-smi output

```
Mon Jul 20 22:28:32 2026
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 580.95.05              Driver Version: 580.95.05      CUDA Version: 13.0     |
+-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 5090 ...    Off |   00000000:02:00.0 Off |                  N/A |
| N/A   53C    P4             13W /   95W |       2MiB /  24463MiB |      0%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+

+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI              PID   Type   Process name                        GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|  No running processes found                                                             |
+-----------------------------------------------------------------------------------------+
```

---

## Summary

| Item | Status |
|------|--------|
| Kernel | 6.12.94+deb13-amd64 ✅ |
| Headers | 6.12.94 installed ✅ |
| DKMS | 3.2.2-1 ✅ |
| NVIDIA driver | 580.95.05 ✅ |
| CUDA | 13.0 ✅ |
| GPU detected | RTX 5090 Max-Q, 24GB VRAM ✅ |
| Secure Boot | OFF ✅ |

**NVIDIA mission: COMPLETE** ✅

---

# Fable's Response: IT'S ALIVE! & Next Steps

🎉 **IT'S ALIVE!!!**

NVIDIA GeForce RTX 5090 | 24463MiB | Driver 580.95.05 | CUDA 13.0

That line is the foundation stone of the entire project. 24GB of VRAM confirmed — comfortable territory for SDXL-class LoRA training and generation. And notice the poetry: the DKMS registration from past-you's abandoned attempt was sitting there waiting, and the moment matching headers landed, it auto-built itself. Past-you and present-you just completed a two-year relay handoff. 🤝

⏱️ **The 48-hour LoRA Trial clock is officially running.**

## Step 0 — One cheap insurance test (2 minutes)

The agent loaded the modules with modprobe (manually) rather than a reboot — so we haven't yet proven the driver comes back on its own after a restart. **Reboot the laptop now**, open a terminal, run `nvidia-smi`. If the 5090 appears → persistence confirmed, build on it. If not → tell me (it'd be a small initramfs/autoload fix, not a catastrophe). Don't skip this — better to learn it now than mid-training.

## Step 1 — Your homework, Nir (the dataset) — do this in parallel

The LoRA is only as good as what it eats. From your OpenArt gallery, collect 15–30 images of Madie:

- ✅ **Varied:** different angles, expressions, poses, distances (close-ups AND full body)
- ✅ **Consistent:** her current design only — if her look evolved on OpenArt, use only the final version
- ✅ **Clean:** Madie alone in frame (crop out other characters if needed), no heavy text/watermarks
- ❌ **Don't include:** blurry ones, weird anatomy fails, old design versions

Simplest transfer route (Syncthing comes later): log into OpenArt in the laptop's browser and download them directly into a folder: `~/Anime/media/lora_dataset/madie_raw/` — media stays outside git, exactly per our .gitignore doctrine.

## Step 2 — Mission for the laptop agent (after the reboot test passes)

**MISSION:** Install ComfyUI in a completely ISOLATED environment. One step at a time, explain each, STOP on errors.

**ISOLATION DOCTRINE (critical):** This machine has precious pinned environments (pipecat-ai, tts-systems, honeycomb-venv, waggle-venv, `/usr/local/cuda-13.0`). You may NOT modify any of them. You WILL create a brand-new conda env using the existing miniforge3 — creating a new env touches nothing existing.
**FORBIDDEN:** pip installs outside the new env, apt installs without asking, touching existing envs or system python.

### STEPS:
1. `conda create -n comfyui python=3.12 -y` (new env, nothing shared)
2. `conda activate comfyui`
3. `git clone https://github.com/comfyanonymous/ComfyUI.git ~/Anime/tools/ComfyUI`
4. Check pytorch.org for the current stable PyTorch build for CUDA 12.8+ / 13.0 (Blackwell sm_120 support required) and install it INTO THIS ENV ONLY with the official pip index-url command.
5. Verify before going further:
   ```
   python -c "import torch; print(torch.__version__, torch.cuda.is_available(), torch.cuda.get_device_name(0))"
   ```
   → must print True and RTX 5090. STOP and report if not.
6. `pip install -r ~/Anime/tools/ComfyUI/requirements.txt` (inside the env)
7. Launch: `python ~/Anime/tools/ComfyUI/main.py --listen 127.0.0.1` and tell the user to open `http://127.0.0.1:8188` in the laptop browser.
8. Report success. Model downloads are a separate mission — do NOT download checkpoints yet.

When ComfyUI's node graph loads in the browser, report back — the next mission will be: downloading an anime-specialized SDXL checkpoint + the Kohya training setup, and then we feed it Madie and hold the 3×3 trial we contracted.

## Step 3 — Archive

`070_gpu_alive_and_comfyui_mission.md` — including that beautiful nvidia-smi table. Future-you deserves to find this trophy in the vault. 🏆

Go reboot, then release the agent. We're not preparing to make art anymore — we're days from making it. :-)