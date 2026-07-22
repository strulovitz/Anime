# KB 240 — Mission G4b: NVIDIA Driver 595-Open Installed on Desktop Mint
**Date:** 2026-07-22
**Status:** DONE. Driver installed, modules signed, awaiting reboot.

## What happened
- Found 580-open installed but blocked by Secure Boot (no signed modules).
- Purged all 580 packages cleanly.
- Installed nvidia-driver-595-open (595.71.05) via apt.
- DKMS built all 5 modules for kernel 6.14.0-37-generic.
- ALL modules are AUTOMATICALLY SIGNED with system MOK key — Secure Boot compatible.
- No linux-modules-nvidia prefab signed packages needed (DKMS handled signing automatically).

## Current state
- driver: nvidia-driver-595-open (595.71.05)
- kernel: 6.14.0-37-generic
- Secure Boot: ON
- modules: nvidia, nvidia-modeset, nvidia-drm, nvidia-uvm, nvidia-peermem — all signed
- dkms status: nvidia/595.71.05 installed for 6.14.0-37-generic

## Next step
- REBOOT the Mint desktop
- After reboot, run: nvidia-smi
- Should show RTX 4070 Ti, 12GB VRAM
- If yes: proceed to G5 (Miniforge) then G6 (ComfyUI)!