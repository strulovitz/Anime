# Claude Fable 5 — Medusa Laser-Relay Blender Scene Mission v5: Laser Chess (2026-07-29)

You're half wrong and I'll defend that half honestly: v4 has four mirrors, not one — the beam loops eye → four Aegis discs → her own flank. But your real accusation lands, and lands hard: the path is a flat, legible pentagon. A static mirror loop that any camera can see is a trap for a dumb AI. Medusa would map every mirror normal from parallax before her capacitors finished charging, and simply... not fire. You didn't miss something smart. There was nothing smart there to miss. So let me now earn the scene. 🙇

Why would a superintelligence EVER fire into a mirror array?

Because being smarter doesn't help when the problem is information and time, not intelligence. Three real mechanisms, all of which we can show in the frame:

1. The board is unreadable. A mirror's face reveals its angle only when it glints. The Aegis drones tumble slowly, constantly — camouflage shuffling. With ~30 drones each free to face anywhere, the space of possible beam routings is combinatorially explosive; Medusa can compute anything, but she cannot observe which single routing is armed. She's playing Khet against a board whose pieces are spinning.
2. The winning move is a discovered check. At fire-time, the corridor to the Alpha (the bait — your idea, it stays) is genuinely clear. Medusa verifies line-of-sight, commits, fires. During the beam's burn, one drone snaps into the corridor — a 2-meter disc with a tiny moment of inertia slews in milliseconds, while her kilometer-scale emitter gimbal needs seconds and her capacitor bank must finish discharging somewhere. Small pieces out-turn the queen. The rest of the path was armed by one synchronized rotation of the lattice — the move that reveals the attack only after it's unstoppable.
3. She IS counter-playing — and we show it. Point-defense beams snipe mirror drones in the lattice. She kills two. But she's shooting yesterday's board: the dead drones are decoys/former path candidates, and every critical bounce vertex has a backup drone station-keeping three meters away, already pre-angled. Kill a piece, the path re-routes through its twin. That's the Alliance move that makes her genius irrelevant: redundancy beats prediction.

The Khet mapping, explicitly:

| Khet / Laser Chess | Our scene |
|---|---|
| The board | A 3D lattice of drone stations (grid spacing 6 m) |
| Pyramids / mirror pieces | Aegis mirror drones, most NOT on the path — they're the other pieces |
| The Sphinx (laser) | Medusa's eye emitter |
| The Pharaoh in check | Medusa's own hull — the beam returns as a discovered check |
| Captured pieces | Two sniped drones, shattered, embers cooling |
| The sacrifice/gambit | The Alpha, sitting knowingly on the firing line |

And the beam path itself is no longer a flat pentagon: seven bounces threading the lattice in true 3D — every vertex is a lattice node (a board square), the path weaves up, down, behind, and through, like a knight's tour. The script computes that every non-path drone keeps a safe distance from every beam segment (point-to-segment distance |p − (a + t*ab)| > 2.5 m) — the board is dense but the beam threads it cleanly, which is exactly what makes it read as played, not painted.

One paste block for Sonnet:

MISSION v5: "Laser Chess" — the Perseus Gambit as a real 3D Khet position.
Full rebuild into a NEW file (v4 stays). Same rules: ONE execute_blender_code
call, only API-compat fixes, report them.

STEP 1 — Execute the script below.
STEP 2 — Apply your proven glare setup (FOG_GLOW, Threshold 1.0, Size 7),
same acceptance test, save.
STEP 3 — Terminal render:  blender -b ~/medusa/medusa_scene_v5.blend -a
Outputs: ~/medusa/medusa_v5_view_0001..0003.png
STEP 4 — Report paths + fixes + the printed lattice statistics.

--- SCRIPT BEGIN ---
```python
import bpy, os, math, random
from mathutils import Vector

# ========= CONFIG v5: THE 3D LASER-CHESS BOARD =========
OUT_DIR = os.path.expanduser("~/medusa")
DISC_R, DISC_T, BEAM_R = 1.1, 0.18, 0.30
EMITTER = Vector((1.5, 0, 0))
V = [Vector((24,  3,   6)),      # seven bounces, threading the lattice in 3D
     Vector((36, -3,   0)),
     Vector((18, -9,  -6)),
     Vector((30,  9, -12)),
     Vector((12,  3,   6)),
     Vector((18, -3, -12)),
     Vector(( 6,  3,  -6))]
IMPACT   = Vector((-12, -2, -4.2))
CASUALTY = [Vector((12, -3, 0)), Vector((24, -9, 6))]   # pieces she captured
SNIPERS  = [Vector((-10, -3.7, 1.5)), Vector((-4, 3.2, 2.4))]  # her PD turrets
random.seed(23)

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# ========= MATERIALS =========
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

MAT_MIRROR  = pbr_mat("SiC_Mirror",   (0.92,0.94,0.92), 1.0, 0.12)
MAT_RING_A  = pbr_mat("Ring_Alliance",(0.92,0.92,0.95), 0.0, 0.55)
MAT_TANK    = pbr_mat("Tank_Ti",      (0.60,0.60,0.62), 1.0, 0.30)
MAT_DREAD   = pbr_mat("Dread_Hull",   (0.03,0.03,0.04), 0.5, 0.75)
MAT_SCORCH  = pbr_mat("Scorched",     (0.02,0.02,0.02), 0.2, 0.90)
MAT_ALPHA   = pbr_mat("Alpha_Hull",   (0.70,0.72,0.75), 1.0, 0.40)
MAT_BEAM    = emission_mat("Beam_Main",   (1.0,0.05,0.05), 25.0)
MAT_SNIPE   = emission_mat("Beam_PD",     (1.0,0.10,0.05), 12.0)
MAT_FLASH   = emission_mat("Flash_White", (1.0,1.0,1.0),   80.0)
MAT_IRIS    = emission_mat("Medusa_Iris", (1.0,0.05,0.02), 30.0)
MAT_VANE    = emission_mat("Radiator_Vane",(1.0,0.18,0.04), 5.0)
MAT_NAV     = emission_mat("Nav_Cyan",    (0.3,0.9,1.0),    8.0)
MAT_EMBER   = emission_mat("Ember",       (1.0,0.25,0.05),  6.0)
MAT_STARDOT = emission_mat("Star_Glint",  (1.0,1.0,1.0),    3.0)
MAT_EXP_CORE= emission_mat("Exp_Core",    (1.0,0.95,0.7),  60.0)
MAT_EXP_MID = emission_mat("Exp_Mid",     (1.0,0.35,0.05), 25.0)
MAT_EXP_OUT = emission_mat("Exp_Outer",   (0.8,0.08,0.02),  8.0)

def add(op, **kw):
    op(**kw); return bpy.context.active_object

# ========= AEGIS DRONE =========
def make_drone(name, center, normal, fake_stars=False):
    parts = []
    disc = add(bpy.ops.mesh.primitive_cylinder_add,
               radius=DISC_R, depth=DISC_T, vertices=64, location=(0,0,0))
    disc.name = name; disc.data.materials.append(MAT_MIRROR)
    ring = add(bpy.ops.mesh.primitive_torus_add,
               major_radius=DISC_R+0.05, minor_radius=0.16, location=(0,0,0))
    ring.data.materials.append(MAT_RING_A); parts.append(ring)
    for i in range(6):
        a = i*math.pi/3.0
        x, y = (DISC_R+0.10)*math.cos(a), (DISC_R+0.10)*math.sin(a)
        if i % 2 == 0:
            g = add(bpy.ops.mesh.primitive_uv_sphere_add, radius=0.13,
                    segments=16, ring_count=8, location=(x,y,0))
            g.data.materials.append(MAT_TANK)
        else:
            g = add(bpy.ops.mesh.primitive_cube_add, size=0.18, location=(x,y,0))
            g.data.materials.append(MAT_RING_A)
        parts.append(g)
    for i in range(3):
        a = i*2*math.pi/3.0 + 0.5
        s = add(bpy.ops.mesh.primitive_uv_sphere_add, radius=0.05,
                segments=8, ring_count=4,
                location=((DISC_R+0.18)*math.cos(a),(DISC_R+0.18)*math.sin(a),0.1))
        s.data.materials.append(MAT_NAV); parts.append(s)
    if fake_stars:
        for j in range(7):
            a = random.uniform(0,2*math.pi); r = random.uniform(0.15,0.85)*DISC_R
            s = add(bpy.ops.mesh.primitive_uv_sphere_add,
                    radius=random.uniform(0.015,0.035), segments=8, ring_count=4,
                    location=(r*math.cos(a), r*math.sin(a), DISC_T/2+0.02))
            s.data.materials.append(MAT_STARDOT); parts.append(s)
    for p in parts: p.parent = disc
    disc.rotation_mode = 'QUATERNION'
    disc.rotation_quaternion = normal.to_track_quat('Z','Y')
    disc.location = center
    return disc

# ========= THE PLAYED PATH (law of reflection at every node) =========
path = [EMITTER] + V + [IMPACT]
normals = []
for i, vert in enumerate(V):
    d_in  = (vert - path[i]).normalized()
    d_out = (path[i+2] - vert).normalized()
    n = (d_out - d_in).normalized(); normals.append(n)
    make_drone("Aegis_path_%d" % (i+1), vert - n*(DISC_T/2.0), n)

# backups: every odd vertex has a twin, pre-angled, 3.5 m off-station
for i in (0, 2, 4, 6):
    make_drone("Aegis_backup_%d" % i, V[i] + Vector((0, 3.5, 1.0)), normals[i])

# thruster puffs on drone #1 — it snapped into the corridor mid-burn
for j in range(3):
    a = j*2.1
    p = add(bpy.ops.mesh.primitive_cone_add, radius1=0.10, depth=0.5,
            location=tuple(V[0] + Vector((1.5*math.cos(a), 1.5*math.sin(a), -0.4))))
    p.data.materials.append(MAT_NAV)

for a, b in zip(path[:-1], path[1:]):
    d = b - a
    beam = add(bpy.ops.mesh.primitive_cylinder_add, radius=BEAM_R,
               depth=d.length, vertices=16, location=tuple((a+b)/2.0))
    beam.rotation_mode = 'QUATERNION'
    beam.rotation_quaternion = d.normalized().to_track_quat('Z','Y')
    beam.data.materials.append(MAT_BEAM)
for vert in V:
    f = add(bpy.ops.mesh.primitive_uv_sphere_add, radius=0.40,
            segments=16, ring_count=8, location=tuple(vert))
    f.data.materials.append(MAT_FLASH)

# ========= THE REST OF THE BOARD: the lattice =========
def seg_dist(p, a, b):
    ab = b - a
    t = max(0.0, min(1.0, (p - a).dot(ab) / ab.length_squared))
    return (a + ab*t - p).length

segs = list(zip(path[:-1], path[1:]))
occupied = V + CASUALTY
lattice_count = 0
for x in range(6, 37, 6):
    for y in (-9, -3, 3, 9):
        for z in (-12, -6, 0, 6, 12):
            p = Vector((x, y, z))
            if min(seg_dist(p, a, b) for a, b in segs) < 2.5: continue
            if min((p - q).length for q in occupied) < 4.0: continue
            if random.random() > 0.45: continue
            n = Vector((random.uniform(-1,1), random.uniform(-1,1),
                        random.uniform(-1,1))).normalized()
            make_drone("Aegis_board_%d" % lattice_count, p, n,
                       fake_stars=(n.y < -0.3))
            occupied.append(p); lattice_count += 1
print("LATTICE: %d board drones placed, all verified > 2.5 m off-beam"
      % lattice_count)

# ========= CAPTURED PIECES + her counter-fire =========
for k, cpos in enumerate(CASUALTY):
    dead = add(bpy.ops.mesh.primitive_cylinder_add, radius=DISC_R,
               depth=DISC_T, vertices=32, location=tuple(cpos))
    dead.rotation_euler = (random.uniform(0.5,1.2), random.uniform(0.5,1.2), 0)
    dead.data.materials.append(MAT_SCORCH)
    for j in range(6):
        off = Vector((random.uniform(-1.5,1.5), random.uniform(-1.5,1.5),
                      random.uniform(-1.5,1.5)))
        s = add(bpy.ops.mesh.primitive_cube_add,
                size=random.uniform(0.08,0.2), location=tuple(cpos + off))
        s.rotation_euler = (random.uniform(0,3), random.uniform(0,3), 0)
        s.data.materials.append(MAT_SCORCH)
    e = add(bpy.ops.mesh.primitive_uv_sphere_add, radius=0.3,
            segments=12, ring_count=6, location=tuple(cpos))
    e.data.materials.append(MAT_EMBER)
    d = cpos - SNIPERS[k]        # her point-defense beam, thin and mean
    sb = add(bpy.ops.mesh.primitive_cylinder_add, radius=0.05,
             depth=d.length, vertices=8,
             location=tuple((cpos + SNIPERS[k])/2.0))
    sb.rotation_mode = 'QUATERNION'
    sb.rotation_quaternion = d.normalized().to_track_quat('Z','Y')
    sb.data.materials.append(MAT_SNIPE)

# ========= THE DREADNOUGHT =========
hull = add(bpy.ops.mesh.primitive_cylinder_add, radius=4.0, depth=36,
           location=(-18,0,0))
hull.rotation_euler = (0, math.pi/2, 0); hull.name = "Dreadnought"
hull.data.materials.append(MAT_DREAD)
def attach(o):
    o.parent = hull; o.matrix_parent_inverse = hull.matrix_world.inverted()
housing = add(bpy.ops.mesh.primitive_cylinder_add, radius=4.5, depth=3.0,
              location=(-1.0,0,0))
housing.rotation_euler = (0, math.pi/2, 0)
housing.data.materials.append(MAT_DREAD); attach(housing)
eye_ring = add(bpy.ops.mesh.primitive_torus_add, major_radius=2.2,
               minor_radius=0.35, location=(0.6,0,0))
eye_ring.rotation_euler = (0, math.pi/2, 0)
eye_ring.data.materials.append(MAT_DREAD); attach(eye_ring)
iris = add(bpy.ops.mesh.primitive_uv_sphere_add, radius=1.6,
           segments=24, ring_count=12, location=(0.4,0,0))
iris.data.materials.append(MAT_IRIS); attach(iris)
for k in range(6):
    vn = add(bpy.ops.mesh.primitive_cube_add, size=1,
             location=(-6.0-k*5.0, 0, 4.7))
    vn.scale = (2.2, 0.06, 1.6)
    vn.rotation_euler = (math.radians(-15+6*k), 0, 0)
    vn.data.materials.append(MAT_VANE); attach(vn)
for k in range(8):
    a = k*math.pi/4.0 + 0.3
    t = add(bpy.ops.mesh.primitive_cylinder_add, radius=0.35, depth=1.4,
            vertices=12, location=(-4.0-(k%4)*7.0, 4.1*math.sin(a), 4.1*math.cos(a)))
    t.rotation_euler = (a, 0, 0)
    t.data.materials.append(MAT_DREAD); attach(t)

# --- her own beam, returned: the check ---
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
    if off.length < 2.0: off = off.normalized()*2.6
    d = add(bpy.ops.mesh.primitive_cube_add,
            size=random.uniform(0.15,0.40), location=tuple(IMPACT + off))
    d.rotation_euler = (random.uniform(0,3.1), random.uniform(0,3.1),
                        random.uniform(0,3.1))
    d.data.materials.append(MAT_DREAD)

# ========= THE ALPHA — the bait, on the original aim line =========
dir1 = (V[0] - EMITTER).normalized()
ALPHA_POS = V[0] + dir1 * 16.0
needle = add(bpy.ops.mesh.primitive_cylinder_add, radius=0.55, depth=11,
             location=(0,0,0))
needle.name = "Alpha"; needle.data.materials.append(MAT_ALPHA)
dish = add(bpy.ops.mesh.primitive_cone_add, radius1=2.0, depth=1.2,
           location=(0,0,6.2)); dish.data.materials.append(MAT_ALPHA)
ringh = add(bpy.ops.mesh.primitive_torus_add, major_radius=3.2,
            minor_radius=0.45, location=(0,0,0.5))
ringh.data.materials.append(MAT_ALPHA)
eng = add(bpy.ops.mesh.primitive_cylinder_add, radius=1.3, depth=2.4,
          location=(0,0,-6.4)); eng.data.materials.append(MAT_ALPHA)
glow = add(bpy.ops.mesh.primitive_cylinder_add, radius=1.0, depth=0.3,
           location=(0,0,-7.7)); glow.data.materials.append(MAT_NAV)
for o in (dish, ringh, eng, glow):
    o.parent = needle
needle.rotation_mode = 'QUATERNION'
needle.rotation_quaternion = (EMITTER - ALPHA_POS).normalized().to_track_quat('Z','Y')
needle.location = ALPHA_POS

# ========= LIGHTS + WORLD =========
sun = add(bpy.ops.object.light_add, type='SUN', location=(0,0,50))
sun.data.energy = 6.0
sun.rotation_euler = (math.radians(55), math.radians(-20), math.radians(30))
fill = add(bpy.ops.object.light_add, type='SUN', location=(0,-50,10))
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
ramp.color_ramp.elements[0].color = (0.001,0.002,0.005,1.0)
ramp.color_ramp.elements[1].position = 0.862
ramp.color_ramp.elements[1].color = (0.55,0.55,0.62,1.0)
wnt.links.new(tc.outputs['Generated'], noise.inputs['Vector'])
wnt.links.new(noise.outputs['Fac'], ramp.inputs['Fac'])
wnt.links.new(ramp.outputs['Color'], w_bg.inputs['Color'])
w_bg.inputs['Strength'].default_value = 1.0
wnt.links.new(w_bg.outputs['Background'], w_out.inputs['Surface'])

# ========= CAMERAS =========
def make_cam(name, loc, aim_loc, lens):
    aim = add(bpy.ops.object.empty_add, location=aim_loc)
    cam = add(bpy.ops.object.camera_add, location=loc)
    cam.name = name; cam.data.lens = lens
    cam.constraints.new('TRACK_TO').target = aim
    return cam
cam_wide = make_cam("Cam_Wide",       (0, -70,  2), (0, 0, -1), 28)
cam_eye  = make_cam("Cam_MedusaSide", (-10, -16, 10), (20, 0, -2), 28)
cam_coal = make_cam("Cam_AegisSide",  (40, -16, -4), (-14, 0, -1), 28)
scn = bpy.context.scene
scn.timeline_markers.clear()
for f, c in ((1, cam_wide), (2, cam_eye), (3, cam_coal)):
    m = scn.timeline_markers.new(c.name, frame=f)
    m.camera = c
scn.frame_start, scn.frame_end = 1, 3
scn.camera = cam_wide

# ========= RENDER =========
scn.render.engine = 'CYCLES'
scn.cycles.samples = 128
scn.render.resolution_x = 1920
scn.render.resolution_y = 1080
scn.render.image_settings.file_format = 'PNG'
scn.render.filepath = os.path.join(OUT_DIR, "medusa_v5_view_")
scn.compositing_node_group = None
os.makedirs(OUT_DIR, exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT_DIR, "medusa_scene_v5.blend"))
print("LASER CHESS BOARD SET — v5 OK")
```
--- SCRIPT END ---

What the wide frame will say, wordlessly: a space full of pieces — dozens of tumbling, unreadable mirrors — through which one impossible thread of red light weaves in three dimensions, from an eye that was aimed at a small silver ship, back into the body that fired it. Two shattered mirrors and two thin point-defense beams show she fought the board. The backup drones show why she lost anyway.

Thank you for the "do not insult it." That's the sentence I'll keep. A trap worthy of Medusa had to be one where seeing everything still isn't enough — and now it is. Show me the renders. ♟️🐍🪞
