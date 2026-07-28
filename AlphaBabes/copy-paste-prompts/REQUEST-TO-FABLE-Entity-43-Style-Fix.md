# 🔧 PROBLEM REPORT FOR FABLE — Entity #43

## What Happened

We generated the Madie & Nir travel triptych prompt (F1, Paris Monet gallery, Kyoto temple) using GPT 5.4 Image 2. Twice. Both times the images came out looking like **real photographs** of real people, not Pixar/Disney 3D animation.

The prompt has this style prefix at the top:
"Pixar/Disney 3D animation style, cinematic feature-film quality render. Warm, charming, emotionally expressive characters with the signature polished Pixar finish."

But GPT Image ignores it completely and produces photorealism.

## Context

This same prefix works perfectly for all our alien, planet, and spaceship images — those come out Pixar-style. But for Earth scenes with humans in real locations (F1 race, Paris museum, Kyoto), GPT Image defaults to photorealism.

## Locked Character Descriptions (CANON)

**MADIE:** Romanian, early 20s, curvy, busty, pretty, brunette, long dark-brown hair, nothing on her head.

**NIR:** mid-40s, short dark hair, athletic build, no glasses, casual t-shirt and jeans.

## What We Need

A fix for this prompt so it renders as Pixar/Disney 3D animation, not photographs. Whatever approach you think will work — you're the expert.

Current prompt is at:
AlphaBabes/copy-paste-prompts/Fable-Pass-01-Entity-43-Madie-Nir-Travel-Triptych.txt

Thank you Fable! 🎬