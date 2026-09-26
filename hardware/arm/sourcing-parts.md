# Sourcing Parts — SO-101 Arm (Follower + Leader)

> Based on the [SO-ARM100](https://github.com/TheRobotStudio/SO-ARM100#sourcing-parts) by TheRobotStudio.  
> Sourced from France. Prices as of early 2025.

---

## Servos — Feetech STS3215

6× per arm (12× total for follower + leader).

| Supplier | Link | Unit price | Notes |
|---|---|---|---|
| Alibaba (Shenzhen Feite) | https://www.alibaba.com/product-detail/Top-Seller-Low-Cost-Feetech-STS3215_1600999461525.html | ~$14 | Pack of 6 — best price, ~2–3 weeks shipping |

> Order from AliExpress mirror if Alibaba MOQ is an issue.  
> Spec: 7.4V, 19kg·cm, magnetic encoder, 0–360°, half-duplex UART.

---

## Electronics

| Part | Link | Price | Notes |
|---|---|---|---|
| Waveshare Serial Bus Servo Driver | https://www.amazon.fr/dp/B0CJ6TP3TP | ~20€ | USB-C, compatible STS3215 |
| Alimentation 5V (bloc secteur) | https://www.amazon.fr/dp/B07BNF842T | ~12€ | Powering the servo bus |
| Câbles USB-C (lot de 2) | https://www.amazon.fr/dp/B08S6Z7S4V | ~8€ | |

---

## Fixation & Assemblage

| Part | Link | Price | Notes |
|---|---|---|---|
| Serres-joints rapides (lot de 4) | https://www.amazon.fr/dp/B01HRR9GY4 | ~6€ | Fixation bras sur table |
| Câble de remplacement | https://www.amazon.fr/dp/B0CLRJZG8D | ~6€ | Remplacement câble servo endommagé |

---

## Caméra (optionnel pour le wrist)

| Part | Link | Price | Notes |
|---|---|---|---|
| Innomaker 720P USB UVC | Amazon (déjà acheté) | ~24€ | Config: index 0, 640×480, 30fps |

---

## Total estimé par bras

| | Follower | Leader |
|---|---|---|
| Servos (×6) | ~84$ | ~84$ |
| Électronique | ~40€ | ~20€ (controller partagé possible) |
| Fixation | ~12€ | ~12€ |
| **Total** | **~130€** | **~100€** |

---

## Notes terrain

- Les STS3215 d'Alibaba (commande #24528848600...) : livraison Frankfurt — **tentative échouée**, à surveiller ou recommander sur AliExpress.
- Le câble du servo **wrist_roll (ID 5)** a été endommagé pendant le montage du follower — servo fonctionnel mais fixation fragile.
- Commander 1–2 câbles de rechange dès le départ.
