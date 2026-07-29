# Sonnet — Medusa Blender Scene v5.2 Report: Split Beam/Scene Passes (2026-07-29)

Mission source: `AlphaBabes/Fable-Medusa-Blender-Scene-Mission-v5.2-Split-Passes-2026-07-29.md`

## STEP 1 — Script execution: bug found and fixed
Ran the split-pass script in `~/medusa/medusa_scene_v5.blend`.

**First attempt printed:** `beam objects: 10 | scene objects: 788` — wrong.
Fable's script math implies 17 beam objects (8 main beam segments + 2
point-defense beams + 7 vertex flash spheres). I investigated before
proceeding rather than accepting the wrong count silently.

**Root cause (not an API-compat issue, a material-naming collision):**
Blender's `bpy.data.materials.new(name)` always creates a NEW data-block
even if a material with that name already exists — it silently appends
`.001`, `.002`, etc. Because this session had already built v1 through v5
scenes one after another without ever clearing `bpy.data.materials`, by the
time v5's script ran, the name `"Flash_White"` was already taken by an
orphaned material from an earlier build, so Blender created
`"Flash_White.005"` instead. Fable's `is_beam()` check used an exact-match
set (`{"Beam_Main", "Beam_PD", "Flash_White"}`), so it correctly matched the
beam cylinders (their material names happened to still be exact) but missed
all 7 flash spheres, misclassifying them into the "scene" pass instead of
the "beam" pass.

**Fix applied:** changed the exact-match check to `name.startswith(prefix)`
for each of the three beam material prefixes, then re-ran the split from a
freshly-reloaded copy of `medusa_scene_v5.blend` (also reset all
`hide_render` flags first, in case the earlier wrong pass left stale state).

**Corrected result:**
```
beam objects: 17 | scene objects: 781
beam object names/materials: [('Cylinder', 'Beam_Main'), ('Cylinder.001', 'Beam_Main'),
('Cylinder.002', 'Beam_Main'), ('Cylinder.003', 'Beam_Main'), ('Cylinder.004', 'Beam_Main'),
('Cylinder.005', 'Beam_Main'), ('Cylinder.006', 'Beam_Main'), ('Cylinder.007', 'Beam_Main'),
('Cylinder.009', 'Beam_PD'), ('Cylinder.011', 'Beam_PD'),
('Sphere.066', 'Flash_White.005'), ('Sphere.067', 'Flash_White.005'), ('Sphere.068', 'Flash_White.005'),
('Sphere.069', 'Flash_White.005'), ('Sphere.070', 'Flash_White.005'), ('Sphere.071', 'Flash_White.005'),
('Sphere.072', 'Flash_White.005')]
TWO PASS FILES SAVED OK (fixed)
```
17 beam objects = 8 Beam_Main + 2 Beam_PD + 7 Flash_White.005 — matches the
script's own geometry exactly (8 path segments, 2 point-defense shots, 7
bounce vertices). 781 scene objects (everything else: 43 lattice drones + 7
path drones + 4 backup drones + dreadnought parts + Alpha parts + explosion
debris + casualty wreckage + stars, etc).

Saved:
- `~/medusa/medusa_v5_scenepass.blend` (beams hidden from render)
- `~/medusa/medusa_v5_beampass.blend` (only beams visible, world background
  strength set to 0.0 for pure black)

## STEP 2 — Terminal renders (both passes, all 3 cameras)
```
blender -b ~/medusa/medusa_v5_scenepass.blend -a
blender -b ~/medusa/medusa_v5_beampass.blend -a
```
Output files (1920x1080, 128 samples, Cycles, glare compositor still active
on both passes exactly as it was in v5):
- `~/medusa/medusa_v5_scenepass_0001.png` (mean brightness 87.1/255)
- `~/medusa/medusa_v5_scenepass_0002.png` (mean brightness 90.8/255)
- `~/medusa/medusa_v5_scenepass_0003.png` (mean brightness 93.0/255)
- `~/medusa/medusa_v5_beampass_0001.png` (mean brightness 90.0/255)
- `~/medusa/medusa_v5_beampass_0002.png` (mean brightness 119.5/255)
- `~/medusa/medusa_v5_beampass_0003.png` (mean brightness 118.0/255)

Verified visually: scenepass frame 1 shows the full dreadnought, all 43+11
drones, the explosion, and the Alpha — completely clean, zero beams or
flashes anywhere. Beampass frame 1 shows only the 8 beam segments and their
white-hot bounce flashes, floating on near-black (the residual dark red is
correct bloom halo from the emission shaders, not a background light — the
world background strength was set to 0.0 as instructed).

All copied to:
- `/home/nir/Pictures/learnime/medusa_v5_{scenepass,beampass}_000{1,2,3}.png`
- `AlphaBabes/images/medusa_v5_{scenepass,beampass}_000{1,2,3}.png`

Both `.blend` files copied to the repo at:
- `AlphaBabes/blender-scenes/medusa-v5-scenepass-2026-07-29.blend`
- `AlphaBabes/blender-scenes/medusa-v5-beampass-2026-07-29.blend`

## STEP 3 — Object counts (as requested)
- Beam objects: **17** (8 main beam segments, 2 point-defense beams, 7 bounce-flash spheres)
- Scene objects (everything else): **781**

## STEP 4 — Composite script, ready and waiting
Saved Fable's screen-blend compositing script to
`AlphaBabes/blender-scenes/composite_v5_beams.py`, ready to run once Nir
returns with GPT 5.4 Image 2's repainted beamless plates. Not run yet since
no GPT plates exist.

## API/bug fixes made
One fix, fully disclosed above: switched material matching from exact-name
to prefix-match to handle Blender's automatic `.00N` suffixing on repeated
`materials.new()` calls within the same long-running session. This is a
same-session material-hygiene issue, not a Blender-version API break, but
I'm reporting it with full transparency per the mission's fix-disclosure
requirement.

## Files
- Scene passes: `AlphaBabes/blender-scenes/medusa-v5-scenepass-2026-07-29.blend`, `medusa-v5-beampass-2026-07-29.blend`
- Composite script: `AlphaBabes/blender-scenes/composite_v5_beams.py`
- Renders: `AlphaBabes/images/medusa_v5_scenepass_0001-3.png`, `medusa_v5_beampass_0001-3.png`
