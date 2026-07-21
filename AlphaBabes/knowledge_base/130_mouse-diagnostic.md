# Mouse Diagnostic Report
**Date:** 2026-07-21

## Issue A: TUI mouse/copy within OpenCode

**Previous fix:** Created `~/.config/opencode/tui.json` with `"mouse": false`
This disabled mouse tracking in OpenCode's terminal UI so native copy/paste works.
Since then: `Shift+drag` = text selection in terminal, `Ctrl+Shift+C` = copy.

**New doctrine:** Never copy long outputs from screen. Every mission ends with
"write the full report to a knowledge_base file and push." Copy from
github.com/strulovitz/Anime in Firefox with normal mouse instead.

## Issue B: Right-click not working in Debian

**Root cause:** GNOME touchpad default is `click-method = 'fingers'`
(two-finger-tap = right-click) instead of the expected `areas`
(bottom-right corner = right-click).

**Fix applied:**
```
gsettings set org.gnome.desktop.peripherals.touchpad click-method areas
```

**After:** Bottom-right corner of touchpad = right-click.

## Issue C: Every terminal shortcut brings same OpenCode window

**Fix:** `Ctrl+Shift+N` = new terminal window, `Ctrl+Shift+T` = new tab.
These are grabbed by the terminal before OpenCode sees them.

## Diagnostic summary

| Check | Result |
|-------|--------|
| `gsettings click-method` (before) | `fingers` |
| `gsettings click-method` (after fix) | `areas` ✅ |
| `gsettings tap-to-click` | `true` |
| `~/.Xmodmap` | Not present |
| `/etc/udev/rules.d/` | Empty |
| `xinput` | Not available (Wayland) |
| OpenCode TUI mouse | Disabled (`"mouse": false` in tui.json) |