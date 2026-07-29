# Claude Fable 5 — Medusa Laser-Relay Blender Scene Mission v3 (2026-07-29)

Excellent notes — all three are exactly what a director should be catching. :-) And a fun fact before the fix: the missing star reflections are my fault via the brushed finish — I set the mirror roughness to 0.12, which smears tiny star-points into invisible blur. Your "fake it" instinct is precisely what real VFX studios do: painted-on star glints, only where the camera looks. We'll fake honestly. 😄

What v3 changes:

1. Stars: fewer (higher threshold), dimmer (gray instead of white, lower strength) — a gentle deep-space dust instead of a disco.
2. Fake star glints: background drones whose mirror faces are turned toward the camera (and only drones not touched by the laser, per your rule) get a sprinkle of tiny emissive star-dots sitting on the mirror face — reads exactly like a reflected starfield.
3. Real ships instead of boxes: the attacker becomes a proper warship — cylindrical hull, nose cone, engine block with blue-glowing nozzles, and a turret with a cannon barrel aimed exactly along the first beam segment (computed, of course). The target becomes a capital ship — hull, forward section, bridge tower, lit windows — exploding at the exact impact point: white-hot core, orange fireball shells, dark-red outer flames, and a debris cloud of tumbling hull fragments. All primitives, but composed — exactly the "good basis" GPT 5.4 needs for the beautify pass later. That's the plan: Blender gives the truth, GPT gives the skin.

One paste block for Sonnet:

MISSION v3: Rebuild the Medusa scene with ships, explosion, and star fixes.
Same rules: ONE execute_blender_code call for the script between the markers;
only API-compatibility fixes allowed; report every fix.

STEP 1 — Execute the v3 script below (full rebuild, replaces the scene).

STEP 2 — GLARE: if your v2 socket-based glare node group passed its
acceptance test back then, re-apply the identical setup now (FOG_GLOW,
Threshold 1.0, Size 7) and re-run the same acceptance check (soft bloom on
beams, mean brightness well below 0.5). If it failed in v2 or fails now, set
scene.compositing_node_group = None and report.

STEP 3 — Save and render from terminal:
    blender -b ~/medusa/medusa_scene.blend -f 1
Report output path + fixes.

--- SCRIPT BEGIN ---
```python
import bpy, os, math, random
from mathutils import Vector

# ================= CONFIG v3 =================
OUT_DIR = os.path.expanduser("~/medusa")
DISC_R  = 1.1
DISC_T  = 0.18
BEAM_R  = 0.04
EMITTER = Vector((-22.0,  2.0,  0.0))
V = [Vector((-14.0, 0.0,  7.0)),
     Vector(( -5.0, 0.0, -5.0)),
     Vector((  5.0, 0.0,  6.0)),
     Vector(( 14.0, 0.0, -4.0))]
TARGET = Vector(( 26.0,  4.0,  2.0))
random.seed(11)

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

MAT_MIRROR  = pbr_mat("SiC_Mirror",   (0.92, 0.94, 0.92), 1.0, 0.12)
MAT_RING_M  = pbr_mat("Ring_Medusa",  (0.45, 0.46, 0.48), 1.0, 0.45)
MAT_RING_A  = pbr_mat("Ring_Alliance",(0.92, 0.92, 0.95), 0.0, 0.55)
MAT_HULL    = pbr_mat("Hull",         (0.45, 0.46, 0.48), 1.0, 0.50)
MAT_HULL_D  = pbr_mat("Hull_Dark",    (0.30, 0.30, 0.33), 1.0, 0.60)
MAT_TANK    = pbr_mat("Tank_Ti",      (0.60, 0.60, 0.62), 1.0, 0.30)
MAT_BEAM    = emission_mat("Beam_Red",     (1.0, 0.05, 0.05), 25.0)
MAT_FLASH   = emission_mat("Flash_White",  (1.0, 1.0, 1.0),   80.0)
MAT_MUZZLE  = emission_mat("Muzzle_Red",   (1.0, 0.10, 0.05), 40.0)
MAT_WINDOW  = emission_mat("Windows",      (0.7, 0.85, 1.0),   6.0)
MAT_ENGINE  = emission_mat("Engine_Blue",  (0.3, 0.6, 1.0),   12.0)
MAT_STARDOT = emission_mat("Star_Glint",   (1.0, 1.0, 1.0),    3.0)
MAT_EXP_CORE= emission_mat("Exp_Core",     (1.0, 0.95, 0.7),  60.0)
MAT_EXP_MID = emission_mat("Exp_Mid",      (1.0, 0.35, 0.05), 25.0)
MAT_EXP_OUT = emission_mat("Exp_Outer",    (0.8, 0.08, 0.02),  8.0)

def add(op, **kw):
    op(**kw); return bpy.context.active_object

# ================= DRONE BUILDER =================
def make_drone(name, center, normal, ring_mat, fake_stars=False):
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
    if fake_stars:   # painted-on star glints, VFX-style
        for j in range(7):
            ang = random.uniform(0, 2*math.pi)
            r   = random.uniform(0.15, 0.85) * DISC_R
            s = add(bpy.ops.mesh.primitive_uv_sphere_add,
                    radius=random.uniform(0.015, 0.035), segments=8, ring_count=4,
                    location=(r*math.cos(ang), r*math.sin(ang), DISC_T/2 + 0.02))
            s.data.materials.append(MAT_STARDOT); parts.append(s)
    for p in parts:
        p.parent = disc
    disc.rotation_mode = 'QUATERNION'
    disc.rotation_quaternion = normal.to_track_quat('Z', 'Y')
    disc.location = center
    return disc

# ===== HERO DRONES (no fake stars — the laser is their jewelry) =====
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
for vert in V:   # bounce flashes only; the impact gets a real explosion now
    f = add(bpy.ops.mesh.primitive_uv_sphere_add,
            radius=0.20, segments=16, ring_count=8, location=tuple(vert))
    f.data.materials.append(MAT_FLASH)

# ================= ATTACKER WARSHIP =================
aim_dir = (V[0] - EMITTER).normalized()
hull = add(bpy.ops.mesh.primitive_cylinder_add, radius=1.0, depth=8.0,
           location=tuple(EMITTER + Vector((-6.0, 0, -1.0))))
hull.rotation_euler = (0, math.pi/2, 0); hull.name = "Attacker"
hull.data.materials.append(MAT_HULL)
nose = add(bpy.ops.mesh.primitive_cone_add, radius1=1.0, depth=2.4,
           location=tuple(EMITTER + Vector((-0.8, 0, -1.0))))
nose.rotation_euler = (0, math.pi/2, 0); nose.data.materials.append(MAT_HULL)
eng = add(bpy.ops.mesh.primitive_cylinder_add, radius=1.15, depth=1.2,
          location=tuple(EMITTER + Vector((-10.6, 0, -1.0))))
eng.rotation_euler = (0, math.pi/2, 0); eng.data.materials.append(MAT_HULL_D)
for k in range(3):
    nz = add(bpy.ops.mesh.primitive_cone_add, radius1=0.35, depth=0.7,
             location=tuple(EMITTER + Vector((-11.5, -0.65 + 0.65*k, -1.0))))
    nz.rotation_euler = (0, -math.pi/2, 0); nz.data.materials.append(MAT_ENGINE)
    nz.parent = hull; nz.matrix_parent_inverse = hull.matrix_world.inverted()
turret = add(bpy.ops.mesh.primitive_cube_add, size=0.9,
             location=tuple(EMITTER - aim_dir*2.4))
turret.data.materials.append(MAT_HULL_D)
barrel = add(bpy.ops.mesh.primitive_cylinder_add, radius=0.11, depth=2.2,
             vertices=16, location=tuple(EMITTER - aim_dir*1.1))
barrel.rotation_mode = 'QUATERNION'
barrel.rotation_quaternion = aim_dir.to_track_quat('Z', 'Y')
barrel.data.materials.append(MAT_HULL_D)
for o in (nose, eng, turret, barrel):
    o.parent = hull; o.matrix_parent_inverse = hull.matrix_world.inverted()
for k in range(4):
    w = add(bpy.ops.mesh.primitive_cube_add, size=1,
            location=tuple(EMITTER + Vector((-3.5 - k*1.6, -1.02, -0.7))))
    w.scale = (0.5, 0.05, 0.12); w.data.materials.append(MAT_WINDOW)
    w.parent = hull; w.matrix_parent_inverse = hull.matrix_world.inverted()
muz = add(bpy.ops.mesh.primitive_uv_sphere_add, radius=0.28,
          segments=16, ring_count=8, location=tuple(EMITTER))
muz.data.materials.append(MAT_MUZZLE)

# ================= TARGET CAPITAL SHIP + EXPLOSION =================
chull = add(bpy.ops.mesh.primitive_cube_add, size=1,
            location=tuple(TARGET + Vector((7.0, 1.5, 0))))
chull.scale = (11, 2.6, 2.6); chull.name = "Target_Capital"
chull.data.materials.append(MAT_HULL)
fwd = add(bpy.ops.mesh.primitive_cylinder_add, radius=1.8, depth=4.5,
          location=tuple(TARGET + Vector((0.8, 1.5, 0))))
fwd.rotation_euler = (0, math.pi/2, 0); fwd.data.materials.append(MAT_HULL)
bridge = add(bpy.ops.mesh.primitive_cube_add, size=1,
             location=tuple(TARGET + Vector((8.5, 1.5, 3.0))))
bridge.scale = (1.6, 1.2, 2.0); bridge.data.materials.append(MAT_HULL_D)
for o in (fwd, bridge):
    o.parent = chull; o.matrix_parent_inverse = chull.matrix_world.inverted()
for k in range(6):
    w = add(bpy.ops.mesh.primitive_cube_add, size=1,
            location=tuple(TARGET + Vector((3.0 + k*1.5, -1.12, 0.8))))
    w.scale = (0.6, 0.05, 0.15); w.data.materials.append(MAT_WINDOW)
    w.parent = chull; w.matrix_parent_inverse = chull.matrix_world.inverted()

# --- the explosion, at the exact impact point ---
core = add(bpy.ops.mesh.primitive_uv_sphere_add, radius=0.5,
           segments=16, ring_count=8, location=tuple(TARGET))
core.data.materials.append(MAT_EXP_CORE)
for j in range(5):
    off = Vector((random.uniform(-0.8, 0.4), random.uniform(-0.8, 0.3),
                  random.uniform(-0.6, 0.8)))
    b = add(bpy.ops.mesh.primitive_uv_sphere_add,
            radius=random.uniform(0.3, 0.6), segments=12, ring_count=6,
            location=tuple(TARGET + off))
    b.data.materials.append(MAT_EXP_MID)
for j in range(6):
    off = Vector((random.uniform(-1.6, 0.6), random.uniform(-1.6, 0.6),
                  random.uniform(-1.2, 1.6)))
    b = add(bpy.ops.mesh.primitive_uv_sphere_add,
            radius=random.uniform(0.4, 0.9), segments=12, ring_count=6,
            location=tuple(TARGET + off))
    b.data.materials.append(MAT_EXP_OUT)
for j in range(12):   # tumbling debris
    off = Vector((random.uniform(-3, 1.5), random.uniform(-3, 1.5),
                  random.uniform(-2.5, 2.5)))
    if off.length < 1.2: off = off.normalized() * 1.8
    d = add(bpy.ops.mesh.primitive_cube_add,
            size=random.uniform(0.10, 0.25), location=tuple(TARGET + off))
    d.rotation_euler = (random.uniform(0, 3.1), random.uniform(0, 3.1),
                        random.uniform(0, 3.1))
    d.data.materials.append(MAT_HULL_D)

# ===== BACKGROUND FORMATIONS (fake star glints if facing camera) =====
for i in range(10):
    pos = Vector((-18 + (i % 5)*8, 26.0, 12 + (i // 5)*9))
    n = Vector((random.uniform(-1,1), random.uniform(-0.3,0.3),
                random.uniform(-1,1))).normalized()
    make_drone("Obol_bg_%d" % i, pos, n, MAT_RING_M, fake_stars=(n.y < -0.15))
for i in range(6):
    pos = Vector((26 + (i % 3)*6, 18.0, -8 + (i // 3)*7))
    n = Vector((-1.0, -0.4, 0.1*i - 0.3)).normalized()
    make_drone("Aegis_%d" % i, pos, n, MAT_RING_A, fake_stars=True)

# ================= LIGHTS =================
sun = add(bpy.ops.object.light_add, type='SUN', location=(0, 0, 50))
sun.data.energy = 6.0
sun.rotation_euler = (math.radians(55), math.radians(-20), math.radians(30))
fill = add(bpy.ops.object.light_add, type='SUN', location=(0, -50, 10))
fill.data.energy = 1.2
fill.rotation_euler = (math.radians(78), 0.0, 0.0)

# ================= WORLD: GENTLER, SPARSER STARS =================
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
ramp.color_ramp.elements[0].position = 0.845          # fewer stars
ramp.color_ramp.elements[0].color = (0.001, 0.002, 0.005, 1.0)
ramp.color_ramp.elements[1].position = 0.862
ramp.color_ramp.elements[1].color = (0.55, 0.55, 0.62, 1.0)   # dimmer stars
wnt.links.new(tc.outputs['Generated'], noise.inputs['Vector'])
wnt.links.new(noise.outputs['Fac'], ramp.inputs['Fac'])
wnt.links.new(ramp.outputs['Color'], w_bg.inputs['Color'])
w_bg.inputs['Strength'].default_value = 1.0
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
scn.render.filepath = os.path.join(OUT_DIR, "medusa_render_v3_")
scn.compositing_node_group = None   # Sonnet handles glare in STEP 2

os.makedirs(OUT_DIR, exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT_DIR, "medusa_scene.blend"))
print("SCENE v3 BUILT OK")
```
--- SCRIPT END ---

Details worth noticing when you orbit the scene in your Blender window: the cannon barrel isn't decorative — its axis is computed from d̂=|V1​−E|/(V1​−E), the same vector as the first beam segment, so the laser visibly comes out of the gun. And the explosion sits at the exact point where the last segment terminates on the capital ship's hull. Cause and effect, end to end: cannon → four mirrors → fireball. ♟️🔥

Show me medusa_render_v3_0001.png — if the composition sings, the next step is feeding it to GPT 5.4 Image 2 as the geometric skeleton for the photoreal pass, and I'll write that prompt to explicitly preserve every beam angle.
