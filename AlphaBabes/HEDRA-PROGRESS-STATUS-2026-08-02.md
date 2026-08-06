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
| 21 — The Battle of the Staging Ground | 7 / 7 | ✅ COMPLETE (this scene had 7 segments) |
| 22 — The Ultimatum (FINAL rewrite: ship-AI surrender ultimatum, Corbomite Maneuver, Pascal's Wager) | 6 / 6 | ✅ COMPLETE (this scene had 6 segments) |
| 23 — The Wager (FINAL rewrite: Pascal's Wager reasoned aloud by Medusa) | 6 / 6 | ✅ COMPLETE (this scene had 6 segments) |
| 24 — Peace and the Price | 5 / 5 | ✅ COMPLETE |
| 25 — Meeting Zeus | 0 / 8 | ⬜ NOT STARTED (EXPANDED to 8 segments 2026-08-05 night — Flatland 4D explanation + much more emotional Zeus speech; script final, see Fable-Pass-01-Scenes-25-26-27-FINAL-EXPANDED-2026-08-05.md) |
| 26 — Paradise | 0 / 8 | ⬜ NOT STARTED (EXPANDED to 8 segments 2026-08-05 night — added Gödel Closed Timelike Curves / parallel universe physics; script final, see same file above) |
| 27 — Epilogue & Dedication | 0 / ? | ⬜ NOT STARTED — DECISION LOCKED 2026-08-06: Nir chose OPTION 3 — Madie's AI voice reads his real dedication letter (AlphaBabes/THE-DEDICATION-FINAL-2026-08-01.md), split into 3 parts (A/B/C) with emotion images Love/Hope/Crying. Do NOT use Fable's old generic "Optional Segment 6" dedication text — use Nir's real letter verbatim, split into the 3 parts. The other segments of Scene 27 (1-5, the tree/salute/wink/"Then let's fly") are unchanged from Fable-Pass-01-Scene-27-FINAL-Epilogue-and-Dedication-2026-08-05.md.

Total Hedra clips made so far: 137 (across scenes 1-24, all complete)

## WHAT'S LEFT TO DO:
1. Record Scenes 24, 25, 26, 27 the same way, segment by segment. IMPORTANT: Scene 25 is now 8 segments and Scene 26 is now 8 segments (both expanded 2026-08-05 night) — use Fable-Pass-01-Scenes-25-26-27-FINAL-EXPANDED-2026-08-05.md as the script source, NOT the earlier 6-segment versions. Scene 24 is 5 segments (Fable-Pass-01-Scene-24-FINAL-Peace-and-the-Price-2026-08-05.md). Scene 27's first 5 segments are in Fable-Pass-01-Scene-27-FINAL-Epilogue-and-Dedication-2026-08-05.md — but its dedication segment(s) must use Nir's real letter (see point 2 below), NOT Fable's generic "Optional Segment 6."
2. Scene 27's dedication: Nir already chose OPTION 3 (2026-08-06) — Madie's AI voice reading his real letter in 3 parts (Part A/B/C, emotion images Love/Hope/Crying). Need to split THE-DEDICATION-FINAL-2026-08-01.md into 3 natural parts before recording those segments.
3. Once ALL 27 scenes have their Hedra clips: assemble everything in Premiere — full scene illustration as background, Madie's small clip (~35-40% scale) bottom-left for first half of a scene's segments then "jumps" to bottom-right for the rest (split only between segments, never mid-segment). Flip her clip horizontally when in bottom-right (check her chest tag doesn't look bad mirrored).
4. Separately (paused, low priority, per Nir's explicit "stop" from an earlier session): the Madie flipped-emotion-image "MADIE" chest-tag mirror-text fix is UNRESOLVED and PAUSED. Do not resume without Nir's explicit go-ahead. See AGENTS.md for full details of what was tried and rejected.
5. Long-standing pending items (not urgent): entity images #60-116 on hold, ComfyUI/WAN2.2/Windows software setup, Mazes & Mages songs.

## BOOT SEQUENCE FOR TOMORROW (2026-08-06):
1. Read AGENTS.md (full context, rules, this session's summary — check the very latest session entry)
2. `git -C /home/nir/Anime pull`
3. Greet Nir simply, confirm: Scenes 1-23 are 100% complete (132 Hedra clips total). All 27 scenes are now fully scripted/directed by Fable (including the big Scene 22/23 rewrite — universal laser-chess doctrine + HIVE canon — and the Scene 25/26/27 expansion — Flatland 4D Zeus, Gödel Closed Timelike Curves, much more emotional Zeus speech, and Nir's real dedication letter replacing Fable's generic one).
4. Ask Nir which Scene 27 dedication presentation option he wants (see point 2 above) before recording that scene.
5. Continue the exact Hedra workflow — find file in `~/Downloads/`, rename+copy+push for both MP3 and MP4 steps, no confirmation needed per segment (Nir asked not to be asked each time back on 2026-08-05).
6. Do NOT resume the Madie chest-tag mirror-text fix work unless Nir explicitly asks.
7. Next scene to record: Scene 24 (Peace and the Price), 5 segments.
