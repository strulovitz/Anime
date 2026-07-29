# 🔧 Sonnet Report — Blender MCP Config Fix (2026-07-29 midday)

## PROBLEM FOUND
After the OpenCode restart, Sonnet had NO Blender MCP tools available at all
(no `execute_blender_code`, no screenshot tool, nothing). Diagnosed why:

- `blender-mcp` package requires `mcp[cli]>=1.3.0`
- `uvx blender-mcp` (no version pin) resolved the NEWEST `mcp` package = 2.0.0
- `mcp` 2.0.0 restructured its internals and REMOVED `mcp.server.fastmcp`
- `blender_mcp/server.py` imports `from mcp.server.fastmcp import FastMCP, Context, Image`
- Result: `blender-mcp` crashed on startup with `ModuleNotFoundError: No module
  named 'mcp.server.fastmcp'` — so the MCP server never came up, and OpenCode
  never got any tools from it.

## FIX APPLIED
Changed `~/.config/opencode/opencode.jsonc` blender MCP command from:
```
"command": ["uvx", "blender-mcp"]
```
to:
```
"command": ["uvx", "--with", "mcp[cli]<2.0", "blender-mcp"]
```
This pins `mcp` to the last 1.x line (which still has `server.fastmcp`) while
letting `blender-mcp` itself stay unpinned/latest.

## VERIFIED WORKING
Ran manually in terminal:
```
uvx --with "mcp[cli]<2.0" blender-mcp --help
```
Output confirmed:
- Server started up cleanly
- Connected to Blender at localhost:9876 (the bridge Nir opened earlier is
  STILL LIVE — no need to reconnect in Blender)
- Successfully got telemetry consent + polyhaven status responses
- Clean shutdown, no errors

## CURRENT STATE
- `opencode.jsonc` is fixed and saved.
- Blender is still open on Nir's desktop, BlenderMCP addon still connected,
  port 9876 still live.
- **A SECOND OpenCode restart is required** so THIS session's fresh process
  picks up the corrected MCP command and actually loads the Blender tools.
- Once restarted, tools like `execute_blender_code`, `get_scene_info`, viewport
  screenshot, etc. should appear in Sonnet's toolset automatically (as MCP
  tools, no explicit mention needed in the system prompt — they'll just show
  up).

## EXACT NEXT STEPS AFTER THIS RESTART (unchanged from before, just delayed
one more restart because of this bug fix):
Read `AlphaBabes/Fable-Medusa-Blender-Scene-Mission-2026-07-29.md` and do, IN
ORDER:

- **STEP 0**: Using Blender MCP tools, create a UV sphere at (0,0,0) with
  glossy red material, take a viewport screenshot to confirm the bridge
  actually works end-to-end, then DELETE the test sphere.
- **STEP 1**: Execute the full Python script (between SCRIPT BEGIN/END
  markers in that file) in a SINGLE `execute_blender_code` MCP call. Do NOT
  modify creatively — only fix Blender 5.2 API-compat errors if they occur,
  and report every fix made.
- **STEP 2**: Take a viewport screenshot, verify: 4 mirror-disc drones in
  zigzag, 5 red beam segments forming a "W" from attacker ship through all 4
  drones to target ship, white glow at every bounce, background drones
  facing varied directions.
- **STEP 3**: Render via TERMINAL (bash), NOT through MCP (avoids MCP
  timeout):
  ```
  blender -b ~/medusa/medusa_scene.blend -f 1
  ```
  Output: `~/medusa/medusa_render_0001.png` (may take minutes on CPU).
- **STEP 4**: Report to Nir: any API fixes made, script console output, full
  path of rendered PNG. Save report as a new `.md` file in the Anime repo,
  push, give Nir a normal `github.com/.../blob/...` link (per the NEW RULE in
  AGENTS.md about long outputs).

## IF STILL NO BLENDER TOOLS AFTER THIS RESTART
1. Check `uvx --with "mcp[cli]<2.0" blender-mcp --help` still works standalone
   in terminal (confirms the fix itself, isolated from OpenCode).
2. Check OpenCode's own MCP server logs/status if available (may need a
   `/mcp` command or similar in the OpenCode CLI to list connected servers).
3. Double check `~/.config/opencode/opencode.jsonc` still has the pinned
   command (should NOT have been reverted).
4. Confirm Blender's BlenderMCP panel still says "running on port 9876" (if
   Blender itself was closed/restarted, port needs reconnecting via the N
   panel > BlenderMCP tab > Connect).
