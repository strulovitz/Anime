Favicon for anthropic
Claude Fable 5

Ah, the classic tripod problem! 😅 This is a known weakness of image models: they've seen millions of bipeds-with-tails (dinosaurs, kangaroos, dragons...) and almost zero true tripods, so they "correct" the third leg into a tail. Also, if the reference sheet itself got it wrong, every scene will inherit the mistake. Let's fix both ends:
Step 1 — Check the source 🔍

Look at your reference sheet image first. If Zev already has 2 legs + tail there, regenerate the sheet before anything else — a wrong reference poisons every scene that follows.
Step 2 — The Anti-Tail Patch 🩹

Paste this block near the top of the prompt (early text gets the most weight), both when regenerating the sheet and in every Zev/Skarn scene:

ANATOMY LOCK — THREE LEGS: this creature stands on exactly THREE identical, full-length, weight-bearing LEGS arranged in a perfect tripod, 120 degrees apart, like a camera tripod or a three-legged stool — one leg points forward, two legs point back-left and back-right. All three legs are the SAME length, the SAME thickness, with the SAME hoof-claw foot, all three planted firmly on the ground. There is NO tail. There is NO rear appendage. It is NOT a biped. Nothing hangs behind the body — the third limb is a real leg with a knee and a foot standing on the floor, carrying weight. Count the feet on the ground: three.

And remove/avoid these trap-words from the rest of the prompt if present: tail, rear, behind, hind legs — each one nudges the model toward biped-plus-tail.
Step 3 — Choose poses that force the tripod 📐

Three-quarter views let the model hide the third leg and hallucinate a tail. These angles make cheating impossible:
Works well ✅	Risky ❌
Slightly elevated front view, one leg toward camera, two spread behind — all three feet visible	Side profile (legs overlap → looks bipedal)
Top-down / high-angle diagram view	Walking poses (gait confusion)
Wide standing stance, feet clearly separated on visible floor	Legs in shadow or cropped at the knees
Step 4 — Bootstrap trick 🎯

Generate several attempts of a single Skarn, standing still, high angle, all three feet visible. The moment you get one correct image, that becomes your new reference image for all future Skarn scenes — a correct visual reference teaches the model far better than any text.
Step 5 — Last resort 🖌️

If your tool supports inpainting/editing, take a near-perfect image and edit just the rear region with: "replace the tail with a third full leg, identical to the other two, knee and hoof-claw foot planted on the floor." Fixing one limb is much easier than re-rolling the whole scene.

My honest expectation: even with the patch, you'll get maybe 50–70% success on tripods — it's genuinely one of the hardest body plans for these models. Generate in small batches and curate ruthlessly. 💪

Want me to also produce a rewritten full Zev sheet prompt with the patch already integrated and the risky words scrubbed out? Or shall we push on to #12: the Zĭrán Pilgrim-Ship? 🚀