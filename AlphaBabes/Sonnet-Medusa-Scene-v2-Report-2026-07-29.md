# Sonnet — Medusa Laser-Relay Blender Scene v2: Build Report (2026-07-29)

Mission source: `AlphaBabes/Fable-Medusa-Blender-Scene-Mission-v2-2026-07-29.md`

## STEP 1 — v2 script execution
Executed Fable's full v2 script in a single `execute_blender_code` call
(starfield world, brushed mirror finish, ships moved inward with lit
windows, fill light, red muzzle glow). **No API-compatibility errors this
time** — the script ran clean start to finish. No creative changes made.

Scene rebuilt from scratch as specified: 4 hero `Obol` drones (law-of-
reflection computed), 10 `Obol_bg` + 6 `Aegis` background drones, 5 beam
segments, 5 flash spheres, 1 muzzle glow sphere, Attacker ship (with 4
window strips) + Target_Capital ship (with 6 window strips), 2 sun lights
(key + fill), procedural noise-based starfield world, camera at (-2,-52,4)
with 32mm lens.

## STEP 2 — Glare sub-mission
Re-enabled the compositor using the Blender 5.2 node-group-based Glare API
discovered during v1 debugging:
- `bpy.data.node_groups.new(..., 'CompositorNodeTree')` → assign to
  `scene.compositing_node_group`
- Added an "Image" output socket via `node_group.interface.new_socket(...)`
- Wired `RenderLayers → Glare → NodeGroupOutput`

One additional API-compat fix found and applied (not in Fable's spec, a
5.2 quirk): the Glare "Type" input socket's enum identifier is the display
string `'Fog Glow'` (title case, with a space), not `'FOG_GLOW'`. Set:
`Type = 'Fog Glow'`, `Threshold = 1.0`, `Size = 7`, all other sockets left
at default, exactly as instructed.

**Acceptance test performed** (per mission spec): rendered a small 320×180
/ 32-sample verification frame first, dumped raw EXR pixel stats:
- Mean brightness (RGB combined): **0.095** — well below the 0.5 blowout
  threshold. PASS.
- Max pixel value: ~91.5 (a legitimate HDR emissive beam/flash pixel, not
  a blowout artifact — confirmed by the low overall mean).

Since the acceptance test passed, the glare compositor was kept enabled
(not disabled/set to None) for the final render.

## STEP 3 — Terminal render
`blender -b ~/medusa/medusa_scene.blend -f 1` — Cycles, CPU, 128 samples,
1920×1080. Render time: ~6 seconds.

Output: `/home/nir/medusa/medusa_render_v2_0001.png`

Final 8-bit PNG pixel stats (sanity check): min 6, max 255, mean 88.2 —
healthy range, not blown out, glare visibly softening the beams/flashes
without flattening the frame.

## Visual result
Starfield gives the mirror discs something to reflect (visible sheen on
drone faces now). Ships read clearly at both frame edges with lit window
strips. Muzzle glow marks the beam's origin at the Attacker ship. The
"W" zigzag beam path bounces cleanly through all 4 hero drones with soft
bloom at each flash point. Background Medusa (gray) and Alliance (white
ring) drone formations visible top and lower-right.

## Files
- Scene file: `~/medusa/medusa_scene.blend` (also copied to
  `AlphaBabes/blender-scenes/medusa-laser-relay-scene-v2-2026-07-29.blend`)
- Rendered PNG: `~/medusa/medusa_render_v2_0001.png` (also copied to
  `AlphaBabes/images/medusa-laser-relay-blender-v2-2026-07-29.png` and to
  `~/Pictures/learnime/medusa-laser-relay-blender-v2-2026-07-29.png`)
