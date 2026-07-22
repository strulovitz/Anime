# Session 4 — Fable's Reply: Mission D — Full Test Sweep!
**Date:** 2026-07-22 ~Evening
**Chat:** Claude Fable 5 (OpenRouter)

---

36 minutes 42 seconds — Madie has been LEARNED by the 5090!! 🥳🔥🎉

Loss 0.0685 is right in the sweet spot, and we have 5 snapshots to choose from. Now the moment of truth — Mission D, in two acts :-)

Act 1 — Snapshot Shootout 🥊: Before the big sweep, we generate the SAME 3 test images with each of the 4 serious snapshots (epochs 4, 6, 8, 10) — 12 images total. You look at them and pick the winner.

Act 2 — The Full Sweep 🎭: With your chosen snapshot: all 33 emotions (portraits) + 18 direction/pose shots + 10 stress combos = 61 images.

## MISSION D — Full Instructions

### PHASE 1 - PRE-FLIGHT:
- Verify 5 LoRA files exist
- Start ComfyUI via launcher
- Create output folders: ~/Anime/media/tests/madie_sweep/{shootout,emotions,directions,combos}

### PHASE 2 - BUILD GENERATOR SCRIPT:
Write ~/Anime/tools/madie_sweep.py using ComfyUI HTTP API (POST /prompt, GET /history).
Workflow: CheckpointLoaderSimple (Illustrious-XL-v0.1) -> LoraLoader (strength 0.9/0.9) -> CLIPTextEncode -> EmptyLatentImage 1024x1024 -> KSampler (seed 123456789, steps 28, cfg 4.5, euler_ancestral) -> VAEDecode -> SaveImage.

Positive prompt: "masterpiece, best quality, chara_madie, 1girl, solo, spacesuit, <TAGS>, simple background, grey background"
Negative: "worst quality, low quality, bad anatomy, bad hands, extra digits, watermark, signature, text, black background"

### PHASE 3 - SNAPSHOT SHOOTOUT (12 images):
For each of 4 snapshots (epochs 4,6,8,10), 3 jobs:
A: "portrait, upper body, looking at viewer, neutral expression"
B: "portrait, upper body, looking at viewer, laughing, open mouth"
C: "full body, standing, front view, smile, hand on hip"

### PHASE 4 - FULL SWEEP (with chosen snapshot):
4A: 33 emotions with Danbooru helper tags
4B: 18 direction/pose combos (6 directions x 3 poses)
4C: 10 stress combos

### PHASE 5 - RESULTS CHECKLIST:
Create madie_sweep_results.txt with checkboxes: face[ ] hair[ ] emotion/pose[ ] anatomy[ ]
