# Follower Arm — Configuration & Calibration

> À conserver précieusement. Changer les IDs servo nécessite de démonter le bras.

---

## Port série

```
COM3
```

> Port identifié via `python -m lerobot.find_port` — peut varier selon le port USB utilisé. Toujours vérifier avant une session.

---

## Servo IDs

| Joint | ID | Modèle |
|---|---|---|
| shoulder_pan | 1 | STS3215 |
| shoulder_lift | 2 | STS3215 |
| elbow_flex | 3 | STS3215 |
| wrist_flex | 4 | STS3215 |
| wrist_roll | 5 | STS3215 |
| gripper | 6 | STS3215 |

---

## Calibration

Fichier de référence (backup) : `hardware/arm/calibration/enzo_follower_arm.json`

Source originale : `C:\Users\nzo\.cache\huggingface\lerobot\calibration\robots\so101_follower\enzo_follower_arm.json`

> ⚠️ Il existe un second fichier dans `Dev/Robot/~/lerobot/.cache/` avec des plages wrist_roll et gripper quasi nulles — calibration incomplète, **ne pas utiliser**.

---

## Problèmes connus

### Servo wrist_roll (ID 5) — câble cassé
Câble d'origine cassé pendant le montage. Servo fonctionnel mais fixation fragile.  
Commander un câble de rechange : https://www.amazon.fr/dp/B0CLRJZG8D

### Gripper (ID 6) — bloqué à 100%
Diagnostiqué lors des sessions d'entraînement ACT (août 2025).  
Le gripper reste en position fermée quelle que soit la commande envoyée.

```
Commande gripper: 0%   → Position: 100.00%
Commande gripper: 50%  → Position: 100.00%
Commande gripper: 100% → Position: 100.00%
```

**Causes possibles :**
- Obstruction mécanique (impression 3D, débris)
- Câble endommagé ou mal connecté sur ID 6
- Calibration incomplète (range_min/max quasi nuls dans l'ancien fichier de calibration)

**Action requise :** vérifier physiquement avant toute nouvelle session d'enregistrement.

---

## Config LeRobot

`Dev/Robot/Robot/config_calilbrate.yaml`

```yaml
robot:
  type: so100
  follower_arms:
    main:
      type: feetech
      port: "COM4"
      motors:
        shoulder_pan:  [1, "sts3215"]
        shoulder_lift: [2, "sts3215"]
        elbow_flex:    [3, "sts3215"]
        wrist_flex:    [4, "sts3215"]
        wrist_roll:    [5, "sts3215"]
        gripper:       [6, "sts3215"]
  leader_arms: {}
```

---

## Checklist test bras follower

Avant chaque session :

- [ ] Vérifier câble wrist_roll (ID 5) bien connecté
- [ ] Vérifier mécaniquement le gripper (ID 6) — obstruction ?
- [ ] Identifier le bon port : `python -m lerobot.find_port`
- [ ] Lancer calibration : `python -m lerobot.calibrate --robot.type=so101_follower --robot.port=COM3 --robot.id=enzo_follower_arm`
- [ ] Vérifier que les 6 joints répondent **y compris le gripper**
- [ ] Test mouvement complet shoulder → gripper

## Historique training ACT

- **Dataset** : `Dreinale/so101_demo_1` — 15 épisodes, 6656 frames
- **Policy** : `Dreinale/so101_demo_1_policy` — ACT, ResNet18, 65K steps
- **Loss finale** : 6.890 → 0.051
- **Résultat** : robot bouge de façon autonome, mais gripper non fonctionnel → dataset à refaire une fois le gripper réparé
