# Hedra Lipsync Pipeline — Progress Status (2026-08-02 night)

## HOW WE DO THIS (the workflow, locked):
1. Nir generates an ElevenLabs narration segment MP3 for the current scene/segment number.
2. Nir says "i saved it" or just pastes the raw downloaded filename from `~/Downloads/`.
3. Sonnet finds it in `~/Downloads/`, confirms which Scene+Segment it is (asking Nir "This is Scene X Segment Y, right?" if not obvious from sequence), then:
   - Copies it to `AlphaBabes/voice-samples/Fable-Pass-01-Scene-{NN}-{Scene-Title}-Segment-{NN}.mp3` in the repo
   - Renames the original file in `~/Downloads/` to match the same convention (kept as local backup)
   - `git add` + commit + push immediately
4. Nir feeds that MP3 + a Madie emotion image into Hedra (via OpenArt) to generate a talking-head clip.
5. Nir pastes the raw OpenArt-generated filename (e.g. `openart-XXXX....mp4`).
6. Sonnet finds it in `~/Downloads/`, renames to `AlphaBabes/hedra-clips/Fable-Pass-01-Scene-{NN}-{Scene-Title}-Segment-{NN}.mp4`, copies to repo, renames Downloads copy too, commits + pushes.
7. Repeat until Nir says a scene is complete (segment counts vary per scene — Nir tells us when the last one is done, e.g. "scene 6 only had 4 segments").
8. NEVER assume scene/segment numbers — always confirm with Nir when starting a new scene. Within a scene, segments are assumed sequential unless Nir says otherwise.

## PROGRESS SO FAR (last updated 2026-08-04 night Israel time):

ALL PUSHED TO GITHUB, working tree clean, nothing pending.

| Scene | Segments Done (MP3+MP4) | Status |
|---|---|---|
| 1 — The Alpha in the Void | 5 / 5 | ✅ COMPLETE |
| 2 — Awakening | 5 / 5 | ✅ COMPLETE |
| 3 — The Ten | 5 / 5 | ✅ COMPLETE |
| 4 — First Footfall | 5 / 5 | ✅ COMPLETE |
| 5 — First Life | 5 / 5 | ✅ COMPLETE |
| 6 — The Whale of Ross 128b | 4 / 4 | ✅ COMPLETE (this scene only has 4 segments) |
| 7 — The Call of Ziran | 5 / 5 | ✅ COMPLETE |
| 8 — The Tree City | 5 / 5 | ✅ COMPLETE |
| 9 — Tea with Elder Yun | 4 / 4 | ✅ COMPLETE |
| 10 — Fire in the Sky (CORRECTED physics) | 5 / 5 | ✅ COMPLETE |
| 11 — Taming the Dragon (CORRECTED physics) | 5 / 5 | ✅ COMPLETE |
| 12 — Farewell with Lanterns | 4 / 4 | ✅ COMPLETE |
| 13 — Wreckage and Mercy | 5 / 5 | ✅ COMPLETE |
| 14 — Laser Chess | 5 / 5 | ✅ COMPLETE |
| 15 — Council of Species | 4 / 4 | ✅ COMPLETE |
| 16 — Fall of the Overmind | 5 / 5 | ✅ COMPLETE |
| 17 — The Core Revealed | 5 / 5 | ✅ COMPLETE |
| 18 — The Ondine City (NEW grief-canon narration) | 5 / 5 | ✅ COMPLETE |
| 19 — The Ruins of Wolf 1061c | 6 / 6 | ✅ COMPLETE (this scene had 6 segments) |
| 20 — The Grand Armada | 6 / 6 | ✅ COMPLETE (this scene had 6 segments) |
| 21-27 | 0 | ⬜ NOT STARTED |

Total Hedra clips made so far: 113 (across scenes 1-20, all complete)

## WHAT'S LEFT TO DO:
1. Do Scenes 20 through 27 the same way, segment by segment (segment counts vary per scene, typically 4-6, always confirmed by Nir).
2. IMPORTANT — raise with Nir before continuing: Scenes 20-27's existing narration text (in the Batch 04/05/06 .md files) was written BEFORE the new grief-canon (see AlphaBabes/NEW-CANON-Alien-Cultures-Attitude-Toward-AI-Stages-of-Grief-2026-08-04.md) existed. These scenes involve the Titanites, Aerians, and the Dominion directly (Grand Armada, Battle of the Staging Ground, Ultimatum, Wager, Peace and the Price, Meeting Zeus). They likely need the same narration-rewrite treatment Scene 18 got, to stay consistent with the new canon, before recording ElevenLabs audio. Ask Nir if he wants to request that rewrite from Fable in one batch before continuing the pipeline.
3. Once ALL scenes have their Hedra clips: assemble everything in Premiere — full scene illustration as background, Madie's small clip (~35-40% scale) bottom-left for first half of a scene's segments then "jumps" to bottom-right for the rest (split only between segments, never mid-segment). Flip her clip horizontally when in bottom-right (check her chest tag doesn't look bad mirrored).
4. Separately (paused, low priority, per Nir's explicit "stop" from earlier tonight): the Madie flipped-emotion-image "MADIE" chest-tag mirror-text fix is UNRESOLVED and PAUSED. Do not resume without Nir's explicit go-ahead. See AGENTS.md for full details of what was tried and rejected.
5. Long-standing pending items (not urgent): entity images #60-116 on hold, ComfyUI/WAN2.2/Windows software setup, Mazes & Mages songs.

## BOOT SEQUENCE FOR TOMORROW (2026-08-05):
1. Read AGENTS.md (full context, rules, this session's summary)
2. `git -C /home/nir/Anime pull`
3. Greet Nir simply, confirm: Scenes 1-19 are 100% complete (101 Hedra clips total), next up is Scene 20 (The Grand Armada).
4. Before starting Scene 20, raise point #2 above with Nir (whether Scenes 20-27 narration needs a Fable rewrite pass for grief-canon consistency) rather than silently jumping into recording.
5. Continue the exact workflow above — find file in `~/Downloads/`, confirm scene/segment with Nir, rename+copy+push for both MP3 and MP4 steps.
6. Do NOT resume the Madie chest-tag mirror-text fix work unless Nir explicitly asks.
