# Claude Fable 5 — Blender MCP Setup Instructions (2026-07-29)

Excellent research haul! :-) And good news first, to address your worry directly: the recommended path gives you a 100% normal, full Blender — the official build from blender.org, with the complete GUI, that you can open from your menu and use like any artist. The MCP part is just a regular add-on inside it. Nothing crippled. In fact there's a bonus you'll enjoy: this MCP works with Blender's window open, so you will literally watch the scene build itself live in the viewport — drones appearing, beams connecting — and you can orbit the camera with your mouse while Sonnet works. 🙂

Before the plan, I must flag three errors in Google's answers (I warned you they contradict each other):

1. Version contradiction: Answers 1 and 2 say blender-mcp supports Blender 3.0+. Answer 4 says it requires "Blender 5.1+" — that claim (and the "Official Blender Lab MCP") smells hallucinated. The 3.0+ figure matches the project's actual README. Resolution: we install the latest stable from blender.org, which satisfies every claim, and Sonnet will verify the README's real requirement during setup.
2. Broken command: `curl -LsSf https://astral.sh | sh` is wrong — that's just the homepage. The real uv installer is `https://astral.sh/uv/install.sh`. Corrected below.
3. Wrong config example: The SSE-on-port-8000 example is generic fiction. ahujasid's blender-mcp is a local stdio server launched with `uvx blender-mcp`, which then talks to the Blender add-on over port 9876. Correct config below.

## Our stack (decided)

- ahujasid/blender-mcp — free, open source, ~23k stars, and critically: it has the execute_blender_code tool, which is exactly what Answer 5 recommends — the single-script strategy. I write one complete scene script; Sonnet delivers it in one shot; the scene builds atomically. No 15-command state-corruption spiral, no context bloat.
- The commercial options solve problems we don't have. Skip.

## Step 1 — Paste this mission brief into OpenCode (Sonnet 5 does the work)

Please set up the Blender MCP toolchain on this Linux Mint 22 machine. Work
step by step and report results:

1. Install uv/uvx via the official installer:
   `curl -LsSf https://astral.sh/uv/install.sh | sh`
   Then verify with: `uvx --version`

2. Download the latest stable Blender for Linux x64 as the official tar.xz
   from blender.org (NOT apt, NOT flatpak). Extract it to
   `~/.local/share/blender`, symlink the binary to `~/.local/bin/blender`
   (create `~/.local/bin` if needed), and register its .desktop file so it
   appears in the system application menu. This must remain a full normal
   GUI installation.

3. Clone https://github.com/ahujasid/blender-mcp to `~/tools/blender-mcp`.
   Read its README and report: the minimum Blender version it actually
   requires, and the exact current installation instructions, in case they
   differ from what follows.

4. Install and enable its addon.py in Blender non-interactively: run
   blender in background mode with a small Python script that calls
   `bpy.ops.preferences.addon_install()` on the addon.py file, enables the
   addon, and saves user preferences.

5. Add the MCP server to my OpenCode config at
   `~/.config/opencode/opencode.json` — MERGE with existing content, do not
   overwrite. The entry should be:
   ```
   "mcp": { "blender": { "type": "local",
            "command": ["uvx", "blender-mcp"], "enabled": true } }
   ```

6. Report: Blender version installed, uv version, addon enabled yes/no,
   and the final opencode.json content.

## Step 2 — The only two clicks in the universe you'll do (once per session)

1. Open Blender from your menu (your normal Blender!).
2. Press N in the 3D viewport → find the BlenderMCP tab in the sidebar → click Start/Connect server.

That's Blender being a normal desktop application, not us doing homework — same as opening OpenCode itself.

## Step 3 — Verify the bridge

Restart OpenCode (so it loads the new config), then tell Sonnet:

Using the blender MCP tools, create a UV sphere at (0, 0, 0) with a glossy
red material, and take a viewport screenshot to confirm you can see it.

If a red sphere appears in your Blender window — the bridge is alive. 🎉

## One honest caution + our timeout plan

- Answer 5 is right that long Cycles renders can breach MCP timeouts. Already handled: I'll write our scene script so heavy renders save the .blend and launch the render as a detached background process, returning control immediately. Automatic, no freeze, no crash.
- Also true: this MCP executes arbitrary code with your user's permissions. Our rule: Sonnet only runs scripts that I author. No improvisation on scene code.

Report back with Sonnet's results from Step 1 (especially the README's real version requirement), and the moment the red sphere test passes, my next message is the full Medusa scene — trapezoid formation, computed mirror angles, the perfect "W" beam. ♟️🔧
