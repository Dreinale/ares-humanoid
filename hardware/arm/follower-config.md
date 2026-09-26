# Follower Arm — Configuration & Calibration

> À conserver précieusement. Changer les IDs servo nécessite de démonter le bras.

---

## Port série

```
COM4
```

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

## Problème connu

- **Servo wrist_roll (ID 5)** : câble d'origine cassé pendant le montage. Servo fonctionnel mais fixation fragile.
- Commander un câble de rechange avant toute session intensive : https://www.amazon.fr/dp/B0CLRJZG8D

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
- [ ] Brancher USB controller sur COM4
- [ ] Lancer calibration : `python lerobot/scripts/control_robot.py --config-name=config_calilbrate`
- [ ] Vérifier que les 6 joints répondent
- [ ] Test mouvement complet shoulder → gripper
