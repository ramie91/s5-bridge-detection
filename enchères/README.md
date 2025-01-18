# Description des fichiers pour le projet d'enchères de cartes

## Fichiers de modèle et de données

- **best2.pt** : Fichier de modèle YOLO pré-entraîné utilisé pour la détection des cartes d'enchères dans les vidéos.
- **enchere_data.json** : Fichier JSON qui stocke les résultats de la détection, incluant la liste des cartes détectées, les différentes phases d'enchères, et la dernière carte valide identifiée comme "enchère gagnante".

## Scripts Python

- **enchere3.mp4** : Vidéo source utilisée pour la détection des cartes d'enchères, simulant une séquence d'enchères dans un jeu de cartes pour tester et valider la capacité du modèle à reconnaître et suivre les phases d'enchères.
- **test_Enchere_Cam.py** : Script spécifique pour tester la reconnaissance de cartes via caméra.
- **testEnchere.py** : Script principal utilisé pour l'exécution de la détection des enchères via la vidéo, utilisant le modèle YOLO. Ce script gère le flux vidéo, la reconnaissance des cartes, l'assemblage des phases d'enchères, et la sauvegarde des résultats.

## Fichiers HTML et JavaScript

- **testTabEnch.html** : Page web qui est utilisée pour afficher les résultats des enchères de manière interactive. Cette page web charge les données depuis `enchere_data.json` à l'aide du fichier JavaScript associé.
- **script.js** : Fichier JavaScript qui lit les données d'enchères depuis le fichier `enchere_data.json` et les présente de manière structurée et interactive dans la page HTML `testTabEnch.html`. Ce script organise les données d'enchères et permet une visualisation claire des différentes phases d'enchères et de la carte gagnante.

## Description détaillée du fonctionnement de testEnchere.py

Le script `testEnchere.py` utilise OpenCV et YOLO pour analyser une vidéo d'enchères de cartes (`enchere3.mp4`). Il détecte les cartes à chaque phase d'enchères, gère la transition entre les phases, et identifie les passes successives. Si trois passes ("PA") consécutives sont détectées après une carte valide, la phase d'enchères se termine, et les résultats sont sauvegardés dans `enchere_data.json`. Ce fichier contient une liste complète des cartes détectées pendant la vidéo, les différentes phases d'enchères enregistrées, et l'identification de la dernière enchère valide comme gagnante.

