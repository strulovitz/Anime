# G4c REPORT — NVIDIA Driver Debug & MOK Re-Enrollment (2026-07-22 evening)

## Mission
nvidia-smi failed. Driver 595.71.05 installed & DKMS-built but not loading.

## VERBATIM ERROR
```
NVIDIA-SMI has failed because it couldn't communicate with the NVIDIA driver.
Make sure that the latest NVIDIA driver is installed and running.
```

---

## Full Investigation Log

### 1. Checked kernel modules loaded
```
lsmod | grep nvidia
```
**Result:** NOTHING. Zero nvidia modules loaded.

### 2. Checked DKMS status
```
dkms status
```
**Result:**
```
nvidia/595.71.05, 6.14.0-37-generic, x86_64: installed
```
Driver is built for the running kernel. Good.

### 3. Checked Secure Boot
```
mokutil --sb-state
```
**Result:** `SecureBoot enabled`
This is the root cause.

### 4. Confirmed GPU on PCI bus
```
lspci | grep -i nvidia
```
**Result:**
```
01:00.0 VGA compatible controller: NVIDIA Corporation AD104 [GeForce RTX 4070 Ti] (rev a1)
01:00.1 Audio device: NVIDIA Corporation Device 22bc (rev a1)
```
GPU is physically detected.

### 5. Checked running kernel vs DKMS kernel
```
uname -r
```
**Result:** `6.14.0-37-generic` — matches DKMS build. Good.

### 6. Verified module files exist
```
ls /lib/modules/6.14.0-37-generic/updates/dkms/nvidia*
```
**Result:** All 5 modules present:
- nvidia.ko.zst (6.6MB)
- nvidia-drm.ko.zst
- nvidia-modeset.ko.zst
- nvidia-peermem.ko.zst
- nvidia-uvm.ko.zst

### 7. Tried manual modprobe
```
sudo modprobe nvidia
```
**Result:**
```
modprobe: ERROR: could not insert 'nvidia': Key was rejected by service
```
Secure Boot rejecting the signed module.

### 8. Found MOK keys
Located at `/var/lib/shim-signed/mok/MOK.priv` and `/var/lib/shim-signed/mok/MOK.der`

### 9. FIRST ATTEMPT: Manual re-signing (FAILED — caused corruption)
Tried `sign-file` directly on the `.ko.zst` files. This appended signature bytes to the zstd-compressed module, corrupting the zstd format. All modules became unreadable.

### 10. DKMS CLEAN REBUILD
```
sudo dkms remove nvidia/595.71.05 -k 6.14.0-37-generic
sudo dkms install nvidia/595.71.05 -k 6.14.0-37-generic
```
DKMS rebuilt all modules from source AND automatically signed them using the MOK key at `/var/lib/shim-signed/mok/`. Build output confirmed:
```
Signing module /var/lib/dkms/nvidia/595.71.05/build/nvidia.ko
[... all 5 modules signed ...]
```

### 11. Still rejected after rebuild
```
sudo modprobe nvidia
modprobe: ERROR: could not insert 'nvidia': Key was rejected by service
```
Modules are signed but the MOK key is NOT ENROLLED in the system firmware.

### 12. Checked MOK enrollment
```
sudo mokutil --test-key /var/lib/shim-signed/mok/MOK.der
```
**Result:** `/var/lib/shim-signed/mok/MOK.der is not enrolled`

```
sudo keyctl list %:.builtin_trusted_keys
sudo keyctl list %:.secondary_trusted_keys
```
The `.machine` keyring is EMPTY — no MOK key present.

### 13. Confirmed module signing key matches MOK key
```
modinfo nvidia | grep sig_key
sig_key: 1B:12:05:4A:3E:F2:98:1F:77:6B:4E:0F:D7:05:23:9F:0F:EA:25:52
```
This serial number matches the MOK certificate subject key identifier.

### 14. RE-ENROLLED MOK (SUCCESS)
```
printf '%s\n' '12345678' '12345678' | sudo mokutil --import /var/lib/shim-signed/mok/MOK.der
```
**Result:** Key imported successfully.

### 15. Confirmed pending enrollment
```
sudo mokutil --list-new
```
Shows the MOK key fingerprint `61:6f:82:ca:22:a6:9f:ca:af:60:05:2f:f0:b8:71:15:bf:bc:43:7d` is pending enrollment.

---

## CURRENT STATE

| Item | Status |
|------|--------|
| Driver | nvidia-driver-595-open 595.71.05 |
| DKMS | Built for 6.14.0-37-generic |
| Modules signed | YES (with correct MOK key) |
| MOK enrolled | PENDING — needs reboot + blue screen enrollment |
| GPU | RTX 4070 Ti on PCI |
| Secure Boot | ENABLED |
| MOK password | `12345678` |

---

## NEXT STEP (After Reboot)

During boot, the **blue MOK management screen** will appear. User must:

1. Select **Enroll MOK**
2. Select **Continue**
3. Select **Yes** to enroll the key
4. Enter password: `12345678`
5. Select **Reboot**

After boot, run:
```
nvidia-smi
```
Should show RTX 4070 Ti with driver 595.71.05. Then continue to G5 (Miniforge3).

---

## WHAT WENT WRONG (retrospective)

1. MOK key was created and modules signed during initial G4b setup, but the MOK enrollment step in the blue screen was either skipped or not persisted.
2. Secure Boot remained ON throughout.
3. First recovery attempt (`sign-file` on `.ko.zst` directly) corrupted the modules because `sign-file` doesn't understand zstd compression — you MUST build through DKMS or decompress→sign→compress manually.
4. DKMS rebuild was the correct fix — it builds, signs, and compresses properly in one shot.
5. The missing piece was `mokutil --import` which was never completed properly last time.