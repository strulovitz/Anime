# Voice Samples — Naming Convention (locked 2026-08-02)

Voice sample files (from ElevenLabs, for Madie's character voice) follow the
EXACT SAME naming pattern as the scene images — just a different file
extension. This makes it trivial to match an audio file to its picture.

## Pattern

```
Fable-Pass-01-Scene-XX-Scene-Name.mp3
```

- Same "Pass" number as the image pass (currently Pass 01).
- Same Scene-XX-Scene-Name as the corresponding image file in
  `AlphaBabes/images/Scene-XX-Scene-Name.png`.
- NO extra words like "Voice" or "Sample" at the end — the `.mp3` extension
  already tells you it's audio. Keep the name identical to the image name,
  extension aside.

## Example

- Image: `AlphaBabes/images/Scene-01-The-Alpha-in-the-Void.png`
- Voice: `AlphaBabes/voice-samples/Fable-Pass-01-Scene-01-The-Alpha-in-the-Void.mp3`

## Folder

All voice files live in: `AlphaBabes/voice-samples/`

## Workflow (PUSH-ON-SAVE applies here too)

Every time Nir says "i saved it" for a new ElevenLabs voice file:
1. Find it in `/home/nir/Downloads/` (or wherever it landed).
2. Copy it into `AlphaBabes/voice-samples/`.
3. Rename it to match the pattern above (same Pass + Scene name as the
   picture it belongs to).
4. `git add -f` (voice-samples may need -f depending on .gitignore).
5. Commit + push immediately. No asking, no delay.

## If multiple takes of the SAME scene exist

If Nir records more than one take/version for the same scene, add a simple
`-v2`, `-v3` suffix at the very end (still no "Voice"/"Sample" word):

```
Fable-Pass-01-Scene-01-The-Alpha-in-the-Void-v2.mp3
```
