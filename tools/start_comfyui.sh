#!/bin/bash
source ~/miniforge3/etc/profile.d/conda.sh
conda activate comfyui
cd ~/Anime/tools/ComfyUI
nohup python main.py --listen 127.0.0.1 --port 8188 > /tmp/comfyui.log 2>&1 &
echo "ComfyUI starting — wait ~30 seconds, then open http://127.0.0.1:8188"