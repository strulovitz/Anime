# AUDIT: Corrections for SUHUF and TAWRAT holy books
# Based on verified KB files + live machine data 2026-07-23

======================================================================
DESKTOP (TAWRAT-DESKTOP-LINUX.md) — CORRECTIONS:
======================================================================

❌ GPU: Fable wrote "RTX 5090, 32 GB VRAM"
   TRUTH: NVIDIA GeForce RTX 4070 Ti, 12 GB VRAM (verified by nvidia-smi today)
   NOTE: This is the SECOND machine, the DESKTOP with Mint 22. The 4070 Ti is
   mid-range — 1024px base renders, FP8, tiled upscale. Do not plan for 32GB.
   The 5090 is the LAPTOP (see SUHUF corrections below).

❌ RAM: Fable wrote "96 GB"
   TRUTH: 62Gi (64 GB) (verified by free -h today)

✅ CPU: "Intel i9" — CORRECT (verified: 13th Gen Intel Core i9-13900KF)

✅ Disks: all correct
   - sda2 root "/" 92GB, ~47GB free
   - sda4 /home 1.7TB, ~1.4TB free
   - NEVER TOUCH: nvme0n1 (internal 4TB Windows BitLocker), sdb (EXTERNAL12 12TB)

❌ Kernel/OS: TAWRAT says Mint 22 — correct OS, but:
   Kernel is 7.0.0-28-generic (verified: uname -r today)
   NOT the older kernel Fable may have from old KB records.

❌ GPU driver: TAWRAT doesn't specify
   TRUTH: NVIDIA driver 595.71.05, Canonical-signed, factory kernel modules
   (verified: nvidia-smi today). CUDA 13.2.

======================================================================
LAPTOP (SUHUF-LAPTOP-LINUX.md) — CORRECTIONS:
======================================================================

❌ GPU: Fable wrote "RTX 5070, 8 GB VRAM"
   TRUTH: RTX 5090 Max-Q Mobile, 24 GB VRAM
   Source: KB 040 (lspci output: GB203M / GN22-X11 [GeForce RTX 5090 Max-Q])
   Source: KB 230 ("Laptop 5090 = characters + training")
   Source: KB 210 ("Training time: ~37 minutes on RTX 5090")
   Source: KB 220 ("24GB VRAM, Blackwell sm_120, 95W power cap")
   This is the STRONGEST GPU in the project. The 5070 exists nowhere.

❌ Madie LoRA version: Fable wrote "Madie LoRA v3 — epoch 6, strength 0.7-0.75"
   TRUTH: Madie LoRA v1 — epoch 10, strength 1.0
   Source: KB 210 ("WINNING FILE: chara_madie_v1.safetensors (epoch 10)")
   Source: KB 230 ("epoch 10 winner, 218MB")
   Source: KB 220 ("chara_madie_v1.safetensors (epoch 10, 218MB)")
   Source: KB 230 ("LoRA strength: 1.0 (model + clip)")
   There is NO v3. There is no epoch 6 winner. The v1 epoch 8 is the spare.

❌ Conda env name: Fable wrote "anime" (Python 3.11)
   TRUTH: "comfyui" (Python 3.12)
   Source: KB 090 ("Create ONE new conda environment named 'comfyui'")
   Source: KB 220 ("comfyui env Python 3.12, ComfyUI 0.28.0")
   Source: KB 230 ("Envs: comfyui (Python 3.12)")
   There is NO env named "anime". Never was.

✅ Conda env "kohya" (Python 3.10) — CORRECT
   Source: KB 220 ("kohya env Python 3.10, sd-scripts")

✅ Miniforge at ~/miniforge3 — CORRECT
✅ Repo at ~/Anime — CORRECT
✅ Base model: Illustrious-XL — CORRECT
✅ 36 training images, 1024x1024 — CORRECT

❌ PyTorch: SUHUF says "needs PyTorch nightly cu128"
   TRUTH: PyTorch 2.11.0+cu128 (verified working, KB 220)
   Nightly was the fix path; it has been resolved to 2.11.0+cu128.

======================================================================
DEADLINE:
======================================================================
✅ ~August 3, 2026 — CORRECT (stated across ALL KB files 150, 230, 220, etc.)
   Source: KB 230 ("DEADLINE: ~August 3, 2026. About 12 days remain.")
   This is the gift for Madie's birthday. Everything else waits.

======================================================================
MOST DANGEROUS ERRORS (highest risk to the project):
======================================================================
1. SUHUF says laptop has 8GB VRAM RTX 5070 — it actually has 24GB RTX 5090.
   If Fable plans for 8GB, he will cripple generation quality needlessly.
2. TAWRAT says desktop has 32GB RTX 5090 — it actually has 12GB RTX 4070 Ti.
   If Fable assumes 32GB, he will crash OOM constantly.
3. Madie LoRA "v3 epoch 6" doesn't exist. Only v1 epoch 10 (winner) and
   v1 epoch 8 (spare) exist. Using 0.7 strength vs. 1.0 will lose her likeness.
4. Conda env "anime" doesn't exist — the env is "comfyui".
