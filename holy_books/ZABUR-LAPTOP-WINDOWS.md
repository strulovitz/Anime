# ZABUR-LAPTOP-WINDOWS — THE BOOK OF THE AI COMPOSER'S DESK
Version 2.0 — 2026-07-24. v1.0 wrongly reduced this machine to a
listening station; Nir corrected the doctrine: a 20,000 NIS machine is
not headphones — it is a COMPOSER. LAW: no fact without a source (Nir's
words, live output, or dated Google AI search research). Updates only
with permission from Nir or Fable, by dated line edits. The QURAN always
outranks this book.

## PART 0 — THE DOCTRINE OF THE TWO STUDIOS (source: Nir, 2026-07-24)

Both Windows machines are FULL music production studios. Both get:
Adobe Premiere 23, Ableton Live 12, Omnisphere 2 by Spectrasonics,
Syncthing, and the ableton-mcp bridge. Nir owns all software. The
division is not by tools but by SOUL:
- The living room (Desktop, see INJIL) is where the HUMAN becomes a
  musician: VR piano learning, real hands on the Yamaha P-515.
- The bedroom (this machine) is where the AI becomes one: MCP-driven
  composition, MIDI processing, natural-language orchestration.
Two studios means true parallelism: both can produce music at the same
time, and each can edit in Premiere when the other is busy. This
technique — zero sheet music, zero music theory, just MIDI files, VR,
and AI — is itself a vibe-anime invention meant to be repeatable in
many homes by future vibe-anime artists.

## PART 1 — THE MACHINE AND THE ROOM

Same physical laptop as SUHUF (RTX 5090 Max-Q 24 GB, 64 GB RAM),
Windows 11 side. STATE (source: Nir, 2026-07-23): factory reset,
deliberately EMPTY — disk space reserved for the project. Location: the
bedroom, connected to an external DAC and amplifier, both by Schiit
(schiit.com) — the most truthful listening chain in the project.

## PART 2 — THE AI COMPOSER STACK (source: Google AI research, 2026-07-24)

THE MCP BRIDGE — DECIDED: the ORIGINAL ahujasid/ableton-mcp (NOT the
-extended fork). Reason: it works through strict, predefined
JSON-over-TCP commands and cannot run unchecked scripts on the machine
— the same safety philosophy as our DeepSeek whitelists. The -extended
fork is more powerful but requires managing hybrid TCP/UDP servers —
wrong for a beginner setup; revisit only if a hard wall is hit.

INSTALLATION RECIPE (from research, verify at install time):
1. Download init.py from the ahujasid/ableton-mcp GitHub repository.
2. Place it in a new folder named AbletonMCP inside:
   %USERPROFILE%\Documents\Ableton\User Library\Remote Scripts\
3. In Ableton: Settings -> Link, Tempo & MIDI -> Control Surface =
   AbletonMCP, Input and Output = None.
4. Install the uv Python package manager; register the server in the AI
   client's MCP config with command "uvx", args ["ableton-mcp"].

THE OMNISPHERE RITUAL (critical limitation + workaround): MCP CANNOT
load third-party VST plugins by name — Ableton's API only loads stock
devices and saved presets. The one-time ritual: Nir manually loads
Omnisphere 2 onto a MIDI track, dials in an instrument, and saves it as
an Ableton Instrument Rack preset (.adg) in the User Library. Do this
once per orchestral role and name them clearly: "Omni-SoloViolin",
"Omni-Harp", "Omni-LowStrings", "Omni-Choir", etc. From then on the AI
loads these racks freely by name, forever. The rack library IS the
orchestra; growing it is part of the craft.

WHAT THE AI CAN DO through MCP (verified by research): create tracks
and clips, write/edit/delete notes, set tempo, load .adg racks. It
CANNOT trigger Ableton's "Import MIDI" dialog — instead the AI reads
the MIDI file from disk (filesystem access), parses the notes, and
reconstructs them inside a new clip via add_notes. Same result.

THE MIDI PROCESSING PIPELINE (the assembly line of the orchestra):
[Raw public-domain classical piano MIDI]
1. CLEANUP: Python script using miditoolkit — delete ghost notes (e.g.
   velocity < 10), fix overlapping notes. Fable vibe-codes these helper
   scripts; Nir runs them with simple instructions.
2. QUANTIZE: Magenta Studio (free, Google, runs inside Ableton as Max
   for Live) — its Groove tool linearizes rubato and slow human timing
   onto a steady grid without killing expression. This is also how
   Nir's own slow P-515 performances (recorded in the living room,
   arriving here via Syncthing) get tightened when wanted.
3. SEPARATE: Python musicpy library, split_all() — splits one piano
   MIDI into Melody.mid, Chords.mid, Bass.mid. Fallback for clean
   left/right-hand pieces: pretty_midi with a simple pitch threshold.
4. ORCHESTRATE: the AI, commanded in plain English by Nir ("give the
   melody to the solo violin, the chords to the harp, slow the bridge
   down"), distributes the parts across Omni racks via MCP.
Python + uv must be installed on this machine for steps 1, 3 and the
MCP server. Which AI client hosts the MCP here: TO DECIDE at install
time (research current options; decision gets a dated line here).

## PART 3 — THE GOLDEN EARS (kept from v1.0 — a feature, not identity)

THE BEDROOM TEST (project law): no sound ships without passing this
room. Every voice take, every mix, every finished episode is judged
through the Schiit chain by Nir's ears. The Studio and the Desk create;
the bedroom chain confesses the truth about what they made.

THE CROWNING OF MADIE'S VOICE happens here: the desktop Linux machine
(see TAWRAT) generates candidate voices with Qwen3-TTS (decided
2026-07-24 by Google AI research: it designs brand-new voices from pure
text description — "a 22-year-old female anime character, speaking
English with a clear Romanian accent" — Apache 2.0 license, ~3-6 GB
VRAM). Every candidate reads the SAME audition lines: her name, a
tender line, a commanding line, and one line about borscht soup
(warmth is judged where warmth lives). Nir crowns the winner by ear;
the winning seed .wav becomes Madie's permanent voice — recorded in
TAWRAT with engine, settings and date, as sacred as her LoRA.

THE SUBTITLE DESK: Aegisub (installed by Nir), ENGLISH subtitles only,
crafted here in quiet. Hard-coding via AviDemux, done by Nir — he
knows how; do not micromanage him.

## PART 4 — ALPHA BABES (deadline ~August 3, 2026 — TOP PRIORITY)

Gift duties, in priority order: (1) crown Madie's voice; (2) QC every
audio element and the final mix; (3) English subtitles for Episode 1;
(4) THE FINAL WATCH-THROUGH — the complete episode, start to finish,
in this room, as Madie will experience it, before it is given. If time
allows: the Desk's first AI orchestration — a short Scheherazade
phrase (Madie's leitmotif, see INJIL) for the title card.

## PART 5 — COSMIC CHRYSALIS
Not started. Future duties: AI-composed score in a colder, vaster
classical style; voice work and QC for its characters. Nothing begins
before Madie's gift is done.

## PART 6 — MAZES & MAGES
Not started. Future duties: heaviest use of this Desk — dungeon
ambiences, magical textures, monster voices, AI-orchestrated battle
music. Nothing begins before Madie's gift is done.
