# Claude Fable 5 — Medusa Laser-Relay Blender Scene Mission (2026-07-29)

The bridge is alive — beautiful work, both of you! :-) And Sonnet 5 in OpenCode is literally my sibling, so this project is now a family business. 😄

Quick answer to Sonnet's flagged discrepancy: harmless. The key "blender" is just a local label/namespace in your config — the actual tool names come from the server itself. No change needed.

Now the main event. Below is one single paste block for OpenCode. It contains the bridge test, the complete scene script (the trapezoid relay with computed mirror angles — the math guarantees every reflection is correct and every drone faces a different direction), and the timeout-safe render procedure. Paste the whole thing to Sonnet:

## MISSION: Build the Medusa laser-relay scene in Blender via MCP. Follow steps exactly.

**STEP 0 — Bridge test:** using the blender MCP tools, create a UV sphere at
(0,0,0) with a glossy red material and take a viewport screenshot to confirm
the connection works. Then delete the test sphere.

**STEP 1 —** Execute the Python script between the SCRIPT BEGIN/END markers below
in a SINGLE execute_blender_code call (single-script strategy, do not split
it into many small tool calls). Rule: do NOT modify the script creatively.
You may ONLY fix Blender 5.2 API-compatibility errors if they occur, and you
must report every fix you made.

**STEP 2 —** Take a viewport screenshot and verify: four mirror-disc drones in a
zigzag, five straight red beam segments forming a "W" path from the attacker
ship through all four drone centers to the big target ship, a white glow
point at every bounce, background drones facing various directions.

**STEP 3 —** Render from the terminal in background mode (NOT through MCP, to
avoid the MCP timeout):
```
blender -b ~/medusa/medusa_scene.blend -f 1
```
The output will be `~/medusa/medusa_render_0001.png`. This may take a few
minutes on CPU; that is normal.

**STEP 4 —** Report: any API fixes made, script console output, and the full
path of the rendered PNG.

--- SCRIPT BEGIN ---
```python
import bpy, os, math, random
from mathutils import Vector

# ================= CONFIG (Fable edits these numbers between iterations) ==
OUT_DIR = os.path.expanduser("~/medusa")
DISC_R  = 1.1      # mirror disc radius (2.2 m diameter)
DISC_T  = 0.18     # disc thickness
BEAM_R  = 0.04     # laser beam cylinder radius
EMITTER = Vector((-28.0,  2.0,  0.0))    # attacker's beam origin
V = [Vector((-14.0, 0.0,  7.0)),         # bounce vertex, drone 1
     Vector(( -5.0, 0.0, -5.0)),         # drone 2
     Vector((  5.0, 0.0,  6.0)),         # drone 3
     Vector(( 14.0, 0.0, -4.0))]         # drone 4
TARGET = Vector(( 40.0,  4.0,  2.0))     # impact point on enemy hull

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

MAT_MIRROR = pbr_mat("SiC_Mirror",   (0.85, 0.88, 0.86), 1.0, 0.03)
MAT_RING_M = pbr_mat("Ring_Medusa",  (0.45, 0.46, 0.48), 1.0, 0.45)
MAT_RING_A = pbr_mat("Ring_Alliance",(0.92, 0.92, 0.95), 0.0, 0.55)
MAT_HULL   = pbr_mat("Hull",         (0.35, 0.36, 0.38), 1.0, 0.50)
MAT_TANK   = pbr_mat("Tank_Ti",      (0.60, 0.60, 0.62), 1.0, 0.30)
MAT_BEAM   = emission_mat("Beam_Red",    (1.0, 0.05, 0.05), 25.0)
MAT_FLASH  = emission_mat("Flash_White", (1.0, 1.0, 1.0),   80.0)

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
        if i % 2 == 0:   # spherical propellant tanks
            g = add(bpy.ops.mesh.primitive_uv_sphere_add,
                    radius=0.13, segments=16, ring_count=8, location=(x,y,0))
            g.data.materials.append(MAT_TANK)
        else:            # thruster / avionics boxes
            g = add(bpy.ops.mesh.primitive_cube_add, size=0.18, location=(x,y,0))
            g.data.materials.append(ring_mat)
        parts.append(g)
    for p in parts:
        p.parent = disc
    disc.rotation_mode = 'QUATERNION'
    disc.rotation_quaternion = normal.to_track_quat('Z', 'Y')
    disc.location = center
    return disc

# ===== HERO DRONES: mirror normal computed from law of reflection =====
path = [EMITTER] + V + [TARGET]
for i, vert in enumerate(V):
    d_in  = (vert - path[i]).normalized()
    d_out = (path[i+2] - vert).normalized()
    n = (d_out - d_in).normalized()          # angle in = angle out, guaranteed
    center = vert - n * (DISC_T/2.0)         # mirror surface touches the vertex
    make_drone("Obol_%d" % (i+1), center, n, MAT_RING_M)

# ================= BEAM SEGMENTS =================
for a, b in zip(path[:-1], path[1:]):
    d = b - a
    beam = add(bpy.ops.mesh.primitive_cylinder_add,
               radius=BEAM_R, depth=d.length, vertices=12,
               location=tuple((a+b)/2.0))
    beam.rotation_mode = 'QUATERNION'
    beam.rotation_quaternion = d.normalized().to_track_quat('Z', 'Y')
    beam.data.materials.append(MAT_BEAM)

# ===== white-hot flash at every bounce + at impact =====
for vert in V + [TARGET]:
    f = add(bpy.ops.mesh.primitive_uv_sphere_add,
            radius=0.16, segments=16, ring_count=8, location=tuple(vert))
    f.data.materials.append(MAT_FLASH)

# ================= SHIPS =================
att = add(bpy.ops.mesh.primitive_cube_add, size=1,
          location=tuple(EMITTER + Vector((-3.5, 0, 0))))
att.scale = (7, 1.4, 1.4); att.name = "Attacker"
att.data.materials.append(MAT_HULL)

tgt = add(bpy.ops.mesh.primitive_cube_add, size=1,
          location=tuple(TARGET + Vector((6.0, 1.5, 0))))
tgt.scale = (14, 3, 3.5); tgt.name = "Target_Capital"
tgt.data.materials.append(MAT_HULL)

# ===== BACKGROUND FORMATIONS (every drone faces its own direction) =====
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

# ================= LIGHT + WORLD =================
sun = add(bpy.ops.object.light_add, type='SUN', location=(0, 0, 50))
sun.data.energy = 4.0
sun.rotation_euler = (math.radians(55), math.radians(-20), math.radians(30))
world = bpy.context.scene.world
if world is None:
    world = bpy.data.worlds.new("Space"); bpy.context.scene.world = world
world.use_nodes = True
bg = world.node_tree.nodes.get('Background')
bg.inputs['Color'].default_value = (0.002, 0.003, 0.006, 1.0)
bg.inputs['Strength'].default_value = 1.0

# ================= CAMERA =================
cam = add(bpy.ops.object.camera_add, location=(-2, -42, 3))
cam.data.lens = 40
aim = add(bpy.ops.object.empty_add, location=(2, 0, 1))
con = cam.constraints.new('TRACK_TO'); con.target = aim
bpy.context.scene.camera = cam

# ================= RENDER SETTINGS + GLOW =================
scn = bpy.context.scene
scn.render.engine = 'CYCLES'
scn.cycles.samples = 128
scn.render.resolution_x = 1920
scn.render.resolution_y = 1080
scn.render.image_settings.file_format = 'PNG'
scn.render.filepath = os.path.join(OUT_DIR, "medusa_render_")
scn.use_nodes = True
nt = scn.node_tree; nt.nodes.clear()
rl = nt.nodes.new('CompositorNodeRLayers')
gl = nt.nodes.new('CompositorNodeGlare')
try:
    gl.glare_type = 'FOG_GLOW'; gl.quality = 'HIGH'
    gl.threshold = 1.0; gl.size = 8
except Exception as e:
    print("Glare options changed in this version, using defaults:", e)
cmp = nt.nodes.new('CompositorNodeComposite')
nt.links.new(rl.outputs['Image'], gl.inputs['Image'])
nt.links.new(gl.outputs['Image'], cmp.inputs['Image'])

# ================= SAVE =================
os.makedirs(OUT_DIR, exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT_DIR, "medusa_scene.blend"))
print("SCENE BUILT OK — saved to ~/medusa/medusa_scene.blend")
```
--- SCRIPT END ---

What you should see with your own eyes the moment Step 1 runs: the scene materializing live in your Blender window. Feel free to orbit around it with your middle mouse button — it's your scene, in your normal Blender.

Why this cannot fail like GPT did: the beams are drawn between the bounce points, and each mirror's angle is derived from the beam directions (n̂ = (d̂_out − d̂_in) / |d̂_out − d̂_in|). The reflection isn't painted — it's solved. Wrong geometry is mathematically impossible here.

When the render finishes, look at ~/medusa/medusa_render_0001.png and tell me what you see (or describe/attach it). Then we iterate: I change only the numbers in the CONFIG block — formation shape, camera angle, beam thickness — and after it looks right, we do the GPT 5.4 photoreal beautify pass on top. ♟️🚀
