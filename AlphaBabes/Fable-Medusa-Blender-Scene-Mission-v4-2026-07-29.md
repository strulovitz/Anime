# Claude Fable 5 — Medusa Laser-Relay Blender Scene Mission v4: The Perseus Gambit (2026-07-29)

WHAT A FIND!!! 🤩 You had the perfect scene sitting in your own canon the whole time — and it's better than anything I proposed. The Aegis Array / Perseus Gambit is the mythologically correct answer: Medusa fires her colossal eye-beam, and the good guys don't shoot back — they hold up the mirror. The hunter petrified by her own gaze. (And written with o1 Pro — that's practically archaeology now. 😄 The story held up.)

One important design decision before the script, because it changes your earlier request: the beam stays RED. Not because I'm lazy — because it's canon and it's the whole point: red = Medusa, and in this scene the good guys' weapon is Medusa's own red beam, caught and bent back into her. The good guys' identity shows in everything else: white ceramic rings, cyan navigation lights, disciplined formation, and the Alpha watching from the deep background. (If you still want a cyan beam scene, canon gives us one for free: the Aegis Array's alignment test, where the coalition fires its own laser through the mirrors to calibrate — that can be scene v5.)

The infrastructure needs zero changes — only the path is new: it starts at the dreadnought's eye, arcs through four white-ringed Aegis drones, and returns to strike the dreadnought's own flank. Same law-of-reflection math, just a loop instead of a line.

One paste block for Sonnet:

MISSION v4: "The Perseus Gambit" — Aegis Array vs. Medusa's Dreadnought.
Same rules: ONE execute_blender_code call; only API-compat fixes; report them.
This builds into a NEW file (v3 scene stays untouched).

STEP 1 — Execute the script below.
STEP 2 — GLARE: apply your proven socket-based glare node group to this scene
(FOG_GLOW, Threshold 1.0, Size 7), same acceptance test, save.
STEP 3 — Render all three views from terminal:
    blender -b ~/medusa/medusa_scene_v4.blend -a
Outputs: ~/medusa/medusa_v4_view_0001..0003.png
STEP 4 — Report paths + fixes.

--- SCRIPT BEGIN ---
```python
import bpy, os, math, random
from mathutils import Vector

# ============ CONFIG v4: THE PERSEUS GAMBIT ============
OUT_DIR = os.path.expanduser("~/medusa")
DISC_R, DISC_T = 1.1, 0.18
BEAM_R = 0.30                      # colossal main beam
EMITTER = Vector((1.5, 0, 0))      # Medusa's eye, front of dreadnought
V = [Vector((20, 1,   8)),         # Aegis drones: the arc of the mirror
     Vector((30, 3,  -3)),
     Vector((22, 5, -12)),
     Vector(( 4, 4, -13))]
IMPACT = Vector((-12, -2, -4.2))   # her own flank
random.seed(11)

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# ============ MATERIALS ============
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
MAT_RING_A  = pbr_mat("Ring_Alliance",(0.92, 0.92, 0.95), 0.0, 0.55)
MAT_TANK    = pbr_mat("Tank_Ti",      (0.60, 0.60, 0.62), 1.0, 0.30)
MAT_DREAD   = pbr_mat("Dread_Hull",   (0.04, 0.04, 0.05), 0.6, 0.70)
MAT_OBOL    = pbr_mat("Obol_Black",   (0.03, 0.03, 0.03), 0.4, 0.80)
MAT_ALPHA   = pbr_mat("Alpha_Hull",   (0.70, 0.72, 0.75), 1.0, 0.40)
MAT_BEAM    = emission_mat("Beam_Medusa_Red", (1.0, 0.05, 0.05), 25.0)
MAT_FLASH   = emission_mat("Flash_White",  (1.0, 1.0, 1.0),  80.0)
MAT_IRIS    = emission_mat("Medusa_Iris",  (1.0, 0.05, 0.02), 30.0)
MAT_VANE    = emission_mat("Radiator_Vane",(1.0, 0.18, 0.04),  5.0)
MAT_NAV     = emission_mat("Nav_Cyan",     (0.3, 0.9, 1.0),    8.0)
MAT_LENS    = emission_mat("Obol_Lens",    (1.0, 0.05, 0.05), 10.0)
MAT_STARDOT = emission_mat("Star_Glint",   (1.0, 1.0, 1.0),    3.0)
MAT_EXP_CORE= emission_mat("Exp_Core",     (1.0, 0.95, 0.7),  60.0)
MAT_EXP_MID = emission_mat("Exp_Mid",      (1.0, 0.35, 0.05), 25.0)
MAT_EXP_OUT = emission_mat("Exp_Outer",    (0.8, 0.08, 0.02),  8.0)

def add(op, **kw):
    op(**kw); return bpy.context.active_object

# ============ AEGIS DRONE BUILDER (white ring + cyan nav lights) ======
def make_drone(name, center, normal, fake_stars=False):
    parts = []
    disc = add(bpy.ops.mesh.primitive_cylinder_add,
               radius=DISC_R, depth=DISC_T, vertices=64, location=(0,0,0))
    disc.name = name; disc.data.materials.append(MAT_MIRROR)
    ring = add(bpy.ops.mesh.primitive_torus_add,
               major_radius=DISC_R+0.05, minor_radius=0.16, location=(0,0,0))
    ring.data.materials.append(MAT_RING_A); parts.append(ring)
    for i in range(6):
        a = i * math.pi/3.0
        x, y = (DISC_R+0.10)*math.cos(a), (DISC_R+0.10)*math.sin(a)
        if i % 2 == 0:
            g = add(bpy.ops.mesh.primitive_uv_sphere_add,
                    radius=0.13, segments=16, ring_count=8, location=(x,y,0))
            g.data.materials.append(MAT_TANK)
        else:
            g = add(bpy.ops.mesh.primitive_cube_add, size=0.18, location=(x,y,0))
            g.data.materials.append(MAT_RING_A)
        parts.append(g)
    for i in range(3):   # cyan navigation lights
        a = i * 2*math.pi/3.0 + 0.5
        s = add(bpy.ops.mesh.primitive_uv_sphere_add, radius=0.05,
                segments=8, ring_count=4,
                location=((DISC_R+0.18)*math.cos(a), (DISC_R+0.18)*math.sin(a), 0.1))
        s.data.materials.append(MAT_NAV); parts.append(s)
    if fake_stars:
        for j in range(7):
            a = random.uniform(0, 2*math.pi); r = random.uniform(0.15, 0.85)*DISC_R
            s = add(bpy.ops.mesh.primitive_uv_sphere_add,
                    radius=random.uniform(0.015, 0.035), segments=8, ring_count=4,
                    location=(r*math.cos(a), r*math.sin(a), DISC_T/2 + 0.02))
            s.data.materials.append(MAT_STARDOT); parts.append(s)
    for p in parts: p.parent = disc
    disc.rotation_mode = 'QUATERNION'
    disc.rotation_quaternion = normal.to_track_quat('Z', 'Y')
    disc.location = center
    return disc

# ============ THE BEAM LOOP (law of reflection, as always) ============
path = [EMITTER] + V + [IMPACT]
for i, vert in enumerate(V):
    d_in  = (vert - path[i]).normalized()
    d_out = (path[i+2] - vert).normalized()
    n = (d_out - d_in).normalized()
    make_drone("Aegis_%d" % (i+1), vert - n*(DISC_T/2.0), n)

for a, b in zip(path[:-1], path[1:]):
    d = b - a
    beam = add(bpy.ops.mesh.primitive_cylinder_add, radius=BEAM_R,
               depth=d.length, vertices=16, location=tuple((a+b)/2.0))
    beam.rotation_mode = 'QUATERNION'
    beam.rotation_quaternion = d.normalized().to_track_quat('Z', 'Y')
    beam.data.materials.append(MAT_BEAM)
for vert in V:
    f = add(bpy.ops.mesh.primitive_uv_sphere_add, radius=0.45,
            segments=16, ring_count=8, location=tuple(vert))
    f.data.materials.append(MAT_FLASH)

# ============ MEDUSA'S DREADNOUGHT ============
hull = add(bpy.ops.mesh.primitive_cylinder_add, radius=4.0, depth=36,
           location=(-18, 0, 0))
hull.rotation_euler = (0, math.pi/2, 0); hull.name = "Dreadnought"
hull.data.materials.append(MAT_DREAD)
def attach(o):
    o.parent = hull; o.matrix_parent_inverse = hull.matrix_world.inverted()
housing = add(bpy.ops.mesh.primitive_cylinder_add, radius=4.5, depth=3.0,
              location=(-1.0, 0, 0))
housing.rotation_euler = (0, math.pi/2, 0)
housing.data.materials.append(MAT_DREAD); attach(housing)
eye_ring = add(bpy.ops.mesh.primitive_torus_add, major_radius=2.2,
               minor_radius=0.35, location=(0.6, 0, 0))
eye_ring.rotation_euler = (0, math.pi/2, 0)
eye_ring.data.materials.append(MAT_DREAD); attach(eye_ring)
iris = add(bpy.ops.mesh.primitive_uv_sphere_add, radius=1.6,
           segments=24, ring_count=12, location=(0.4, 0, 0))
iris.data.materials.append(MAT_IRIS); attach(iris)
for k in range(6):   # ember-red radiator vanes
    vx = -6.0 - k*5.0
    vn = add(bpy.ops.mesh.primitive_cube_add, size=1, location=(vx, 0, 5.6))
    vn.scale = (2.2, 0.06, 1.6)
    vn.rotation_euler = (math.radians(-15 + 6*k), 0, 0)
    vn.data.materials.append(MAT_VANE); attach(vn)
for k in range(8):   # bristling turrets
    a = k * math.pi/4.0 + 0.3
    tx = -4.0 - (k % 4)*7.0
    t = add(bpy.ops.mesh.primitive_cylinder_add, radius=0.35, depth=1.4,
            vertices=12, location=(tx, 4.1*math.sin(a), 4.1*math.cos(a)))
    t.rotation_euler = (a, 0, 0)
    t.data.materials.append(MAT_DREAD); attach(t)

# --- her own beam striking her own flank ---
core = add(bpy.ops.mesh.primitive_uv_sphere_add, radius=0.9,
           segments=16, ring_count=8, location=tuple(IMPACT))
core.data.materials.append(MAT_EXP_CORE)
for j in range(5):
    off = Vector((random.uniform(-1.2,1.2), random.uniform(-1.4,0.4),
                  random.uniform(-1.0,1.0)))
    b = add(bpy.ops.mesh.primitive_uv_sphere_add,
            radius=random.uniform(0.5,0.9), segments=12, ring_count=6,
            location=tuple(IMPACT + off))
    b.data.materials.append(MAT_EXP_MID)
for j in range(6):
    off = Vector((random.uniform(-2.4,2.4), random.uniform(-2.6,0.6),
                  random.uniform(-2.0,2.0)))
    b = add(bpy.ops.mesh.primitive_uv_sphere_add,
            radius=random.uniform(0.7,1.4), segments=12, ring_count=6,
            location=tuple(IMPACT + off))
    b.data.materials.append(MAT_EXP_OUT)
for j in range(14):
    off = Vector((random.uniform(-4,4), random.uniform(-5,1),
                  random.uniform(-3.5,3.5)))
    if off.length < 2.0: off = off.normalized() * 2.6
    d = add(bpy.ops.mesh.primitive_cube_add,
            size=random.uniform(0.15,0.40), location=tuple(IMPACT + off))
    d.rotation_euler = (random.uniform(0,3.1), random.uniform(0,3.1),
                        random.uniform(0,3.1))
    d.data.materials.append(MAT_DREAD)

# ============ OBOL ESCORT SWARM (matte black, red lidar eye) =========
for i in range(8):
    pos = Vector((-30 + i*3.5, random.uniform(6,10),
                  random.uniform(5, 10)))
    o = add(bpy.ops.mesh.primitive_ico_sphere_add, radius=0.5,
            subdivisions=1, location=tuple(pos))
    o.data.materials.append(MAT_OBOL)
    lens = add(bpy.ops.mesh.primitive_uv_sphere_add, radius=0.09,
               segments=8, ring_count=4, location=tuple(pos + Vector((0,-0.48,0))))
    lens.data.materials.append(MAT_LENS)
    lens.parent = o; lens.matrix_parent_inverse = o.matrix_world.inverted()

# ============ BACKGROUND AEGIS FORMATION ============
for i in range(8):
    pos = Vector((0 + (i % 4)*9, 32.0, 6 + (i // 4)*10))
    n = Vector((random.uniform(-0.6,0.6), -1.0,
                random.uniform(-0.4,0.4))).normalized()
    make_drone("Aegis_bg_%d" % i, pos, n, fake_stars=True)

# ============ THE ALPHA, WATCHING FROM DEEP BACKGROUND ============
needle = add(bpy.ops.mesh.primitive_cylinder_add, radius=0.35, depth=7.0,
             location=(16, 55, 14))
needle.rotation_euler = (0, math.pi/2, 0); needle.name = "Alpha"
needle.data.materials.append(MAT_ALPHA)
dish = add(bpy.ops.mesh.primitive_cone_add, radius1=1.3, depth=0.8,
           location=(19.8, 55, 14))
dish.rotation_euler = (0, math.pi/2, 0); dish.data.materials.append(MAT_ALPHA)
ringh = add(bpy.ops.mesh.primitive_torus_add, major_radius=2.0,
            minor_radius=0.30, location=(16, 55, 14))
ringh.rotation_euler = (0, math.pi/2, 0); ringh.data.materials.append(MAT_ALPHA)
engn = add(bpy.ops.mesh.primitive_cylinder_add, radius=0.8, depth=1.6,
           location=(12.0, 55, 14))
engn.rotation_euler = (0, math.pi/2, 0); engn.data.materials.append(MAT_ALPHA)
for o in (dish, ringh, engn):
    o.parent = needle; o.matrix_parent_inverse = needle.matrix_world.inverted()

# ============ LIGHTS + WORLD (gentle stars, as tuned in v3) ==========
sun = add(bpy.ops.object.light_add, type='SUN', location=(0, 0, 50))
sun.data.energy = 6.0
sun.rotation_euler = (math.radians(55), math.radians(-20), math.radians(30))
fill = add(bpy.ops.object.light_add, type='SUN', location=(0, -50, 10))
fill.data.energy = 1.2
fill.rotation_euler = (math.radians(78), 0.0, 0.0)
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
ramp.color_ramp.elements[0].position = 0.845
ramp.color_ramp.elements[0].color = (0.001, 0.002, 0.005, 1.0)
ramp.color_ramp.elements[1].position = 0.862
ramp.color_ramp.elements[1].color = (0.55, 0.55, 0.62, 1.0)
wnt.links.new(tc.outputs['Generated'], noise.inputs['Vector'])
wnt.links.new(noise.outputs['Fac'], ramp.inputs['Fac'])
wnt.links.new(ramp.outputs['Color'], w_bg.inputs['Color'])
w_bg.inputs['Strength'].default_value = 1.0
wnt.links.new(w_bg.outputs['Background'], w_out.inputs['Surface'])

# ============ THREE CAMERAS, BOUND TO FRAMES ============
def make_cam(name, loc, aim_loc, lens):
    aim = add(bpy.ops.object.empty_add, location=aim_loc)
    cam = add(bpy.ops.object.camera_add, location=loc)
    cam.name = name; cam.data.lens = lens
    cam.constraints.new('TRACK_TO').target = aim
    return cam

cam_wide = make_cam("Cam_Wide",       (-2, -62,  2), (-2, 0, -2), 30)
cam_eye  = make_cam("Cam_MedusaSide", (-10, -14, 10), (18, 2, -2), 28)
cam_coal = make_cam("Cam_AegisSide",  (36, -18, -2), (-14, 0, -1), 28)

scn = bpy.context.scene
scn.timeline_markers.clear()
for f, c in ((1, cam_wide), (2, cam_eye), (3, cam_coal)):
    m = scn.timeline_markers.new(c.name, frame=f)
    m.camera = c
scn.frame_start, scn.frame_end = 1, 3
scn.camera = cam_wide

# ============ RENDER SETTINGS ============
scn.render.engine = 'CYCLES'
scn.cycles.samples = 128
scn.render.resolution_x = 1920
scn.render.resolution_y = 1080
scn.render.image_settings.file_format = 'PNG'
scn.render.filepath = os.path.join(OUT_DIR, "medusa_v4_view_")
scn.compositing_node_group = None   # glare in STEP 2

os.makedirs(OUT_DIR, exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT_DIR, "medusa_scene_v4.blend"))
print("PERSEUS GAMBIT BUILT OK")
```
--- SCRIPT END ---

What you'll see: the dreadnought's glowing red eye firing forward, the beam arcing through four white-ringed, cyan-lit Aegis mirrors "like pieces of a puzzle," and slamming back into her own hull — with her Obol escort swarm hovering uselessly above, and the Alpha watching from far behind the mirror line. The wide shot reads as a giant question-mark-shaped loop of light, which feels almost poetic.

Same caveat as before: the two POV camera framings may need a nudge once we see through them. Show me the three renders, and then I'll write the GPT repaint prompts — this time with special language for the dreadnought's radiator forest and the eye. Perseus is ready. 🪞🐍♟️
