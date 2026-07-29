# Claude Fable 5 — Medusa Laser-Relay Blender Scene Mission v2 (2026-07-29)

VICTORY! 🎉 Look at that image — do you understand what you're looking at? A geometrically perfect "W." Five razor-straight segments, every bounce exactly at a drone's face, every drone tilted at its own computed angle, background drones each facing their own direction. Everything GPT failed at ten times in a row, solved on the first render — because we computed it instead of painting it. And huge credit to Sonnet: that EXR pixel-dump debugging of the Blender 5.2 compositor change was genuinely professional work. The family is proud. 😄

Now, my diagnosis of the image — three problems, all fixable with numbers:

1. The mirror discs are invisible (drones look like empty rings). This is actually physically honest, which is funny: a perfect mirror reflecting empty black space looks like... empty black space. Real problem, real-world cause. Fix: a starfield in the world background (so the mirrors have something to reflect) plus a slightly brushed mirror finish (roughness 0.03 → 0.12) so the sun paints a broad sheen across the faces.
2. The ships are out of frame. The beam enters and exits the picture anonymously. Fix: ships moved inward, camera pulled back and widened — ships now enter the frame edges cinematically, with glowing window strips so they read against black.
3. Too dark overall. Fix: stronger sun + a fill light from the camera's side, brighter flash points, and a red muzzle glow at the beam's origin.

Also, the render took 4.6 seconds — iterations are essentially free. Excellent news for us.

Here is the complete v2 mission — one paste block for Sonnet, as always:

MISSION v2: Rebuild the Medusa scene with Fable's fixes. Same rules: execute
the script between the markers in ONE execute_blender_code call; only
API-compatibility fixes allowed; report any fix.

STEP 1 — Execute the v2 script below (it rebuilds the whole scene from
scratch; the old scene is replaced).

STEP 2 — GLARE SUB-MISSION (your discovery, your implementation): re-enable
the compositor using the Blender 5.2 socket-based Glare API you discovered
(scene.compositing_node_group + interface sockets + NodeGroupOutput).
Parameters: FOG_GLOW, Threshold = 1.0, Size = 7, everything else default.
Acceptance test: render a small verification frame and check pixel
statistics — the beams must bloom softly but the frame must NOT be uniformly
blown out (mean brightness must stay well below 0.5). If it blows out again,
set scene.compositing_node_group = None and report; we ship v2 without glare.

STEP 3 — Save, then render from terminal:
    blender -b ~/medusa/medusa_scene.blend -f 1
Report the output path and any fixes made.

--- SCRIPT BEGIN ---
```python
import bpy, os, math, random
from mathutils import Vector

# ================= CONFIG v2 =================
OUT_DIR = os.path.expanduser("~/medusa")
DISC_R  = 1.1
DISC_T  = 0.18
BEAM_R  = 0.04
EMITTER = Vector((-22.0,  2.0,  0.0))    # moved inward (was -28)
V = [Vector((-14.0, 0.0,  7.0)),
     Vector(( -5.0, 0.0, -5.0)),
     Vector((  5.0, 0.0,  6.0)),
     Vector(( 14.0, 0.0, -4.0))]
TARGET = Vector(( 26.0,  4.0,  2.0))     # moved inward (was 40)

# ================= CLEAN SCENE =================
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# ================= MATERIALS =================
def emission_mat(name, color, strength):
    m = bpy.data.materials.new(name); m.use_nodes = True
    nt = m.node_tree; nt.nodes.clear()
    out = nt.nodes.new('ShaderNodeOutputMaterial')
    em  = nt.nodes.new('ShaderNodeEmission')
    em.inputs['Color'].default_value = (color[0], color[1], color[2], 1.0)
    em.inputs['Strength'].default_value = strength
    nt.links.new(em.outputs['Emission'], out.inputs['Surface'])
    return m

def pbr_mat(name, color, metallic, rough):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes.get('Principled BSDF')
    b.inputs['Base Color'].default_value = (color[0], color[1], color[2], 1.0)
    b.inputs['Metallic'].default_value = metallic
    b.inputs['Roughness'].default_value = rough
    return m

MAT_MIRROR = pbr_mat("SiC_Mirror",   (0.92, 0.94, 0.92), 1.0, 0.12)  # brushed
MAT_RING_M = pbr_mat("Ring_Medusa",  (0.45, 0.46, 0.48), 1.0, 0.45)
MAT_RING_A = pbr_mat("Ring_Alliance",(0.92, 0.92, 0.95), 0.0, 0.55)
MAT_HULL   = pbr_mat("Hull",         (0.45, 0.46, 0.48), 1.0, 0.50)
MAT_TANK   = pbr_mat("Tank_Ti",      (0.60, 0.60, 0.62), 1.0, 0.30)
MAT_BEAM   = emission_mat("Beam_Red",    (1.0, 0.05, 0.05), 25.0)
MAT_FLASH  = emission_mat("Flash_White", (1.0, 1.0, 1.0),   80.0)
MAT_MUZZLE = emission_mat("Muzzle_Red",  (1.0, 0.10, 0.05), 40.0)
MAT_WINDOW = emission_mat("Windows",     (0.7, 0.85, 1.0),   6.0)

def add(op, **kw):
    op(**kw); return bpy.context.active_object

# ================= DRONE BUILDER =================
def make_drone(name, center, normal, ring_mat):
    parts = []
    disc = add(bpy.ops.mesh.primitive_cylinder_add,
               radius=DISC_R, depth=DISC_T, vertices=64, location=(0,0,0))
    disc.name = name
    disc.data.materials.append(MAT_MIRROR)
    ring = add(bpy.ops.mesh.primitive_torus_add,
               major_radius=DISC_R+0.05, minor_radius=0.16, location=(0,0,0))
    ring.data.materials.append(ring_mat); parts.append(ring)
    for i in range(6):
        a = i * math.pi/3.0
        x, y = (DISC_R+0.10)*math.cos(a), (DISC_R+0.10)*math.sin(a)
        if i % 2 == 0:
            g = add(bpy.ops.mesh.primitive_uv_sphere_add,
                    radius=0.13, segments=16, ring_count=8, location=(x,y,0))
            g.data.materials.append(MAT_TANK)
        else:
            g = add(bpy.ops.mesh.primitive_cube_add, size=0.18, location=(x,y,0))
            g.data.materials.append(ring_mat)
        parts.append(g)
    for p in parts:
        p.parent = disc
    disc.rotation_mode = 'QUATERNION'
    disc.rotation_quaternion = normal.to_track_quat('Z', 'Y')
    disc.location = center
    return disc

# ===== HERO DRONES (law of reflection, computed) =====
path = [EMITTER] + V + [TARGET]
for i, vert in enumerate(V):
    d_in  = (vert - path[i]).normalized()
    d_out = (path[i+2] - vert).normalized()
    n = (d_out - d_in).normalized()
    make_drone("Obol_%d" % (i+1), vert - n*(DISC_T/2.0), n, MAT_RING_M)

# ================= BEAMS + FLASHES =================
for a, b in zip(path[:-1], path[1:]):
    d = b - a
    beam = add(bpy.ops.mesh.primitive_cylinder_add,
               radius=BEAM_R, depth=d.length, vertices=12,
               location=tuple((a+b)/2.0))
    beam.rotation_mode = 'QUATERNION'
    beam.rotation_quaternion = d.normalized().to_track_quat('Z', 'Y')
    beam.data.materials.append(MAT_BEAM)

for vert in V + [TARGET]:
    f = add(bpy.ops.mesh.primitive_uv_sphere_add,
            radius=0.20, segments=16, ring_count=8, location=tuple(vert))
    f.data.materials.append(MAT_FLASH)

muz = add(bpy.ops.mesh.primitive_uv_sphere_add,
          radius=0.28, segments=16, ring_count=8, location=tuple(EMITTER))
muz.data.materials.append(MAT_MUZZLE)

# ================= SHIPS (now in frame, with lit windows) ==========
att = add(bpy.ops.mesh.primitive_cube_add, size=1,
          location=tuple(EMITTER + Vector((-4.5, 0, 0))))
att.scale = (8, 1.6, 1.6); att.name = "Attacker"
att.data.materials.append(MAT_HULL)
for k in range(4):
    w = add(bpy.ops.mesh.primitive_cube_add, size=1,
            location=tuple(EMITTER + Vector((-2.0 - k*1.6, -0.85, 0.3))))
    w.scale = (0.5, 0.05, 0.12); w.data.materials.append(MAT_WINDOW)
    w.parent = att; w.matrix_parent_inverse = att.matrix_world.inverted()

tgt = add(bpy.ops.mesh.primitive_cube_add, size=1,
          location=tuple(TARGET + Vector((5.0, 1.5, 0))))
tgt.scale = (12, 3, 3.5); tgt.name = "Target_Capital"
tgt.data.materials.append(MAT_HULL)
for k in range(6):
    w = add(bpy.ops.mesh.primitive_cube_add, size=1,
            location=tuple(TARGET + Vector((1.5 + k*1.5, -0.05, 0.8))))
    w.scale = (0.6, 0.05, 0.15); w.data.materials.append(MAT_WINDOW)
    w.parent = tgt; w.matrix_parent_inverse = tgt.matrix_world.inverted()

# ===== BACKGROUND FORMATIONS =====
random.seed(7)
for i in range(10):
    pos = Vector((-18 + (i % 5)*8, 26.0, 12 + (i // 5)*9))
    n = Vector((random.uniform(-1,1), random.uniform(-0.3,0.3),
                random.uniform(-1,1))).normalized()
    make_drone("Obol_bg_%d" % i, pos, n, MAT_RING_M)
for i in range(6):
    pos = Vector((26 + (i % 3)*6, 18.0, -8 + (i // 3)*7))
    n = Vector((-1.0, -0.4, 0.1*i - 0.3)).normalized()
    make_drone("Aegis_%d" % i, pos, n, MAT_RING_A)

# ================= LIGHTS =================
sun = add(bpy.ops.object.light_add, type='SUN', location=(0, 0, 50))
sun.data.energy = 6.0
sun.rotation_euler = (math.radians(55), math.radians(-20), math.radians(30))
fill = add(bpy.ops.object.light_add, type='SUN', location=(0, -50, 10))
fill.data.energy = 1.2
fill.rotation_euler = (math.radians(78), 0.0, 0.0)   # from camera side

# ================= WORLD: STARFIELD =================
world = bpy.context.scene.world
if world is None:
    world = bpy.data.worlds.new("Space"); bpy.context.scene.world = world
world.use_nodes = True
wnt = world.node_tree; wnt.nodes.clear()
w_out = wnt.nodes.new('ShaderNodeOutputWorld')
w_bg  = wnt.nodes.new('ShaderNodeBackground')
tc    = wnt.nodes.new('ShaderNodeTexCoord')
noise = wnt.nodes.new('ShaderNodeTexNoise')
noise.inputs['Scale'].default_value = 150.0
noise.inputs['Detail'].default_value = 0.0
ramp  = wnt.nodes.new('ShaderNodeValToRGB')
ramp.color_ramp.elements[0].position = 0.795
ramp.color_ramp.elements[0].color = (0.001, 0.002, 0.005, 1.0)  # deep space
ramp.color_ramp.elements[1].position = 0.815
ramp.color_ramp.elements[1].color = (1.0, 1.0, 1.0, 1.0)        # stars
wnt.links.new(tc.outputs['Generated'], noise.inputs['Vector'])
wnt.links.new(noise.outputs['Fac'], ramp.inputs['Fac'])
wnt.links.new(ramp.outputs['Color'], w_bg.inputs['Color'])
w_bg.inputs['Strength'].default_value = 1.5
wnt.links.new(w_bg.outputs['Background'], w_out.inputs['Surface'])

# ================= CAMERA =================
cam = add(bpy.ops.object.camera_add, location=(-2, -52, 4))
cam.data.lens = 32
aim = add(bpy.ops.object.empty_add, location=(2, 0, 0.5))
con = cam.constraints.new('TRACK_TO'); con.target = aim
bpy.context.scene.camera = cam

# ================= RENDER SETTINGS =================
scn = bpy.context.scene
scn.render.engine = 'CYCLES'
scn.cycles.samples = 128
scn.render.resolution_x = 1920
scn.render.resolution_y = 1080
scn.render.image_settings.file_format = 'PNG'
scn.render.filepath = os.path.join(OUT_DIR, "medusa_render_v2_")
scn.compositing_node_group = None   # Sonnet re-enables glare in STEP 2

os.makedirs(OUT_DIR, exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT_DIR, "medusa_scene.blend"))
print("SCENE v2 BUILT OK")
```
--- SCRIPT END ---

What changed and why, in one breath: stars give the mirrors a universe to reflect ✦ brushed finish catches the sun ✦ ships slide into the frame edges with lit windows ✦ fill light from the camera side wakes up the whole formation ✦ red muzzle glow marks where the beam is born ✦ and Sonnet gets to finish his own compositor victory with a proper acceptance test.

Show me medusa_render_v2_0001.png when it's done — I suspect this is the one where it starts looking like a battle. ♟️✨
