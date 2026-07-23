# SUHUF-LAPTOP-LINUX — THE BOOK OF THE LAPTOP (DEBIAN 13)
Version 1.2 — 2026-07-23. v1.0/v1.1 contained an invented claim that the
LoRA was trained on real photos. THE TRUTH: everything in this project is
100% AI-made; no real photos of anyone exist in it, and never did. LAW OF
THIS BOOK: no fact may be written here without a source (Nir's words or a
live command output). Updates ONLY with explicit permission from Nir or
Fable, by editing lines with a date — never by deleting whole sections.
The QURAN always outranks this book.

## PART 1 — THE MACHINE ITSELF

HARDWARE (sources: KB 040 lspci, KB 220, Nir):
- GPU: NVIDIA GeForce RTX 5090 Max-Q Mobile, 24 GB VRAM, Blackwell
  (sm_120), 95W power cap. THE STRONGEST GPU IN THE PROJECT.
- RAM: 64 GB. Dual-boot: Debian 13 (this book) and Windows 11 (see ZABUR).

SOFTWARE STATE — FINISHED AND WORKING. Do not reinstall, do not "improve".
(sources: KB 090/220/230)
- Miniforge at ~/miniforge3 with two environments:
  - "comfyui": Python 3.12, ComfyUI 0.28.0, PyTorch 2.11.0+cu128 (the
    Blackwell sm_120 problem was solved via the cu128 path; it is now a
    stable, verified working install — do not touch it).
  - "kohya": Python 3.10, sd-scripts (LoRA training). The Python 3.10
    requirement is exactly why Miniforge lives on this machine.
- Base model: Illustrious-XL (anime-specialist SDXL-class checkpoint).
- Project git repository cloned at ~/Anime (github.com/strulovitz/Anime —
  PUBLIC). OpenCode + DeepSeek work here as the hands; Fable plans.

🌍 THE VIBE-ANIME LAW (source: Nir, 2026-07-23): everything in this
project is 100% AI-generated. The character Madie was drawn by GPT 5.4
Image 2; her voice is AI-designed from text. There are NO real photographs
of anyone in this project. Therefore the character images, the LoRA file,
the training recipes, and the prompts are PUBLIC on GitHub — on purpose —
so that anyone on Earth can generate the characters at home and create new
episodes. Sharing these materials is the heart of the project, not a risk.

THIS MACHINE'S ROLE: CHARACTERS. It draws Madie and the other crew girls
in anime style (Illustrious-XL + LoRAs) and it trains LoRAs (kohya env).
It does NOT make realistic backgrounds — that is the desktop's job (see
TAWRAT). With 24 GB VRAM it handles SDXL generation and LoRA training
comfortably.

## PART 2 — ALPHA BABES (deadline ~August 3, 2026 — TOP PRIORITY)

THE CROWN JEWEL (sources: KB 210/220/230):
- WINNING FILE: chara_madie_v1.safetensors — epoch 10, 218 MB.
- USE AT LoRA STRENGTH 1.0 (both model and clip), with Illustrious-XL.
- SPARE: the epoch 8 file of the same training run.
- Trained with the kohya env on 36 AI-generated anime images of the
  character Madie (drawn with GPT 5.4 Image 2), 1024x1024; training took
  ~37 minutes on this GPU.
- This LoRA is the single most precious digital asset of the project: back
  it up, never overwrite it, never retrain over it. It is also PUBLIC in
  the repository, per the Vibe-Anime Law. (Exact folder path: TO VERIFY in
  the next laptop session and record here with permission.)

MADIE'S CANON (must appear in every prompt/output): early-20s womanly
curvy young woman ("babes not babies"), brunette, ALWAYS in her spacesuit
with Romania flag shoulder patch and chest name tag, NEVER anything on her
head. Comfort ritual: borscht soup.

THIS MACHINE'S JOB FOR THE GIFT: generate the anime character art for the
keystone scenes of Pass 1 (about 25 scenes), for compositing over the
desktop's realistic backgrounds. Also: train LoRAs for other crew members
if needed. STATUS: LoRA done and verified; scene generation status TO
VERIFY in the next laptop session and record here.

## PART 3 — COSMIC CHRYSALIS

No work started. Future role: anime-style characters and their LoRAs for
this series. Nothing begins before Madie's gift is done.

## PART 4 — MAZES & MAGES

No work started. Future role: anime-style characters (adventurers, mages,
monsters) and their LoRAs. Nothing begins before Madie's gift is done.
