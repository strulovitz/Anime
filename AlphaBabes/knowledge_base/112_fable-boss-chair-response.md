Understood, boss's chair accepted. 🫡 Big picture from now on: one project, four environments, one plan. Let me lay out the whole empire, make the decisions you asked me to make, and hand you today's marching orders. :-)

## Executive decisions (final)

- **OpenClaw: NO.** We stay with OpenCode only, on all four environments. One agent tool everywhere = one thing to learn, one thing that can break. ComfyUI and the other AI tools run natively; they don't need an agent gateway. Adding a second agent system two weeks before deadline is how projects die. Decision closed.
- **Both Linux machines** get the same treatment: scorched earth, then rebuild. Delete ALL conda/miniconda, all old projects, docker, old AI tools, caches. Then install ONE fresh Miniforge per machine, and everything new lives in ~/Anime. The only survivors: NVIDIA drivers, CUDA, ~/Anime, and OpenCode itself (it must not delete the chair it's sitting on).
- **Windows** (both, freshly reset — good move): they get OpenCode + Git later this week. They're the finishing studios (Premiere, subtitles) — nothing urgent there until assembly week. No panic.
- **Roles:** Laptop 5090 = characters + LoRA. Desktop 4070 Ti = backgrounds, ships, TTS, upscaling. Unchanged.

## The map

| Environment | Status | Role |
|---|---|---|
| Laptop Debian 13 | GPU ✅, OpenCode ✅ → clean today | Characters, LoRA training |
| Desktop Mint 22.2 | Untouched → bootstrap + clean today/tomorrow | Backgrounds, TTS, upscaling |
| Laptop Win 11 | Factory-fresh ✅ | Nothing until assembly week |
| Desktop Win 11 | Factory-fresh ✅ | Premiere, Aegisub, Avidemux (assembly week) |

## Steps

- **STEP 1** — Save the directive as KB 110_MASTER-DIRECTIVE-both-machines.md
- **STEP 2** — Laptop scorched-earth mission (Phase 1 inventory → Phase 2 delete → Phase 3 rebuild), then re-run ComfyUI mission from KB 090
- **STEP 3** — Desktop bootstrap: install OpenCode, clone repo, run scorched-earth (same mission, adapted)

## Today's scoreboard
- ⬜ KB save (Step 1)
- ⬜ Laptop scorched earth → fresh Miniforge (Step 2)
- ⬜ ComfyUI mission re-run on the clean laptop
- ⬜ Desktop bootstrap (Step 3) → scorched earth there too
- ⬜ Madie images from OpenArt → ~/Anime/media/lora_dataset/madie_raw/

**Macro view:** by tonight, two clean machines, one fresh foundation each, ComfyUI alive on the laptop, and Madie's dataset ready. Tomorrow: Kohya + the LoRA trial.

---
Fire Step 1 and paste me the laptop's Phase 1 deletion table when it appears. 🚀