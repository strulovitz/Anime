# Session 4 — Fable's Reply: 4-Mission Plan + Mission A
**Date:** 2026-07-22 ~Afternoon
**Chat:** Claude Fable 5 (OpenRouter)

---

No worries at all, Nir — and thank you for your patience! :-) 💖 Let me quickly address your concerns, and then give you exactly what you asked for.
First — about the "getting stuck" 🛠️

I promise you Anthropic is not sabotaging OpenRouter users — there's no detection or punishment of non-Claude-Code tools. What you're seeing is almost certainly very long responses hitting timeouts or token limits on the OpenRouter side. The practical fix (without dumbing me down!) is exactly what we'll do now: I'll keep each answer to ONE mission at a time, so no single reply is huge enough to stall. Reasoning stays ON. :-)

And yes — agreed 100%: Laptop first, fully tested, then Desktop. No parallel work. And the 3×3 "target" from the old contract is not the goal anymore — your goal is the goal: full broad emotional range + all directions/poses. The 3×3 becomes just a 2-minute sanity check before the big sweep, so we don't waste GPU time if something is fundamentally broken.
The Plan — 4 Missions 🗺️

    Mission A (below, paste it now): Verify the 36 images + build the Kohya training folder. Zero-install, very safe.
    Mission B (next reply): Kohya install + WD14 captioning (trigger word chara_madie + emotion word from each filename baked into the caption — this is the secret sauce that lets us later summon each emotion by name!) + Illustrious checkpoint download.
    Mission C: Train the LoRA (~1000 steps on the 5090).
    Mission D: The Full Emotion & Direction Test Sweep — described in detail below so you know exactly where we're going.

📋 MISSION A — paste this to OpenCode on the laptop:

MISSION A: Madie LoRA - Step 1 of 4 - Dataset Verification & Kohya Folder Prep
Machine: Laptop Debian 13 (RTX 5090)

RULES FOR YOU, THE AGENT:
- Before every action, explain it in one simple sentence.
- Execute ONE step at a time. Never batch steps.
- On ANY error: STOP immediately and show the error verbatim. Do not improvise fixes.
- If anything is unclear, PAUSE and ask the user to relay the question to Fable.

STRICT WHITELIST - you may ONLY create/modify files inside:
- ~/Anime/media/lora_dataset/
You may READ (but never modify): ~/miniforge3/envs/comfyui/ (to use its python),
and ~/Anime/media/lora_dataset/madie_raw/ (never modify or delete the originals).
FORBIDDEN: NVIDIA driver, /usr/local/cuda, ~/.ssh, ~/.bashrc, conda envs,
ComfyUI, anything else on the system. No package installs in this mission.

PHASE 1 - READ-ONLY DIAGNOSTICS (no changes to anything):
Step 1.1: Run: ls -la ~/Anime/media/lora_dataset/madie_raw/
Step 1.2: Count the PNG files. Expected: exactly 36.
Step 1.3: Using the comfyui env python (~/miniforge3/envs/comfyui/bin/python)
and Pillow, print for every image: filename, width x height, mode (RGB/RGBA).
Step 1.4: Report a plain-text summary: file count, min/max resolution, any file
that is corrupt, unreadable, or suspiciously small (under 512px on any side).
THEN STOP. Print exactly: "DIAGNOSTICS DONE - type go to continue"
and WAIT for the user to type: go

PHASE 2 - BUILD TRAINING FOLDER (only after user types go):
Step 2.1: Create folder: ~/Anime/media/lora_dataset/madie_train/10_chara_madie
Step 2.2: With the comfyui env python + Pillow, for EACH of the 36 images:
- open the original from madie_raw (never modify the original),
- convert to RGB if it is RGBA,
- if the longest side is over 1024, resize so the longest side = 1024
  (keep aspect ratio, use LANCZOS); otherwise keep original size,
- save as PNG into 10_chara_madie/ with the SAME filename
  (the filenames carry the emotion names - they must be preserved exactly).
Step 2.3: Verify: exactly 36 PNGs in 10_chara_madie/, all readable, print each
filename with its new dimensions.
Step 2.4: Final report in plain text: original count, copied count, any skipped
or failed files. Print exactly: "MISSION A COMPLETE".
Do NOT start captioning, do NOT install anything, do NOT train. That is Mission B.

🎭 The Full Emotion & Direction Test Plan (this becomes Mission D)

This is the detailed answer to "how to test all the emotions and directions." After training, we generate a big sweep through ComfyUI (a script the agent will write — I'll provide it in Mission D). All images use: fixed seed, LoRA strength 0.9, CFG 4.5, ~28 steps, 1024×1024, simple background (grey) — so the ONLY thing changing between images is the emotion/pose tag. That's how we isolate and judge her range. 🔬

Phase 1 — Sanity check (9 images, ~2 min): front / three-quarter / profile × neutral / smile / angry. Just to confirm the LoRA works at all before the big run.

Phase 2 — FULL EMOTION SWEEP (33 images, front bust portrait): one image per emotion, using the emotion word from the training filenames PLUS Danbooru-style helper tags (Illustrious speaks Danbooru!). The mapping we'll use:

    neutral → neutral expression, closed mouth
    happiness → happy, smile
    sadness → sad, frown
    anger → angry, furrowed brow
    fear → scared, wide eyes, trembling
    surprise → surprised, open mouth, wide eyes
    disgust → disgust, wavy mouth
    contempt → smug, narrowed eyes, smirk
    joy → joyful, grin, sparkling eyes
    love → loving gaze, blush, heart-shaped pupils (weight 0.6)
    hate → glaring, hateful stare, shaded face
    hope → hopeful, gentle smile, looking up
    boredom → bored, half-closed eyes, cheek rest
    calmness → calm, serene, soft smile, closed eyes
    excitement → excited, open mouth smile, raised fists
    interest → curious, head tilt, bright eyes
    wonder → wonder, parted lips, wide eyes, looking up
    awe → awe, amazed, hand over mouth
    adoration → adoring gaze, sparkling eyes, hands clasped
    amusement → amused, giggling, hand over mouth
    compassion → compassionate, gentle expression, warm smile
    crying → crying, tears, tearful eyes
    embarrassment → embarrassed, full blush, averting gaze
    envy → envious, pout, side glance
    gratitude → grateful, warm smile, hand on chest
    horror → horrified, wide eyes, pale, open mouth
    laughing → laughing, open mouth, closed eyes, ^_^
    rage → enraged, clenched teeth, veins, screaming
    relaxation → relaxed, content, eyes closed, soft expression
    sensory pleasure → blissful, closed eyes, content smile
    shame → ashamed, looking down, downcast eyes
    depression → depressed, empty eyes, gloom, head down
    arousal → flustered, heavy blush, half-closed eyes

Phase 3 — DIRECTION & POSE SWEEP (~18 images, full body): with a neutral-pleasant expression held constant:

    Directions (6): front view / three-quarter view / from side, profile / from side, profile, facing left / from behind, looking back / from behind
    Each direction generated in 3 poses: standing / walking / running

⚠️ Honest expectation: her dataset has front/back/right-side only, so left profile and from-behind may be the weakest — the sweep will tell us exactly where she needs IP-Adapter/ControlNet support later.

Phase 4 — STRESS COMBOS (~10 images): emotions + motion together, e.g. walking, laughing, running, scared, three-quarter view, crying, sitting, bored, standing, arms crossed, smug — because in the actual saga she'll rarely be a front-facing portrait!

Scoring (plain-text checklist per image, saved to the repo): ① Is it instantly Madie's face? ② Hair correct (brunette, her style)? ③ Emotion clearly readable? ④ Anatomy OK? — We mark each Y/N and get a precise map of her strengths and gaps. Roughly 70 images total ≈ 10–15 minutes on the 5090. 🚀

Paste Mission A now, and when the agent prints "MISSION A COMPLETE" (or hits any error), paste me the full report — then I'll immediately hand you Mission B. One mission per reply = no more getting stuck. :-) 😍🎉
