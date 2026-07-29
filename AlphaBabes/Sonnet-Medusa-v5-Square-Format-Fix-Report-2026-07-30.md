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
