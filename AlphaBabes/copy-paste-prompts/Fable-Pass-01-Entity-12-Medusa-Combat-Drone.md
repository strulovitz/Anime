# Entity #12 — Combat Reflector Drone, "Obol Mk.II" (Medusa production)

Double-sided precision mirror + equatorial equipment ring. 2.2 m dia, 350 kg wet.

## Layout
- Core: monolithic sintered SiC disc; both faces polished, dielectric-coated
  (R > 99.995% @ 1030 nm, valid incidence 10°–55°). Core IS the structure.
- Each face: ~120 piezo actuators (figure control + slight refocus curvature).
- Equator ring: 4x CMGs (~160 N·m cluster), 2x propellant tanks, 12x 22 N
  green-monoprop thrusters (canted pairs: translate without rotating),
  2x star trackers, FOG IMU, corner-cube retroreflectors, laser crosslink
  heads, edge radiators + heat pipes, Li-SOCl2 primary batteries (72 h).

## Performance
- Worst-case slew (90°, two faces): ~2.0 s + ~0.1 s piezo settle.
- Pointing: 2 µrad body knowledge via formation laser metrology
  (reflection doubles error — this budget is the whole game).
- Δv ≈ 1.26 km/s. 100 m reposition ≈ 45 s. Moves are turn-based by physics.
- Thermal: ~100 W absorbed per 2 MW relayed; rejected via rim radiators.
  Outside 10°–55° incidence, absorption spikes — illegal angles burn drones.

## Doctrine
Expendable. Bare metal, no lights, no recovery hardware. Serial number only.