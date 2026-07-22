# MADIE LORA RECIPE — PROVEN 2026-07-22
**Status:** LoRA Trial — PASS. Ready for production.

---

WINNING FILE:
- chara_madie_v1.safetensors (epoch 10)
- Backup: ~/Anime/media/backups/madie_lora_v1/
- Runner-up spare: chara_madie_v1-000008.safetensors (epoch 8)

---

TRAINING RECIPE:
- Base model: Illustrious-XL-v0.1
- Images: 36 PNGs, 1024x1024 RGB
- Tool: kohya sd-scripts (git clone main branch)
- Network: LoRA, dim=32, alpha=16
- Batch size: 4
- Epochs: 10 (~900 optimizer steps)
- Learning rate: 1e-4 (text encoder: 5e-5)
- Scheduler: cosine, warmup 50 steps
- Optimizer: AdamW
- Mixed precision: bf16 (save bf16)
- min_snr_gamma: 5
- shuffle_caption: on
- keep_tokens: 2
- seed: 42
- Training time: ~37 minutes on RTX 5090
- Final avg loss: ~0.068

---

CAPTION RECIPE:
- Format: chara_madie, <emotion>, <WD14 tags>
- WD14 tagger: SmilingWolf/wd-swinv2-tagger-v3, ONNX, thresh 0.35
- Identity tags PRUNED: hair color, eye color, lips, bangs, ponytail, braid, hair bun, sidelocks, breasts
- Tags REMOVED: astronaut, american flag, japanese flag, realistic
- Tag ADDED: black background (on every caption)
- Emotion tag derived from filename (e.g. madie-laughing.png → "laughing")

---

GENERATION SETTINGS (PROVEN):
- LoRA strength: 1.0 (both model and clip)
- Positive template: "masterpiece, best quality, chara_madie, 1girl, solo, mature female, young woman, spacesuit, no headwear, <TAGS>, simple background, grey background"
- Negative template: "worst quality, low quality, bad anatomy, bad hands, extra digits, watermark, signature, text, black background, helmet, space helmet, headwear, hood, hat, hair ornament, child, chibi, loli, aged down, deformed, large head"
- CFG: 4.5
- Sampler: euler_ancestral
- Two-pass pipeline:
  - Pass 1: 40 steps, denoise 1.0
  - Upscale: LatentUpscaleBy 1.5x (bislerp)
  - Pass 2: 20 steps, denoise 0.45
- Canvas: portraits 1024x1024 base → ~1536x1536, full-body 832x1216 base → ~1248x1824
- Seed: 123456789 (fixed for testing; vary for final production images)

---

KNOWN WEAK POINTS:
- Tiny insignia (Romania flag patch, name tag) need a detailer/inpaint pass for close-ups
- Left profile + from-behind angles are the dataset's thin side — support with IP-Adapter/ControlNet when needed
- Only 3 body angles in dataset (front, back, right side) — left-facing angles may be weaker