# NVIDIA Driver Install — Phase 1 Pre-flight Report
**Date:** 2026-07-20

---

## Goal
Install NVIDIA driver from existing downloaded installer:
`~/nvidia-driver/NVIDIA-Linux-x86_64-580.95.05.run`

Phase 2 commands to run (NOT YET EXECUTED):
```
sudo apt install linux-headers-amd64 build-essential dkms
sudo sh ~/nvidia-driver/NVIDIA-Linux-x86_64-580.95.05.run --dkms --kernel-module-type=open --no-x-check
```

---

## Pre-flight Results

| Check | Status | Detail |
|-------|--------|--------|
| Installer exists & integrity | ✅ OK | `check sums and md5 sums are ok` |
| gcc | ✅ 14.2.0 | `gcc (Debian 14.2.0-19) 14.2.0` |
| make | ✅ 4.4.1 | `GNU Make 4.4.1` |
| nouveau blacklisted | ✅ | `/etc/modprobe.d/blacklist-nouveau.conf` exists with `blacklist nouveau` and `options nouveau modeset=0` |

### Kernel & headers detail

| Item | Value |
|------|-------|
| Running kernel | `6.12.85+deb13-amd64` |
| `linux-headers-amd64` metapackage candidate | `6.12.94-1` (newer than running kernel) |
| `linux-headers-6.12.85+deb13-amd64` | Available from `trixie-security/main` |

## ⚠️ Key concern before proceeding

The command `apt install linux-headers-amd64` pulls the **latest** headers (currently for kernel 6.12.94), **not** headers for the currently running kernel (6.12.85). The NVIDIA DKMS build compiles the kernel module against the **running** kernel's headers, so it needs `linux-headers-6.12.85+deb13-amd64` specifically.

### Question for Claude Fable:
Should the Phase 2 command be changed to:
```
sudo apt install linux-headers-6.12.85+deb13-amd64 build-essential dkms
```
...instead of `linux-headers-amd64`? Or should BOTH be installed? The metapackage will pull a newer kernel's headers that won't help this build. The exact-version package `linux-headers-6.12.85+deb13-amd64` is confirmed available from the security repo.

---

# Fable's Answer: Install BOTH Header Packages

Superb catch by the laptop agent — this is exactly the class of bug that quietly kills driver installs, and it deserves a precise answer:

## Answer: install BOTH header packages

```
sudo apt install linux-headers-6.12.85+deb13-amd64 linux-headers-amd64 build-essential dkms
```

### Why both — each one solves a different problem:

| Package | What it solves |
|---------|---------------|
| `linux-headers-6.12.85+deb13-amd64` (exact version) | **Today's build.** DKMS compiles the NVIDIA module against the running kernel's blueprint. Without these exact headers, tonight's install fails or builds for the wrong kernel. |
| `linux-headers-amd64` (metapackage) | **Every future upgrade.** When `apt upgrade` eventually moves the kernel to 6.12.94 (or beyond), this metapackage automatically pulls the matching headers alongside it — so DKMS can auto-rebuild the NVIDIA module for the new kernel before you reboot into it. |

Skipping the metapackage would re-create the exact historical failure of this machine: kernel marches forward (6.12.43 → … → 6.12.85, as we saw), module doesn't follow, and one morning `nvidia-smi` is dead again. The metapackage + DKMS pair is the vaccine against that. The 6.12.94 headers it brings today are harmless — they just sit there until that kernel arrives.

## Corrected Phase 2 (everything else unchanged)

```
sudo apt install linux-headers-6.12.85+deb13-amd64 linux-headers-amd64 build-essential dkms
sudo sh ~/nvidia-driver/NVIDIA-Linux-x86_64-580.95.05.run --dkms --kernel-module-type=open --no-x-check
```

All other pre-flight results look clean and green: installer checksum ✅, gcc 14.2 ✅, make ✅, nouveau already blacklisted ✅ (more archaeology confirming past-you's prep work). No other objections — the plan stands.

**Nir: relay this answer to the laptop agent, and if you're satisfied, give it the "go". Phase 3 (reboot + nvidia-smi verification) as planned.**

And yes — this exchange belongs in the knowledge base too (050_headers_correction.md). An agent that pauses to double-check with the architect before pulling the trigger is a workflow worth immortalizing. 🎯