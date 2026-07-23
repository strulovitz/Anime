# TAWRAT-DESKTOP-LINUX — THE BOOK OF THE DESKTOP (LINUX MINT 22)
Version 1.0 — 2026-07-23. This book MAY be updated, but ONLY with explicit
permission from Nir or Fable, given for that specific change. Update by
EDITING the relevant lines with a date — never by deleting whole sections,
never by creating a rival document. The QURAN always outranks this book.

## PART 1 — THE MACHINE ITSELF

HARDWARE: Desktop PC. GPU: NVIDIA RTX 5090, 32 GB VRAM (Blackwell — needs
PyTorch nightly cu128, same as the laptop's RTX 5070). CPU: Intel i9.
RAM: 96 GB. This is the STRONGEST machine in the project.

⚠️ THE DISK LAW — THE MOST IMPORTANT LAW OF THIS MACHINE ⚠️
Linux Mint 22 boots from an EXTERNAL 2TB USB SSD (sda):
- sda2 = system root "/": only 93 GB total, ~47 GB free. THE SMALL
  APARTMENT. Almost nothing may be installed here.
- sda4 = /home: 1.7 TB, ~1.4 TB free. THE HUGE APARTMENT. EVERYTHING BIG
  GOES HERE: PyTorch, ComfyUI, models, venvs, caches, downloads. ALWAYS
  under /home/nir/.
- Before AND after every big download/install: run df -h /home and show it.
- The one honest exception: tiny apt system packages live on root by Linux
  design — megabytes only, and this must be said out loud when it happens.
NEVER TOUCH: sda3 (swap), nvme0n1 (internal 4TB — Windows 11, BitLocker),
sdb (external 12TB backup "EXTERNAL12"). Violating this can destroy Nir's
data and Windows. There is no valid reason to ever touch them.

SOFTWARE STATE (2026-07-23): Fresh-ish Mint 22. OpenCode + DeepSeek work
(they wrote these holy books). The AI-art stack is NOT yet installed.
THE PLAN (decided 2026-07-22/23, closed): simple Python venv, everything
in /home/nir/ai-art/ (venv, ComfyUI, models, outputs). Model: a REALISTIC
SDXL-class model — NOT an anime model — because this machine's art job is
realism (see Part 2). Old conda/docker leftovers may exist on root; they
will be inspected and cleaned during bootstrap to free the small apartment.

THIS MACHINE'S ROLE: realistic imagery (backgrounds, space, planets,
ships), TTS narration voices, upscaling, heavy batch generation. It does
NOT draw characters and does NOT train LoRAs — that is the laptop's job
(see SUHUF-LAPTOP-LINUX). Finished media goes to the Desktop Windows side
(see INJIL) for Premiere editing.

WORKING DOCTRINE: Fable (Claude) plans; DeepSeek executes one small
mission at a time, explains before acting, stops on errors, reports
verbatim. Nir is a beginner — never assume knowledge, never assume
machine state, always verify. Quality over speed.

## PART 2 — ALPHA BABES (deadline ~Aug 3, 2026 — TOP PRIORITY)

This machine paints the UNIVERSE Madie flies through: photorealistic hard
science-fiction backgrounds — real-looking stars, nebulae, exoplanet
surfaces, spaceship exteriors and interiors. The style contract of the
series: anime characters (from the laptop, Illustrious-XL + Madie LoRA
v3) composed over REALISTIC environments (from this machine) — like the
great anime films: stylized people, breathtaking real-feeling worlds.
Also planned here: TTS for narration and Madie's AI-designed voice
(warm, confident, English with Romanian accent), and upscaling of final
stills. STATUS: nothing produced yet; bootstrap of the AI stack is the
current mission.

## PART 3 — COSMIC CHRYSALIS

No work started. When the time comes, this machine will play the same
role: realistic space imagery (light-sail probes, Sagittarius A*, planet
surfaces), TTS, upscaling. Nothing begins before Madie's gift is done.

## PART 4 — MAZES & MAGES

No work started. When the time comes, this machine will generate the
realistic-fantasy environments (dungeons, landscapes) and TTS. Nothing
begins before Madie's gift is done.
