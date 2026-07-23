# TAWRAT-DESKTOP-LINUX — THE BOOK OF THE DESKTOP (LINUX MINT 22)
Version 1.1 — 2026-07-23. v1.0 contained invented hardware facts; v1.1 is
corrected using ONLY live command outputs verified on this machine on
2026-07-23. LAW OF THIS BOOK: no fact may be written here without a source
(Nir's words or a live command output). This book MAY be updated, but ONLY
with explicit permission from Nir or Fable, by editing lines with a date —
never by deleting whole sections. The QURAN always outranks this book.

## PART 1 — THE MACHINE ITSELF

HARDWARE (verified 2026-07-23 by nvidia-smi, free -h, uname -r):
- GPU: NVIDIA GeForce RTX 4070 Ti, 12 GB VRAM. Mid-range: plan for 1024px
  base renders, FP8 where useful, tiled upscaling. NEVER plan as if this
  card has more memory. Not a Blackwell card — stable PyTorch is fine, no
  special nightly needed.
- CPU: Intel Core i9-13900KF (13th gen). RAM: 64 GB.
- OS: Linux Mint 22, kernel 7.0.0-28-generic. NVIDIA driver 595.71.05
  (Canonical-signed, factory kernel modules), CUDA 13.2.
- Note: the STRONGEST GPU of the project is in the LAPTOP (RTX 5090 Max-Q,
  24 GB — see SUHUF). This desktop is the realism workhorse, not the muscle
  champion.

⚠️ THE DISK LAW — THE MOST IMPORTANT LAW OF THIS MACHINE ⚠️
(verified 2026-07-23 by df -h / lsblk)
Linux Mint 22 boots from an EXTERNAL 2TB USB SSD (sda):
- sda2 = system root "/": 92 GB total, ~47 GB free. THE SMALL APARTMENT.
  Almost nothing may be installed here.
- sda4 = /home: 1.7 TB, ~1.4 TB free. THE HUGE APARTMENT. EVERYTHING BIG
  GOES HERE: PyTorch, ComfyUI, models, venvs, caches, downloads — always
  under /home/nir/.
- Before AND after every big download/install: run df -h /home and show it.
- The one honest exception: tiny apt system packages live on root by Linux
  design — megabytes only, and this must be said out loud when it happens.
NEVER TOUCH: sda3 (swap), nvme0n1 (internal 4 TB — Windows 11, BitLocker),
sdb (external 12 TB backup "EXTERNAL12"). Violating this can destroy Nir's
data and Windows. There is no valid reason to ever touch them.

SOFTWARE STATE (2026-07-23): OpenCode + DeepSeek work (they wrote these
holy books). The AI-art stack is NOT yet installed. THE PLAN (closed
decision): simple Python venv, everything in /home/nir/ai-art/ (venv,
ComfyUI, models, outputs). Model: a REALISTIC SDXL-class model — NOT an
anime model — because this machine's art job is realism (see Part 2).
Old conda/docker leftovers may exist on root; they will be inspected and
cleaned during bootstrap to free space in the small apartment.

THIS MACHINE'S ROLE: realistic imagery (backgrounds, space, planets,
ships), TTS narration voices, upscaling, batch generation sized for 12 GB
VRAM. It does NOT draw characters and does NOT train LoRAs — that is the
laptop's job (see SUHUF). Finished media goes to the Desktop Windows side
(see INJIL) for Premiere editing.

WORKING DOCTRINE: Fable (Claude) plans; DeepSeek executes one small
mission at a time, explains before acting, stops on errors, reports
verbatim. Nir is a beginner — never assume knowledge, never assume machine
state, always verify. Quality over speed. No fact without a source.

## PART 2 — ALPHA BABES (deadline ~August 3, 2026 — TOP PRIORITY)

This machine paints the UNIVERSE Madie flies through: photorealistic hard
science-fiction backgrounds — real-looking stars, nebulae, exoplanet
surfaces, spaceship exteriors and interiors. The style contract of the
series: anime characters (from the laptop, Illustrious-XL + Madie LoRA)
composed over REALISTIC environments (from this machine) — like the great
anime films: stylized people, breathtaking real-feeling worlds. Also
planned here: TTS for narration and Madie's AI-designed voice (warm,
confident, English with Romanian accent), and upscaling of final stills
(tiled, to respect 12 GB VRAM). STATUS: nothing produced yet; bootstrap of
the AI stack is the current mission.

## PART 3 — COSMIC CHRYSALIS

No work started. Future role: realistic space imagery (light-sail probes,
Sagittarius A*, planet surfaces), TTS, upscaling. Nothing begins before
Madie's gift is done.

## PART 4 — MAZES & MAGES

No work started. Future role: realistic-fantasy environments (dungeons,
landscapes) and TTS. Nothing begins before Madie's gift is done.
