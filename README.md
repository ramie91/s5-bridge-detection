# Projet Bridge et Enchères

Ce projet regroupe deux modules principaux : 
1. **Cartes** : Gestion et reconnaissance des cartes.
2. **Enchères** : Simulation et détection des enchères dans un jeu de cartes.

---

## Table des Matières

- [Introduction](#introduction)
- [Prérequis](#prérequis)
- [Structure du Projet](#structure-du-projet)
- [Installation](#installation)
- [Utilisation](#utilisation)
  - [Module Cartes](#module-cartes)
  - [Module Enchères](#module-enchères)
- [Contribuer](#contribuer)

---

## Introduction

Ce projet propose une solution complète pour la reconnaissance de cartes dans un jeu de bridge et pour la simulation des enchères. Il combine des algorithmes de vision par ordinateur (via des modèles préentraînés comme YOLO) et une interface web interactive pour afficher les résultats.

## Prérequis

- Python 3.11+
- Bibliothèques Python : OpenCV, PyTorch, etc.
- Un navigateur web compatible (pour afficher les résultats interactifs)

## Structure du Projet

```
project-root/
├── cartes/
│   ├── Debut.py
│   ├── Est.mp4
│   ├── Nord.mp4
│   ├── Ouest.mp4
│   ├── PID5N0s.pt
│   ├── README.md
│   ├── Sud.mp4
│   ├── historique_jeu.json
│   ├── main.html
│   ├── main.py
│   ├── script.js
│   ├── testGPT.py
│   ├── test_Carte_Cam.py
├── enchères/
│   ├── README.md
│   ├── best2.pt
│   ├── enchere3.mp4
│   ├── enchere_data.json
│   ├── script.js
│   ├── testEnchere.py
│   ├── testTabEnch.html
│   ├── test_Enchere_Cam.py
```

- **cartes/** : Module de reconnaissance de cartes pour le bridge.
- **enchères/** : Module de simulation et détection des enchères.

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/ramie91/s5-bridge-detection.git
   ```
2. Accédez au répertoire :
   ```bash
   cd s5-bridge-detection
   ```
3. Installez les dépendances Python :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

### Module Cartes

Le module `cartes` permet de reconnaître les cartes des joueurs à partir de vidéos :

1. Lancez le script principal :
   ```bash
   python cartes/main.py
   ```
2. Consultez les résultats dans la page web `cartes/main.html`.

Les vidéos de chaque joueur (à l'Est, Nord, Ouest et Sud) sont traitées pour identifier les cartes et générer un fichier `historique_jeu.json`.

### Module Enchères

Le module `enchères` gère la reconnaissance des enchères dans les vidéos :

1. Lancez le script principal :
   ```bash
   python enchères/testEnchere.py
   ```
2. Les résultats sont sauvegardés dans `enchères/enchere_data.json`.
3. Affichez les enchères dans la page web interactive :
   ```bash
   open enchères/testTabEnch.html
   ```

## Contribuer

1. Forkez le projet.
2. Créez une branche pour vos modifications :
   ```bash
   git checkout -b feature/nouvelle-fonctionnalite
   ```
3. Soumettez une Pull Request.

