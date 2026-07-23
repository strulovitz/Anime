# Where We Stopped — 2026-07-23

## Completed
- G1 Roots: AGENTS.md + opencode config ✅
- G2 Clone: Anime repo cloned, git identity set, push working ✅
- G3 Scorched Earth: ~14GB freed ✅
- G4 NVIDIA Driver: nvidia-driver-580-open installed ❌ (blocked by Secure Boot)
- G4b NVIDIA Driver FIX: 580 purged, 595 DKMS-built + MOK-signed ✅
- G4c MOK debug: DKMS rebuild, MOK re-import (failed — key not enrolled) ✅
- G4e Diagnosis: no pre-signed package for 6.14.0-37-generic ✅
- **G4g OFFICIAL KERNEL UPGRADE**: Kernel 7.0.0-28-generic + Canonical-signed NVIDIA 595.71.05 ✅

## Current State
- Running kernel: 6.14.0-37-generic (needs reboot to use new one)
- New kernel installed: 7.0.0-28-generic
- NVIDIA driver: linux-modules-nvidia-595-open-7.0.0-28-generic — signed by "Canonical Ltd. Kernel Module Signing"
- Old kernel 6.14.0-37 still installed as GRUB fallback
- NO MOK, NO blue screen — factory-signed!

## Next — After Reboot
1. **REBOOT** — Machine will boot into 7.0.0-28-generic automatically
2. Run: `nvidia-smi` — should show RTX 4070 Ti with driver 595.71.05
3. Then G5: Miniforge3 install
4. Then G6: ComfyUI install + Illustrious-XL download