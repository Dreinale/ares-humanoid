# ARES-humanoid — Autonomous Robotic Embodied System

> Named after the Greek god of war — and the planet Mars.  
> Built for Earth. Designed to reach further.

ARES is a fully open-source humanoid robot built from scratch with a 3D printer, off-the-shelf servos, and a laptop. The goal: a capable upper-body humanoid that can be teleoperated, trained via imitation learning, and eventually deployed autonomously.

Built on the [LeRobot](https://github.com/huggingface/lerobot) ecosystem (HuggingFace). Designed to be shared, forked, and improved by the community.

---

## Vision

- Full upper-body humanoid (2× arms + hands + torso + head)
- Dexterous manipulation via teleoperation
- Trained with ACT / Diffusion Policy on HuggingFace
- Open-source hardware + software — publishable on HuggingFace Hub
- Long-term: contribute to space robotics research (ESA)

---

## Current State

- [x] SO-101 follower arm — functional
- [x] MuJoCo simulation environment set up
- [ ] SO-101 leader arm (in progress)
- [ ] Dexhand integration
- [ ] Torso + head structure

---

## Hardware Stack

| Component | Model | Role |
|---|---|---|
| Servos | Feetech STS3215 | All joints |
| Controller | Feetech USB Serial Bus | Servo communication |
| SBC | Raspberry Pi / Jetson | Onboard compute |
| Camera | Stereo RGB | Head perception |
| Printer | FDM (PETG) | Structural parts |

---

## Software Stack

| Layer | Tool |
|---|---|
| Simulation | MuJoCo 3.x |
| Robot control | LeRobot (HuggingFace) |
| Training | ACT / Diffusion Policy |
| Firmware | Custom (C++ / Python) |
| Model sharing | HuggingFace Hub |

---

## Repository Structure

```
ares-humanoid/
├── hardware/          # STL files, assembly guides, BOM
│   ├── arm/
│   ├── hand/
│   ├── torso/
│   └── head/
├── simulation/        # MuJoCo MJCF models
├── software/          # Control, teleoperation, training scripts
├── docs/              # Build logs, notes, research
├── ROADMAP.md         # Current status + next steps
└── README.md
```

---

## Bill of Materials (Phase 1)

| Part | Qty | Unit | Total |
|---|---|---|---|
| STS3215 servo (leader arm) | 6 | ~15€ | ~90€ |
| STS3215 servo (Dexhand) | 12 | ~15€ | ~180€ |
| Feetech USB controller | 1 | ~20€ | ~20€ |
| PETG filament 1kg | 3 | ~20€ | ~60€ |
| Hardware (bearings, screws, cables) | — | — | ~30€ |
| **Phase 1 total** | | | **~380€** |

---

## References

- [SO-ARM100 / SO-101](https://github.com/TheRobotStudio/SO-ARM100) — TheRobotStudio
- [V1.0 Dexhand](https://github.com/TheRobotStudio/V1.0-Dexhand) — TheRobotStudio
- [LeRobot](https://github.com/huggingface/lerobot) — HuggingFace
- [MuJoCo](https://mujoco.org) — DeepMind
- [InMoov](https://inmoov.fr) — Gael Langevin

---

