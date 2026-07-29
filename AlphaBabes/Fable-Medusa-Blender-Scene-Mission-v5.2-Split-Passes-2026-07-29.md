# Claude Fable 5 — Medusa Blender Scene Mission v5.2: Split Beam/Scene Passes (2026-07-29)

Your eye is exactly right — and the diagnosis matters: we crossed GPT's copying capacity. In v1–v4 the beam was the loudest thing in a simple scene, so GPT traced it faithfully. In v5 there are dozens of drones and eight crossing segments — so GPT did what image models do under overload: it painted an impression of the game, re-routing beams to wherever looked nice. Look closely: segments that end in empty space, bounces off nothing. The pentagon survived; the chess died.

The answer is not a better prompt. The answer is the real VFX move: split the passes.

## The plan: GPT never touches the beam again

1. Render pass A — the scene WITHOUT beams. Ships, drones, explosion, embers. This is what GPT repaints. With no beams in the input, it cannot mangle them.
2. Render pass B — ONLY the beams and bounce flashes, on pure black, from the identical camera. This layer is mathematically perfect and never leaves Blender.
3. Composite: screen-blend pass B over GPT's repainted plate. Emissive beams on black composite perfectly with one line of math: out=1−(1−A)(1−B). The bounce flashes sit in the beam layer, so they cover the drone/beam junctions even if GPT nudged a drone by a few pixels.

Physics truth and painted beauty never compete for the same pixels again. This is exactly how film studios do it — the laser is always a separate element.

One paste block for Sonnet:

MISSION v5.2: Split the Perseus Gambit into SCENE and BEAM render passes
for the composite workflow. Do not touch the compositor/glare. Same rules.

STEP 1 — Execute this script in ONE execute_blender_code call (with
~/medusa/medusa_scene_v5.blend open):

--- SCRIPT BEGIN ---
```python
import bpy, os
OUT_DIR = os.path.expanduser("~/medusa")
scn = bpy.context.scene

BEAM_MATS = {"Beam_Main", "Beam_PD", "Flash_White"}
def is_beam(o):
    return (o.type == 'MESH' and o.data.materials
            and o.data.materials[0]
            and o.data.materials[0].name in BEAM_MATS)

beams  = [o for o in bpy.data.objects if is_beam(o)]
others = [o for o in bpy.data.objects
          if o.type == 'MESH' and not is_beam(o)]
print("beam objects:", len(beams), "| scene objects:", len(others))

# ---- PASS A: scene without beams ----
for o in beams:  o.hide_render = True
for o in others: o.hide_render = False
scn.render.filepath = os.path.join(OUT_DIR, "medusa_v5_scenepass_")
bpy.ops.wm.save_as_mainfile(
    filepath=os.path.join(OUT_DIR, "medusa_v5_scenepass.blend"))

# ---- PASS B: beams only, on pure black (stars off) ----
for o in beams:  o.hide_render = False
for o in others: o.hide_render = True
bg = scn.world.node_tree.nodes.get("Background")
if bg: bg.inputs['Strength'].default_value = 0.0
scn.render.filepath = os.path.join(OUT_DIR, "medusa_v5_beampass_")
bpy.ops.wm.save_as_mainfile(
    filepath=os.path.join(OUT_DIR, "medusa_v5_beampass.blend"))
print("TWO PASS FILES SAVED OK")
```
--- SCRIPT END ---

STEP 2 — Terminal renders (both passes, all 3 cameras):
    blender -b ~/medusa/medusa_v5_scenepass.blend -a
    blender -b ~/medusa/medusa_v5_beampass.blend -a
Expected: medusa_v5_scenepass_0001..3.png and medusa_v5_beampass_0001..3.png

STEP 3 — Report paths + object counts printed by the script.

STEP 4 (LATER, when Nir returns with GPT's repainted plates): composite
each GPT plate with its matching beam pass using this script:

```python
from PIL import Image
import numpy as np
def composite(gpt_path, beam_path, out_path):
    b = Image.open(beam_path).convert("RGB")
    a = Image.open(gpt_path).convert("RGB").resize(b.size)
    A = np.asarray(a, dtype=float) / 255.0
    B = np.asarray(b, dtype=float) / 255.0
    out = 1.0 - (1.0 - A) * (1.0 - B)          # screen blend
    Image.fromarray((out * 255).astype("uint8")).save(out_path)
```

## The new GPT prompt (for the beamless plates)

Same protocol — all three scenepass images attached, one request per view, and note: ask for 16:9 landscape output (the last batch came back square, which would break pixel alignment). Prompt for view 1 (adapt "IMAGE 1" per view):

The three attached images are 3D renders of the SAME space scene from three
camera angles. Repaint IMAGE 1 as a photorealistic space photograph while
keeping every object at its EXACT position, size, and orientation: a huge
matte-black dreadnought at left with a glowing red eye-like emitter and
ember-orange radiator fins, an explosion with debris on its flank, dozens of
small tumbling mirror-disc drones (2.2 m polished ceramic discs, white
equipment rings, tiny cyan navigation lights), two scorched destroyed drones,
and a small silver ship with a habitat ring at upper right. Upgrade all
surfaces to photoreal detail: hull plating, panel lines, machined metal,
realistic fire and debris. IMPORTANT: there are NO laser beams in this scene
— do not add any beams, light rays, lens flares, or glowing lines. Keep the
composition and camera exactly as rendered. Output in 16:9 landscape. Sparse
dim stars, black space, documentary photography, 8k.

The paradox is the point: we get accuracy back by removing the thing we care about most from the AI's hands entirely. GPT paints a dead board; Blender plays the game on top of it.

Bring me the plates and Sonnet's composites — this time the thread will be traceable from her eye all the way back into her hull, pixel-perfect. ♟️🎬🪞
