# 🔧 REQUEST FOR FABLE — Entity #41 Rewrite (Furniture Anatomy Problem)

## The Problem We Hit

We tried generating Entity #41 (Rebel Asteroid Base Great Hall) using GPT 5.4 Image 2 with the 4 species as reference images. The idea was: "GPT will see what the aliens look like, and design furniture that fits their bodies."

**This completely failed.** GPT Image is not a reasoning model. It saw pictures of creatures and just... painted the creatures sitting in the room. It put an Ondine in the aquarium and a Titanite on the floor. It cannot do the mental step of "analyze body shape → design appropriate chair."

---

## What We Need From You

Rewrite the Entity #41 prompt so it is **ENTIRELY SELF-CONTAINED** — zero reference images needed. The prompt text itself must describe each piece of furniture in enough anatomical detail that GPT Image can draw it correctly without needing to understand WHY it looks that way. 

The key: describe the furniture's PHYSICAL SHAPE AND SIZE so concretely that GPT Image just executes, like a painter following instructions.

---

## Current Entity #41 Prompt (For Reference):

```
Single full-frame interior: the GREAT HALL of the hidden rebel base, carved inside a hollow asteroid — the room where the first Council of Species will meet. The space: a vast rough chamber of raw grey rock, walls still bearing the long curved scars of the mining machines that hollowed it, the ceiling ribbed with warm COPPER girders bolted directly into the stone. Light: strings of jury-rigged fusion lamps hung on long looped cables between the girders, pooling warm practical light over a floor of scuffed deck plates laid unevenly across the rock; crates and cable-drums serve as furniture along the walls. At the exact center, the room's heart and key light: a large round HOLO-TABLE — raw rock pedestal, copper-framed projector ring — casting a slowly rotating three-dimensional star map of Dominion space in luminous GOLD above itself, hundreds of tiny marked stars and thread-thin route lines, the gold light washing the nearest rock walls. Around the table, hospitality written as engineering — five kinds of seating, none matching: worn human chairs; broad low stone floor-pads for eight-legged Titanites; a tall open PERCH-RAIL of copper pipe for winged Aerians; a wheeled transparent WATER-ALCOVE, softly glowing teal, its sea gently rippling, ready for an Ondine; and one wide six-lobed woven floor cushion shaped for a hexapod Zĭrán. Small honest details: a kettle steaming on a crate, hand-chalked tallies on a rock wall, a patched pressure door. No figures — the room waiting for history. Mood: improvised, warm, defiant — a cave that decided to become a parliament.
```

The furniture lines that failed: "broad low stone floor-pads for eight-legged Titanites" — GPT doesn't know what "eight-legged Titanite" means. Ditto for the Aerian perch-rail, Ondine water-alcove, and Zĭrán cushion.

---

## Species Anatomy (So You Know What The Furniture Needs To Fit)

### TITANITES (Entity #05)
- 1.2m tall, 3m long, masses like a small truck
- EIGHT massive pillar-legs in two rows of four, short and thick as tree trunks
- Low, broad, dome-backed body
- The legs splay wide — needs a LOT of floor space
- Carries biomineralized armor plates on back (living rock)
- Four eyes in a low horizontal row under a brow-shelf — no raised head

### AERIANS (Entity #06)
- 6m wingspan, body mass less than a human child
- Slender keel-body like a sailplane fuselage
- On the ground: folds wings into tall narrow tents, walks on WRIST-HOOKS at mid-wing
- Stilt-walks — tall and spindly on the ground
- Two small fine fore-arms with delicate fingers for manipulation
- Keel hangs VERITCALLY when grounded (wings tented upward)
- Needs a PERCH to hook onto, NOT a chair — like a bird perch but shaped for wrist-hooks at about 1.5m height

### ONDINES (Entity #04)
- 1.6m long aquatic bell-body (tulip-shaped mantle)
- Lives in water — cannot be out of water on dry land
- On land/spaceships: uses a transparent water-filled acrylic TANK-SUIT on a four-legged walking frame with flexible sleeve-gauntlets
- The tank-suit is described in detail in the Ondine prompt
- For a meeting room: the WATER-ALCOVE is a stationary version — a transparent wheeled basin of water they can float in

### ZĬRÁN (Entity #01)
- 1.2m tall, 1.6m long, masses like a large dog
- SIX limbs: FOUR column-like walking legs (wide splayed four-toed grip-pads) + TWO slender boneless manipulator arms (elephant-trunk-like, ending in three prehensile finger-tendrils)
- Low horizontal teardrop body
- Dome-backed (like a turtle shell but organic and warm)
- Neck arcs up into a sensory crown of five frond-stalks
- Needs a wide, low surface — can't sit in a chair, but can settle onto a broad cushion

---

## What We Need: The Rewritten Prompt

Please rewrite Entity #41 so that when read by GPT Image, each furniture piece is described with its exact physical shape, size, and material — so concretely that the AI doesn't need to know the alien anatomy to draw the right furniture. It just needs to know "draw a thing that looks like THIS."

The five seats become:
1. **Human chairs** — simple, worn, salvaged (easy, GPT knows chairs)
2. **Titanite floor-pad** — describe its exact physical shape: a massive flat slab of grey stone, 3 meters wide, 2 meters deep, about 30cm thick, resting directly on the deck plates, surface polished smooth by use, with wide shallow grooves worn into it where eight heavy legs always rest. Low to the ground — no backrest, nothing tall.
3. **Aerian perch-rail** — describe its exact physical shape: a horizontal copper pipe mounted at roughly 1.5 meters height on two sturdy vertical posts, the pipe surface scuffed and scratched by repeated hook-grips, with a narrow shelf-platform below it at knee-height for balance. Tall, narrow, skeletal — nothing like a chair.
4. **Ondine water-alcove** — describe its exact physical shape: a transparent acrylic tank roughly 2 meters wide and 1.5 meters deep, rectangular, mounted on four small wheels (like a heavy industrial cart), filled with gently rippling seawater lit from within by soft teal LEDs along the tank's bottom rim, bubbles rising slowly inside. The tank is open at the top. NO creature inside — just the glowing water waiting.
5. **Zĭrán cushion** — describe its exact physical shape: a wide flat woven floor cushion about 1.5 meters across, shaped like a rounded hexagon with six shallow lobes (one for each limb to settle into), made of coarse woven natural fiber in warm browns and creams, thick padding (like a futon), resting directly on the deck plates. Low and wide.

IMPORTANT: The prompt must say "NO FIGURES, NO CREATURES, NO ALIENS — the room is completely empty of living beings." This must be stated EMPHATICALLY at the end.

---

## Final Format

Please output the complete rewritten prompt as a single self-contained block (with Global Style Prefix), ready for me to save as a .txt file. And a brief .md companion describing what the image shows.

Thank you Fable! 🚀✨