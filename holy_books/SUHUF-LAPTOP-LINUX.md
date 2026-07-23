# SUHUF-LAPTOP-LINUX — THE BOOK OF THE LAPTOP (DEBIAN 13)
Version 1.0 — 2026-07-23. This book MAY be updated, but ONLY with explicit
permission from Nir or Fable, given for that specific change. Update by
EDITING lines with a date — never delete whole sections, never create a
rival document. The QURAN always outranks this book.
NOTE: v1.0 was written from project records while working on the desktop.
The first Fable session ON THE LAPTOP should verify exact paths/versions
and update them here (with permission).

## PART 1 — THE MACHINE ITSELF

HARDWARE: Laptop. GPU: NVIDIA RTX 5070, 8 GB VRAM (Blackwell — requires
PyTorch nightly cu128; this was discovered the hard way and must never be
forgotten). Dual-boot: Debian 13 (this book) and Windows 11 (see ZABUR).

SOFTWARE STATE: FINISHED AND WORKING — do not reinstall, do not "improve".
- Miniforge at ~/miniforge3 with two environments:
  - "anime": Python 3.11, runs ComfyUI (image generation).
  - "kohya": Python 3.10, runs kohya_ss GUI (LoRA training). The Python
    3.10 requirement is exactly why Miniforge lives on this machine.
- Model: Illustrious-XL (anime-specialist SDXL-class checkpoint).
- The project git repository is cloned at ~/Anime
  (github.com/strulovitz/Anime — PUBLIC).
- OpenCode + DeepSeek work here as the hands; Fable plans.

⚠️ PRIVACY LAW: Madie's real training photos, and any generated image of
her likeness, must NEVER be committed or pushed to the PUBLIC GitHub
repository. No exceptions. Check every git add carefully.

THIS MACHINE'S ROLE: CHARACTERS. It draws Madie and the other crew girls
in anime style (Illustrious-XL + LoRAs) and it trains LoRAs (kohya). It
does NOT make realistic backgrounds (desktop's job, see TAWRAT). With only
8 GB VRAM, it works carefully: one job at a time, modest batch sizes.

## PART 2 — ALPHA BABES (deadline ~Aug 3, 2026 — TOP PRIORITY)

THE CROWN JEWEL: Madie LoRA v3 — READY. Trained with kohya_ss on curated,
consented photos of Madie. The chosen version is epoch 6, used at LoRA
strength about 0.7–0.75 with Illustrious-XL. This LoRA is the single most
precious digital asset of the whole project: it must be backed up and
never overwritten. (Exact file path: TO VERIFY on the laptop.)

MADIE'S CANON (must appear in every prompt/output): early-20s womanly
curvy young woman ("babes not babies"), brunette, ALWAYS in her spacesuit
with Romania flag shoulder patch and chest name tag, NEVER anything on her
head. Comfort ritual: borscht soup.

THIS MACHINE'S JOB FOR THE GIFT: generate the anime character art for the
keystone scenes of Pass 1 (about 25 scenes), for compositing over the
desktop's realistic backgrounds. Also: train LoRAs for other crew members
if needed. STATUS: LoRA v3 done; scene generation status TO VERIFY on the
laptop and update here.

## PART 3 — COSMIC CHRYSALIS

No work started. Future role: anime-style characters and their LoRAs for
this series. Nothing begins before Madie's gift is done.

## PART 4 — MAZES & MAGES

No work started. Future role: anime-style characters (adventurers, mages,
monsters) and their LoRAs. Nothing begins before Madie's gift is done.
