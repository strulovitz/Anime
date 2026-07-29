# Sonnet Report: v5 Square-Format Fix — 2026-07-30

## The problem Nir caught
GPT 5.4 Image 2 **always** outputs 1024×1024 square images, regardless of what
aspect ratio we request in the prompt text ("16:9 widescreen" is ignored every
time). Our original beam-pass compositing pipeline rendered the beam layer at
1920×1080 (16:9) to match the *requested* aspect — meaning it never actually
matched what GPT produces. Nir is right: **we adapt to GPT, not the other way
around.**

## What I did

1. Confirmed all 3 GPT beamless plates are 1024×1024 PNG (verified with PIL,
   not by eyeballing).
2. Re-rendered the beam pass (`medusa_v5_beampass_sq.blend`) at native
   1024×1024 resolution, using the exact same 3 cameras (`Cam_Wide`,
   `Cam_MedusaSide`, `Cam_AegisSide`, all `sensor_fit='AUTO'`, `lens=28mm`) —
   so the camera's vertical FOV stays identical to the original 16:9 render,
   and only the horizontal FOV narrows to fill a square frame (this is the
   standard "crop the sides, keep full vertical extent" behavior of Blender's
   AUTO sensor fit when you shrink the width).
3. **First attempt (rejected):** I also tried a letterbox approach (scale the
   16:9 render to fit 1024 width, pad top/bottom with black) reasoning that
   GPT might be padding instead of cropping. Testing proved unnecessary and
   worse — GPT's own repaint doesn't add clean black bars, it just naturally
   leaves empty space at top/bottom in wide shots because the scene content
   doesn't reach that far — the native square camera crop already reproduces
   this exact same empty space, without needing any manual letterbox padding,
   and without the visible red "seam" artifact the letterbox version produced
   (the letterboxed beam pass's ambient glare glow existed *within* the
   padded content band but stopped hard at the black bar boundary — creating
   a visible rectangle in the final composite that isn't in GPT's plate).
4. Standardized on the **native square-crop beam pass for all 3 views** —
   simpler, matches GPT's actual behavior, no seam artifact.
5. Re-ran the split-pass composite (screen-blend with `crush=0.06` highlight
   correction, same recipe as before) against all 3 real GPT beamless plates.
6. Verified alignment is good but not pixel-perfect — GPT's repaint
   introduces its own small positional drift on individual drones (it's a
   generative repaint, not a literal copy), most visible as beam bounce
   points landing near-but-not-exactly on ring centers. This is an inherent
   limitation of using a generative image model for a physically precise
   layer, not a bug in the Blender math (I sanity-checked the beam pass
   against my own un-repainted scenepass render — those two align perfectly,
   confirming the Blender-side geometry/scale math is exactly correct).

## Files delivered
- `AlphaBabes/images/medusa_v5_final_0001_wide.png`
- `AlphaBabes/images/medusa_v5_final_0002_medusaside.png`
- `AlphaBabes/images/medusa_v5_final_0003_aegisside.png`
- `AlphaBabes/images/medusa_v5_beampass_square_000{1,2,3}.png` (raw square beam layers, in case Fable wants to recomposite with different settings)
- `AlphaBabes/blender-scenes/medusa_v5_beampass_sq.blend` (the corrected square-native Blender source file)

## Recommendation for future missions
Any future Blender-scene mission that will be repainted by GPT 5.4 Image 2
should render natively at **1024×1024 square** from the start (not 16:9),
using AUTO sensor fit on the same cameras, to avoid this rework.

## UPDATE: Nir caught a real problem — layers had no visual connection

Nir looked at the first delivered composites and correctly identified that the
beam layer and GPT's repainted plate looked like two unrelated images stacked
on top of each other — laser bounce points were floating in empty gaps between
drones instead of landing on actual mirror surfaces, so it didn't read as "these
specific mirrors are reflecting the laser."

### Root cause investigation
I got the exact 3D positions of all 7 laser bounce points directly from Blender
(via camera projection, `world_to_camera_view` — no pixel-guessing) and plotted
them as markers on both my raw Blender render and GPT's actual repainted image
for direct comparison.

- On my raw (un-repainted) Blender render: every single marker landed exactly
  on a real drone, confirming the Blender-side beam-bounce math is correct.
- On GPT's repainted image: the same markers consistently missed — landing in
  gaps between rings instead of on them. This is because GPT's generative
  repaint doesn't preserve exact object positions; it redraws the whole scene
  with its own interpretation, shifting things slightly.
- **View 1 (Wide):** GPT shifted the entire drone cluster by a fairly
  consistent amount (~27px left, 43px up) — a single global correction fixed
  nearly all 7 bounce points to land exactly on real rings.
- **View 2 (MedusaSide):** GPT's repaint was already well-aligned (only ~5-8px
  drift) — small correction applied.
- **View 3 (AegisSide):** GPT's drift was less consistent per-drone (each ring
  shifted independently rather than as one rigid group) — averaged the drift
  across 4 measurable points for a best-effort global correction; not as
  perfect as View 1 but noticeably improved.

### Fix applied
Shifted the beam-pass layer by a per-view pixel offset (computed from real
landmark measurements, not guessed) before compositing:
- View 1: shift (-27, -43)
- View 2: shift (-5, +8)
- View 3: shift (+13, -1)

Re-verified visually after each shift — bounce points now land on or very near
real rings in all 3 views instead of floating in empty space.

### Known remaining limitation
This is a translation-only fix (rigid shift), not a per-object correction.
Since GPT's drift isn't perfectly uniform (especially in View 3), a few
individual bounce points still don't land pixel-perfectly on a ring, though
all are now dramatically closer than before. A fully pixel-perfect result
would require either GPT preserving exact object coordinates (it doesn't) or
a per-drone manual warp (labor-intensive, not attempted here).

## Updated files delivered (replacing earlier versions)
- `AlphaBabes/images/medusa_v5_final_0001_wide.png`
- `AlphaBabes/images/medusa_v5_final_0002_medusaside.png`
- `AlphaBabes/images/medusa_v5_final_0003_aegisside.png`
- Also copied to `/home/nir/Pictures/learnime/` for direct viewing.
