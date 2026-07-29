# Sonnet — Medusa Blender Scene v5 Report: Laser Chess / 3D Khet Board (2026-07-29)

Mission source: `AlphaBabes/Fable-Medusa-Blender-Scene-Mission-v5-2026-07-29.md`

## STEP 1 — Script execution
Ran the full v5 script in a single `execute_blender_code` call.
**Result: clean run, ZERO API-compat fixes needed** — same as v4.

Printed lattice statistics (as requested):
```
LATTICE: 43 board drones placed, all verified > 2.5 m off-beam
LASER CHESS BOARD SET — v5 OK
```
So the final board has: 7 path drones (the played mirrors) + 4 backup drones
(pre-angled twins) + 43 lattice/board drones (the rest of the pieces, each
guaranteed by the script's own distance check to be >2.5 m from every beam
segment) + 2 captured/scorched drones + Medusa's dreadnought + the Alpha
(the bait) = a genuinely dense, combinatorial-looking board, not a flat
diagram.

## STEP 2 — Glare + acceptance test: **PARTIAL FAILURE — flagging honestly**
Applied the identical proven glare node group used in v1-v4
(`Type='Fog Glow'`, `Threshold=1.0`, `Size=7`). This is NOT an API-compat
issue — the node setup itself worked fine. The problem is scene brightness:

**With glare, 320x180, 32 samples, all 3 frames:**
- Frame 1 (Cam_Wide): mean 0.456 — borderline pass
- Frame 2 (Cam_MedusaSide): mean **0.980** — FAILS (threshold 0.5)
- Frame 3 (Cam_AegisSide): mean **1.710** — FAILS badly (threshold 0.5)

I diagnosed this further by re-rendering the same 3 frames with the
compositor disabled entirely (raw Cycles output, no glare at all):
- Frame 1 raw: mean 0.255
- Frame 2 raw: mean **0.538** — already over 0.5 before any glare is applied
- Frame 3 raw: mean **0.908** — already over 0.5 before any glare is applied

**Conclusion: this is not a glare-node problem, it's scene composition.**
The two close POV cameras (`Cam_MedusaSide` at (-10,-16,10) and
`Cam_AegisSide` at (40,-16,-4)) sit very close to a dense cluster of bright
emissive geometry — the iris, casualty embers, snipe beams, explosion debris,
and multiple overlapping Aegis rings/nav-lights all crowded in frame — so
the raw render is already overexposed before glare adds anything on top.
The v1-v4 glare settings themselves are still valid and were applied/saved
correctly; I did not change them, since that would be a creative change
outside my mandate (only API-compat fixes allowed). Flagging for your call
on whether v6 needs adjusted POV camera distances/angles or an exposure
tweak in the world/film settings.

Scene saved to `~/medusa/medusa_scene_v5.blend` with the glare group applied
(matches v1-v4 setup exactly).

## STEP 3 — Final render (via terminal, not MCP)
```
blender -b ~/medusa/medusa_scene_v5.blend -a
```
Rendered all 3 frames at 1920x1080, 128 samples, Cycles, with the glare
compositor active (as saved in STEP 2). Output files:
- `~/medusa/medusa_v5_view_0001.png` (Cam_Wide)
- `~/medusa/medusa_v5_view_0002.png` (Cam_MedusaSide) — visibly bright/hot per the failed acceptance test
- `~/medusa/medusa_v5_view_0003.png` (Cam_AegisSide) — visibly overexposed, background haze washes out detail, per the failed acceptance test

All copied to:
- `/home/nir/Pictures/learnime/medusa_v5_view_000{1,2,3}.png`
- `AlphaBabes/images/medusa_v5_view_000{1,2,3}.png`

The `.blend` file also copied to the repo at:
- `AlphaBabes/blender-scenes/medusa-laser-chess-v5-2026-07-29.blend`

## What the renders show
- **Frame 1 (wide shot) — reads great, no exposure issue:** The full board is
  visible: dozens of tumbling Aegis discs and rings scattered through open
  space, the dreadnought on the left with its radiator vanes and the fresh
  explosion where the beam returned, the red beam threading a genuine 3D
  zigzag through the lattice (not a flat shape at all this time), and the
  Alpha (small silver needle ship) sitting visibly on the original firing
  line on the right. This one fully delivers on the "knight's tour through a
  dense board" description.
- **Frame 2 (Medusa-side POV) — overexposed per acceptance test:** Close
  in among a thick cluster of lattice drones and beam segments crossing
  diagonally; the scene reads as a dense laser-chess cluster but is hotter/
  brighter than intended.
- **Frame 3 (Aegis-side POV) — most overexposed:** Very close to the
  dreadnought's iris/impact area; background haze is visibly blown out,
  reducing legibility of individual pieces compared to frame 1.

## API fixes made
None — script ran perfectly as written, both build and glare application.

## Recommendation for v6 (if wanted)
The wide shot (frame 1) is fully usable as-is. For frames 2/3, options for
you to choose (not applied by me, since these are creative/exposure
decisions, not compat fixes): (a) move the two POV cameras further back from
the dense cluster, (b) reduce emission strengths on MAT_EMBER/MAT_SNIPE/
MAT_EXP_CORE for those specific camera angles, or (c) add filmic/exposure
compensation in the render settings for close-up frames only.

## Files
- Scene: `AlphaBabes/blender-scenes/medusa-laser-chess-v5-2026-07-29.blend`
- Renders: `AlphaBabes/images/medusa_v5_view_0001.png`, `_0002.png`, `_0003.png`
