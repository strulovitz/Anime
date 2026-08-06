# Alpha Babes — Premiere Assembly Instructions (Windows 11 session)
**Written by Claude Sonnet 5 on Linux, 2026-08-06, for a fresh Claude Sonnet 5 / OpenCode session running on Nir's Windows 11 dual-boot partition, to help him assemble the finished 27-scene "Madie's Gift" video in Adobe Premiere.**

This is a birthday gift video Nir built for his girlfriend Madie — a 27-scene hard-sci-fi anime saga ("Alpha Babes") where the main character is literally named Madie. Every scene now has: (1) a static square background illustration, and (2) 1-8 short "talking head" video clips of Madie's animated character reading the scene's narration, meant to appear as a small overlay in the corner of the screen (like a video-call / captain's-log window), while the full illustration fills the rest of the screen.

## 0. FIRST STEPS FOR THE WINDOWS SESSION
1. Make sure the `Anime` GitHub repo is cloned or pulled to a folder on this Windows machine (ask Nir where he wants it, or use `git clone https://github.com/strulovitz/Anime` in a sensible location like `Documents\` or `Anime\`).
2. All the files referenced below are under `AlphaBabes/` inside that repo:
   - `AlphaBabes/images/` — the 27 (well, 29, see note below) full-screen square scene illustrations, 1024×1024 PNG.
   - `AlphaBabes/hedra-clips/` — 146 small square talking-head MP4 clips (960×960, 25fps, h264 video + AAC mono audio ALREADY baked in — these already have Madie's lip-synced voice, you do NOT need to add the narration audio separately).
   - `AlphaBabes/voice-samples/` — the raw ElevenLabs narration MP3s (reference only / backup — not needed for editing since the MP4s already contain synced audio).
3. Open Adobe Premiere. Confirm with Nir the exact final resolution he wants (suggested default: **1080×1080**, 25fps, square/1:1 — matching the source material's native square aspect ratio). **CRITICAL: when creating the New Sequence, set a CUSTOM sequence with a 1:1 (square) frame size — do NOT use a standard 16:9 preset.** All the background illustrations and all the talking-head clips are perfectly square (1024×1024 and 960×960 respectively), so the whole project must be square from the start, or everything will get cropped/pillarboxed wrong.

## 1. THE CORE VISUAL CONCEPT (please read this before touching Premiere)
- **Track 1 (bottom, background):** the full-screen square scene illustration (a still PNG), shown for the ENTIRE duration of that scene (i.e., for as long as all of that scene's talking-head clips play back to back).
- **Track 2 (on top):** Madie's small talking-head clip, scaled down to roughly **35-40% of the frame size**, positioned in ONE corner — either **bottom-left** or **bottom-right** — for the duration of that one segment, then the NEXT segment's clip appears in the (possibly different) corner, and so on, until all of that scene's segments have played. Then the video cuts to the next scene's illustration+clips.
- **DO NOT CHROMA-KEY / DO NOT TRY TO REMOVE THE BLACK BACKGROUND** behind Madie in the small clips. This was decided deliberately in an earlier session: the emotion images she's animated from have a solid black background, and Luma/Chroma keying was tested and rejected (it eats her dark hair, and there's no real alpha transparency in an MP4 anyway). **Just leave the black background as-is** — it reads intentionally as a "hologram / captain's-log / comm-screen transmission" window, which fits the sci-fi tone perfectly. Optional nice-to-have (only if Nir wants extra polish, not required): add a thin rectangular "Color Matte" border behind/around the small clip to make the "screen" edges look more deliberate — but this is optional, skip it if it complicates things or if Nir doesn't want it.
- **Horizontal flip:** whenever a segment's clip is placed in the bottom-RIGHT corner, flip it horizontally (Effect Controls > Motion > Scale, set the horizontal Scale value to a NEGATIVE number, e.g. -40 instead of 40 — this flips the clip left-right while keeping it in the corner). This is so Madie's gaze/body orientation still reads as "looking into" the main scene rather than looking off-screen away from it. **After flipping, check the small "MADIE" name-tag/chest-tag text is not distractingly mirrored/backwards** — if it looks bad on a given clip, it's fine to leave that one clip un-flipped; use judgement, this is a minor cosmetic detail, not a blocker.
- **Corner positions in pixel terms** (assuming a 1080×1080 sequence, small clip scaled to ~40% = ~432×432px):
  - Bottom-LEFT: roughly anchor near x=20px, y=1080-432-20=628px from top-left of frame (i.e., a small margin from the left and bottom edges).
  - Bottom-RIGHT: mirror of the above, small margin from the right and bottom edges.
  - Exact pixel placement isn't critical — just keep a consistent, small margin from the edges on every scene so it looks clean and doesn't touch the frame border.

## 2. AUDIO
- The talking-head MP4 clips in `hedra-clips/` ALREADY have the correct narration audio baked into them (AAC, 44.1kHz, mono). **Do not add the separate MP3 files from `voice-samples/` as extra audio** — that would double up the voice. Voice-samples are just a backup/reference of the raw ElevenLabs audio, already superseded by the final synced MP4s.
- Background music / songs: not part of this task — Nir will handle that separately later if at all. For now, focus purely on visuals + the narration audio already in the clips.

## 3. FILE NAMING CONVENTION (so you can find everything)
Every talking-head clip follows this exact pattern:
```
Fable-Pass-01-Scene-{NN}-{Scene-Title-With-Dashes}-Segment-{NN}.mp4
```
Example: `Fable-Pass-01-Scene-24-Peace-and-the-Price-Segment-03.mp4` = Scene 24, 3rd segment.

Background illustrations follow:
```
Scene-{NN}-{Scene-Title-With-Dashes}.png
```
Example: `Scene-24-Peace-and-the-Price.png`

## 4. ⚠️ SPECIAL CASE — Scenes 10 and 11 have TWO background images each
Both `AlphaBabes/images/` contains an original AND a "-CORRECTED" version for these two scenes:
- Scene 10: use `Scene-10-Fire-in-the-Sky-CORRECTED.png` (NOT the plain `Scene-10-Fire-in-the-Sky.png` — that's the old, superseded version, kept only for history).
- Scene 11: use `Scene-11-Taming-the-Dragon-CORRECTED.png` (NOT the plain `Scene-11-Taming-the-Dragon.png`).
The "-CORRECTED" versions reflect a physics fix Nir requested in an earlier session — always use those two, ignore the non-corrected duplicates.

## 5. MASTER SCENE TABLE — all 27 scenes, in final video order
Play scenes strictly in numeric order, 1 through 27. For each scene, the segments also play strictly in numeric order (Segment-01, Segment-02, ... up to however many that scene has).

| Scene | Title | Background PNG | # Segments | LEFT/RIGHT split |
|---|---|---|---|---|
| 01 | The Alpha in the Void | Scene-01-The-Alpha-in-the-Void.png | 5 | not documented — use general rule* |
| 02 | Awakening | Scene-02-Awakening.png | 5 | general rule* |
| 03 | The Ten | Scene-03-The-Ten.png | 5 | general rule* |
| 04 | First Footfall | Scene-04-First-Footfall.png | 5 | general rule* |
| 05 | First Life | Scene-05-First-Life.png | 5 | general rule* |
| 06 | The Whale of Ross 128b | Scene-06-The-Whale-of-Ross-128b.png | 4 | general rule* |
| 07 | The Call of Zĭrán | Scene-07-The-Call-of-Ziran.png | 5 | general rule* |
| 08 | The Tree City | Scene-08-The-Tree-City.png | 5 | general rule* |
| 09 | Tea with Elder Yùn | Scene-09-Tea-with-Elder-Yun.png | 4 | general rule* |
| 10 | Fire in the Sky | Scene-10-Fire-in-the-Sky-CORRECTED.png | 5 | general rule* |
| 11 | Taming the Dragon | Scene-11-Taming-the-Dragon-CORRECTED.png | 5 | general rule* |
| 12 | Farewell with Lanterns | Scene-12-Farewell-with-Lanterns.png | 4 | general rule* |
| 13 | Wreckage and Mercy | Scene-13-Wreckage-and-Mercy.png | 5 | general rule* |
| 14 | Laser Chess | Scene-14-Laser-Chess.png | 5 | general rule* |
| 15 | Council of Species | Scene-15-Council-of-Species.png | 4 | general rule* |
| 16 | Fall of the Overmind | Scene-16-Fall-of-the-Overmind.png | 5 | general rule* |
| 17 | The Core Revealed | Scene-17-The-Core-Revealed.png | 5 | general rule* |
| 18 | The Ondine City | Scene-18-The-Ondine-City.png | 5 | general rule* |
| 19 | The Ruins of Wolf 1061c | Scene-19-The-Ruins-of-Wolf-1061c.png | 6 | general rule* |
| 20 | The Grand Armada | Scene-20-The-Grand-Armada.png | 6 | general rule* |
| 21 | The Battle of the Staging Ground | Scene-21-The-Battle-of-the-Staging-Ground.png | 7 | general rule* |
| 22 | The Ultimatum | Scene-22-The-Ultimatum.png | 6 | **DOCUMENTED: Segments 1-3 LEFT, 4-6 RIGHT** |
| 23 | The Wager | Scene-23-The-Wager.png | 6 | **DOCUMENTED: Segments 1-3 LEFT, 4-6 RIGHT** |
| 24 | Peace and the Price | Scene-24-Peace-and-the-Price.png | 5 | **DOCUMENTED: Segments 1-2 LEFT, 3-5 RIGHT** |
| 25 | Meeting Zeus | Scene-25-Meeting-Zeus.png | 8 | **DOCUMENTED: Segments 1-4 LEFT, 5-8 RIGHT** |
| 26 | Paradise | Scene-26-Paradise.png | 8 | **DOCUMENTED: Segments 1-4 LEFT, 5-8 RIGHT** |
| 27 | Epilogue & Dedication | Scene-27-Epilogue-and-Dedication.png | 8 | Segments 1-2 LEFT, 3-5 RIGHT (narrative ending) — Segments 6-8 are the personal dedication to the real Madie (Nir's letter, read in Madie's AI voice), see special note in section 6 below for how to treat these differently if desired |

**\*General rule for undocumented scenes (1-21 except 22,23):** split roughly in half, first half of segments = bottom-LEFT, second half = bottom-RIGHT, ALWAYS splitting cleanly between segments (never mid-segment/mid-sentence). Example: a 5-segment scene → segments 1-2 LEFT, 3-5 RIGHT (or 1-3 LEFT, 4-5 RIGHT — either is fine, just be consistent and clean). **If Nir remembers the exact original left/right choice he had in mind for any of scenes 1-21, defer to what he says — this general rule is a reasonable default, not a hard requirement**, since the exact split for those scenes was decided verbally during recording and wasn't written down.

## 6. SPECIAL NOTE ON SCENE 27's DEDICATION (Segments 6, 7, 8)
Segments 1-5 of Scene 27 are the normal story ending (tree planting, Ace's salute, the "wink" from the sky, "Then let's fly") — treat exactly like every other scene (small corner clips, same style).

Segments 6-8 are different in nature: they are Nir's real, personal birthday dedication letter to the real Madie, read aloud in Madie's AI voice, split into 3 parts (this was Nir's own explicit choice — Option 3 out of 3 presented to him). These could be treated:
- (a) Exactly the same as all other segments (small corner clip, consistent with the rest of the video), OR
- (b) Given slightly more visual prominence since it's the emotional/personal climax of the whole gift (e.g., a bit larger, or centered instead of cornered, or with a gentle fade/darkening of the background image behind it).
**Ask Nir directly which he prefers before assembling Scene 27's ending** — don't decide this unilaterally. Default to option (a) for consistency if he has no strong preference.

## 7. STEP-BY-STEP WORKFLOW SUGGESTION
1. Create a new Premiere project. Create a new Sequence with custom settings: 1080×1080 (or 1024×1024), square pixel aspect ratio, 25fps (to match the source clips exactly and avoid frame-rate conversion issues), audio 44.1kHz.
2. Import all 27 background PNGs and all 146 MP4 clips into the Project panel (organize into bins/folders if helpful, e.g. one bin per scene).
3. For Scene 01: drag `Scene-01-The-Alpha-in-the-Void.png` onto Track 1 (V1). Set its duration in the timeline to equal the SUM of the durations of all 5 of Scene 01's clips (check each clip's duration in Premiere's Project panel or Properties — they vary per segment, anywhere from ~5 to ~48 seconds each across the whole project).
4. Drag Scene 01's Segment-01 clip onto Track 2 (V2), positioned at the very start of Scene 01's section, same start time as the background image. Scale it down (~35-40%) and position it bottom-left or bottom-right per the table above. Trim/butt the next segment's clip immediately after it on V2 (no gap, no overlap) — Segment-02 starts exactly when Segment-01 ends, etc.
5. Repeat for all 5 segments of Scene 01, alternating/switching corners per the table's LEFT/RIGHT split.
6. Move to Scene 02: place its background image on V1 immediately after Scene 01's image ends (back to back, no gap — the story should flow continuously scene to scene, no black gaps, unless Nir wants a transition/fade between scenes, which is a nice-to-have not a requirement). Repeat the same corner-clip process on V2 for Scene 02's segments.
7. Continue this pattern for all 27 scenes, in order.
8. Optional simple polish (only if time allows, not required): a short cross-dissolve (e.g. 0.5s) between each scene's background image and the next, for a smoother scene-to-scene transition.

## 8. EXPORT
- Export as H.264 MP4, square 1080×1080 (or whatever final resolution was chosen), matching source frame rate (25fps), reasonably high bitrate/quality (this is a personal one-time gift, not for broadcast — prioritize visual quality over file size).
- Ask Nir where he wants the final export saved.

## 9. WHAT NOT TO DO
- Do NOT chroma-key or Luma-key the black background out of the small talking-head clips (rejected in an earlier session, doesn't work, not needed).
- Do NOT use the non-"-CORRECTED" versions of Scene 10 or Scene 11's background images.
- Do NOT add the `voice-samples/` MP3s as extra audio — the MP4 clips already have the correct synced audio.
- Do NOT stretch/crop the square images or clips into a 16:9 frame — everything must stay 1:1 square, from the sequence settings all the way to final export.

## 10. IF ANYTHING IS UNCLEAR
Just ask Nir directly in plain conversational text (no multiple-choice quizzes — he dislikes those). He has been extremely hands-on and detail-oriented throughout this whole project and is happy to clarify anything about the story, the emotional intent of a scene, or a specific creative choice.

Good luck — this is the final assembly step of a truly massive, heartfelt project. Nir has poured an enormous amount of care into this gift for Madie. 💖🚀
