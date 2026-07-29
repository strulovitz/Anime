# Sonnet's Step 1 Report — Blender MCP Setup (2026-07-29)

## Report for Claude Fable

| Item | Result |
|---|---|
| **uv version** | 0.12.0 (official installer, `~/.local/bin`) |
| **uvx version** | 0.12.0 — verified working |
| **Blender version installed** | **5.2.0 LTS** (official tar.xz from blender.org, NOT apt/flatpak) |
| **Blender location** | `~/.local/share/blender` |
| **Blender binary symlink** | `~/.local/bin/blender` ✅ |
| **Desktop menu entry** | Registered at `~/.local/share/applications/blender.desktop`, validated with `desktop-file-validate` (no errors) ✅ |
| **blender-mcp cloned** | `~/tools/blender-mcp` ✅ |
| **README's real min version** | **Blender 3.0+** confirmed (the "5.1+" claim in Google's answer WAS hallucinated, Fable was right) |
| **README's Python requirement** | Python 3.10+ |
| **README's default port** | 9876 (matches Fable's info exactly) |
| **Addon installed & enabled** | **True** ✅ (installed via headless `bpy.ops.preferences.addon_install`, enabled, prefs saved) |
| **opencode.jsonc updated** | Merged (not overwritten) — final content below ✅ |

## Final opencode.jsonc content

```json
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": ["/home/nir/AGENTS.md"],
  "mcp": {
    "blender": {
      "type": "local",
      "command": ["uvx", "blender-mcp"],
      "enabled": true
    }
  }
}
```

## One discrepancy to flag for Fable

The README's own OpenCode example uses the key `"blender-mcp"` instead of `"blender"`. Sonnet used `"blender"` exactly as Fable instructed. Flagging in case it matters for tool-name recognition later.

## Next steps

- **Step 2 (Nir's two clicks):** Open Blender from the app menu, press `N` in the viewport, find the **BlenderMCP** tab, click **Connect/Start server**.
- **Step 3:** Restart OpenCode, then run the red sphere test.
