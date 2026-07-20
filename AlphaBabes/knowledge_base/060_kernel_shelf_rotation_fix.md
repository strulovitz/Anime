# NVIDIA Driver Install — Phase 2 Error Report
**Date:** 2026-07-20

---

## Command executed
```
sudo apt install linux-headers-6.12.85+deb13-amd64 linux-headers-amd64 build-essential dkms -y
```

## Result: PARTIAL FAILURE

### What succeeded:
- ✅ `build-essential` — already installed (12.12)
- ✅ `dkms` — already installed (3.2.2-1)
- ✅ `linux-headers-6.12.94+deb13-amd64` — fetched from trixie/main
- ✅ `linux-headers-6.12.94+deb13-common` — fetched
- ✅ `linux-headers-amd64` metapackage — fetched
- ✅ `linux-kbuild-6.12.94+deb13` — fetched

### What FAILED (404 Not Found):
These packages were in the Debian **security** repo and have been **rotated out**:
```
Err:1 http://security.debian.org/debian-security trixie-security/main
      linux-headers-6.12.85+deb13-common  6.12.85-1  → 404 Not Found

Err:2 http://security.debian.org/debian-security trixie-security/main
      linux-kbuild-6.12.85+deb13  6.12.85-1  → 404 Not Found

Err:3 http://security.debian.org/debian-security trixie-security/main
      linux-headers-6.12.85+deb13-amd64  6.12.85-1  → 404 Not Found
```

## Running kernel
```
6.12.85+deb13-amd64
```

## Installed headers now
```
6.12.94+deb13-amd64  (newer than running kernel — can't build against these)
```

## The problem
The NVIDIA DKMS build needs headers matching the **running** kernel (6.12.85), but those headers were purged from the Debian security repo. The headers we DO have installed (6.12.94) are for a kernel that isn't running yet.

## Options for Claude Fable to consider:
1. **Boot into 6.12.94** — if `linux-image-6.12.94+deb13-amd64` is available (it was pulled as a dependency), install it, reboot into 6.12.94, then run the NVIDIA installer against matching headers.
2. **Try `apt update` first** — maybe the security repo metadata is stale and a refresh would redirect to the right path.
3. **Try the installer against 6.12.94 headers anyway** — unlikely to work; DKMS builds against `/lib/modules/$(uname -r)/build`.
4. **Download headers from Debian snapshot** — the 6.12.85 packages may still exist at snapshot.debian.org.
5. **Skip DKMS and do a one-shot build** — `--no-dkms` and let the installer build just for 6.12.85 using whatever kbuild infrastructure is available.

## What was NOT touched
- `/usr/local/cuda*` — untouched
- conda environments — untouched
- venvs — untouched
- `/etc/apt/sources.list` — untouched

---

# Fable's Decision: Kernel Shelf Rotation Fix

Not a disaster — just Debian being Debian. Plain-language version of what happened: the security repo only stocks the newest kernel's parts. Between the agent's pre-flight (which saw 6.12.85 headers listed) and the actual download, the shelf was restocked: 6.12.85 was rotated out, 6.12.94 took its place. The pre-flight wasn't wrong; the shelf moved.

## The right move: Option 1 (with a pinch of Option 2 first)

Don't chase the discontinued part (snapshot.debian.org = Option 4) — that pins you to an aging kernel and recreates the fragility we're trying to kill. Instead, step forward onto 6.12.94. Look at what's already sitting on disk:

- Headers for 6.12.94: ✅ already installed (the "useless" packages from the failure are about to become exactly what we need)
- Metapackages for future auto-matching: ✅ installed

So the only missing piece is the 6.12.94 kernel image itself. Install it, reboot into it, and suddenly running kernel and headers match perfectly — then the NVIDIA installer proceeds as originally planned.

### Safety notes for your peace of mind:

- Your current kernel 6.12.85 is **not removed** — it stays in the GRUB boot menu as a fallback. If 6.12.94 misbehaves (very unlikely; this is a routine Debian stable security update), you boot back into 6.12.85 via "Advanced options" and nothing is lost.
- Your pinned environments live in user-space (conda, venvs, CUDA toolkit, torch wheels) — a minor kernel revision bump (6.12.85→6.12.94) is invisible to them. The things kernel updates can break are exactly kernel modules like the NVIDIA driver — which is why we're installing it WITH DKMS after landing on the new kernel, so it's born matched.

Options 3 and 5: correctly rejected — DKMS builds against the running kernel, and a `--no-dkms` one-shot build resurrects the exact disease this machine died of last time.

---

## Paste this to the laptop agent

**DECISION FROM CLAUDE FABLE:** Option 1 (move to kernel 6.12.94), with `apt update` first. Same strict whitelist as before, plus kernel image install. Same rules: one step at a time, explain each, STOP on errors.

### PHASE 2b — kernel alignment:
1. `sudo apt update`
2. `apt-cache policy linux-image-amd64 linux-image-6.12.94+deb13-amd64` — confirm the 6.12.94 image is available. Report before installing.
3. `sudo apt install linux-image-amd64` — this pulls the 6.12.94 kernel image. Do NOT remove or autoremove any old kernels; 6.12.85 must remain in GRUB as fallback.
4. Tell the user to reboot. Explain: if the system fails to boot normally, choose "Advanced options for Debian" in the GRUB menu and select the 6.12.85 kernel to get back to safety.

### PHASE 2c — after reboot (user says "continue nvidia mission, phase 2c"):
5. Verify: `uname -r` → must show `6.12.94+deb13-amd64`. If it doesn't, STOP.
6. Run the installer exactly as previously approved:
   ```
   sudo sh ~/nvidia-driver/NVIDIA-Linux-x86_64-580.95.05.run --dkms --kernel-module-type=open --no-x-check
   ```
   (YES to DKMS, YES to 32-bit libs if asked, NO to nvidia-xconfig/X changes)
7. Tell the user to reboot once more.

### PHASE 3 — after second reboot ("continue nvidia mission, phase 3"):
8. `nvidia-smi` → must show GeForce RTX 5090, Driver 580.95.05, CUDA 13.0
9. `lsmod | grep nvidia` → modules present
10. `dkms status` → nvidia module "installed" for 6.12.94
11. Report and end mission. Touch nothing else.

**Yes, two reboots** — one to board the new kernel, one to wake the driver. Boring and correct beats clever and fragile. 🐢

And for the archive before you switch machines: `060_kernel_shelf_rotation_fix.md`. This whole 404 saga is precisely the institutional memory that will save future-you hours when a kernel update someday shuffles the shelf again.

Bring me that nvidia-smi screenshot-of-glory. ⏱️🎨