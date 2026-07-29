"""
Composite script for Mission v5.2 (Fable's screen-blend VFX approach).
Run this LATER, once Nir has GPT 5.4 Image 2 repainted plates for the
beamless scenepass images (medusa_v5_scenepass_0001/2/3.png).

Usage:
    python3 composite_v5_beams.py

Requires: pillow, numpy (both already available in this environment).
"""
from PIL import Image
import numpy as np
import os

MEDUSA_DIR = os.path.expanduser("~/medusa")

def composite(gpt_path, beam_path, out_path):
    b = Image.open(beam_path).convert("RGB")
    a = Image.open(gpt_path).convert("RGB").resize(b.size)
    A = np.asarray(a, dtype=float) / 255.0
    B = np.asarray(b, dtype=float) / 255.0
    out = 1.0 - (1.0 - A) * (1.0 - B)          # screen blend
    Image.fromarray((out * 255).astype("uint8")).save(out_path)
    print("Saved:", out_path)

if __name__ == "__main__":
    # Fill in the actual GPT plate filenames once Nir provides them, e.g.:
    # composite(
    #     gpt_path=f"{MEDUSA_DIR}/gpt_plate_A_wide.png",
    #     beam_path=f"{MEDUSA_DIR}/medusa_v5_beampass_0001.png",
    #     out_path=f"{MEDUSA_DIR}/medusa_v5_final_0001.png",
    # )
    print("Edit this script with the actual GPT plate paths, then re-run.")
