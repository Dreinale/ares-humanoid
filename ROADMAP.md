# ARES — Roadmap

> Ce fichier est la source de vérité du projet. Mis à jour à chaque étape franchie.  
> Dernière mise à jour : 2026-09-26

---

## Statut global

```
[Phase 1] Upper body ████░░░░░░ 20%
[Phase 2] Simulation  ██░░░░░░░░ 10%
[Phase 3] Training    ░░░░░░░░░░  0%
```

---

## Phase 1 — Upper Body (Buste)

### 1.1 — Bras follower SO-101 ✅ DONE
- [x] Impression 3D
- [x] Assemblage + câblage STS3215
- [x] Code téléoperate adapté (sans leader)
- [x] Tests fonctionnels

### 1.2 — Bras leader SO-101 🔄 EN COURS
- [ ] Impression des pièces (`3D - SO-ARM100/Leader/`)
- [ ] Assemblage + câblage
- [ ] Test téléoperate follower ↔ leader
- [ ] Calibration position nulle

### 1.3 — Dexhand (main droite)
- [ ] Lire le BOM complet : https://github.com/TheRobotStudio/V1.0-Dexhand
- [ ] Commander 12× STS3215
- [ ] Impression pièces (PETG recommandé)
- [ ] Assemblage + câblage
- [ ] Intégration sur bras follower
- [ ] Test préhension basique

### 1.4 — Buste / Thorax
- [ ] Définir la structure (InMoov base ou custom)
- [ ] Concevoir fixation épaules gauche/droite
- [ ] Impression + assemblage
- [ ] Intégration des 2 bras sur buste

### 1.5 — Tête
- [ ] Structure imprimée (InMoov head ou custom)
- [ ] Caméra stéréo RGB (perception)
- [ ] Montage sur buste

---

## Phase 2 — Simulation MuJoCo

### 2.1 — Setup ✅ DONE
- [x] MuJoCo 3.14 installé
- [x] Build `simulate.exe` depuis les sources
- [x] Test viewer + physique basique

### 2.2 — MJCF Bras SO-101
- [ ] Créer le modèle MJCF du follower arm
- [ ] Valider la cinématique dans `simulate`
- [ ] Ajouter le leader arm + contrainte téléoperate

### 2.3 — MJCF Dexhand
- [ ] Modéliser les 12 DOF de la main
- [ ] Tester la préhension en sim

### 2.4 — MJCF Buste complet
- [ ] Assembler tous les sous-modèles
- [ ] Scène de téléoperate complète

---

## Phase 3 — Training LeRobot

### 3.1 — Collecte de données
- [ ] Setup pipeline d'enregistrement LeRobot
- [ ] Enregistrer 50+ démos de tâches simples (pick & place)
- [ ] Pusher dataset sur HuggingFace Hub

### 3.2 — Training
- [ ] Fine-tune ACT (Action Chunking Transformer)
- [ ] Évaluer en simulation
- [ ] Évaluer sur le vrai robot

### 3.3 — Publication
- [ ] Publier le modèle entraîné sur HuggingFace Hub
- [ ] Publier le hardware sur HuggingFace Hub
- [ ] Rédiger un article de présentation

---

## Backlog / Idées futures

- [ ] Jambes (quadrupède ou bipède)
- [ ] Navigation autonome
- [ ] Intégration ROS2
- [ ] Contribution ESA robotics

---

## Journal

| Date | Événement |
|---|---|
| 2026-09-26 | MuJoCo installé et testé. Bras follower SO-101 fonctionnel. Roadmap initialisée. |

---

> Pour ajouter une entrée au journal : date + une ligne de ce qui a été fait/décidé.
