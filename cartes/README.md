# Description des fichiers du projet de bridge

## Scripts Python

- **Debut.py** : Ce fichier est responsable du traitement d'image initial. Il configure et effectue la reconnaissance des cartes via les entrées vidéo, établissant ainsi les configurations ou les paramètres de début de jeu en préparant les données visuelles pour l'analyse et l'intégration ultérieures.
- **main.py** : Le script principal qui orchestre le chargement des mains, la génération de conseils, et la gestion de l'état du jeu. Il utilise les fonctions définies dans `testGPT.py` pour intégrer les réponses du modèle GPT d'OpenAI. Ces réponses sont utilisées pour fournir des conseils stratégiques basés sur les mains actuelles et les enchères en cours.
- **test_Carte_Cam.py** : Teste la fonctionnalité de reconnaissance de cartes via caméra, utilisée pour identifier les cartes jouées à partir des vidéos fournies.
- **testGPT.py** : Gère l'intégration et la réponse du modèle GPT dans le contexte du jeu. Les fonctions de ce fichier sont essentielles pour demander et traiter les conseils de l'API de Chat GPT, utilisées directement dans `main.py`.

## Fichiers de données et modèles

- **historique_jeu.json** : Un fichier JSON pour stocker l'historique du jeu, y compris les mains jouées, les enchères, et les conseils donnés. Ce fichier est alimenté par la reconnaissance des cartes via le modèle et les vidéos, ainsi que par les réponses générées par le modèle Chat GPT.

## Ressources multimédias

- **Est.mp4, Nord.mp4, Ouest.mp4, Sud.mp4** : Fichiers vidéo qui simulent le moment où l'on filme les mains des joueurs. Utilisés pour la reconnaissance des cartes des joueurs grâce à un modèle de vision par ordinateur, les résultats de cette reconnaissance sont ensuite utilisés pour alimenter `historique_jeu.json`.

## Autres fichiers

- **main.html** : Une page web utilisée pour simplifier la visualisation des résultats du jeu. Elle affiche les informations de manière claire et interactive grâce à un tableau mis à jour par le script JavaScript.
- **script.js** : Un fichier JavaScript qui charge et affiche dynamiquement les données de jeu depuis `historique_jeu.json` dans un tableau HTML. Il gère l'insertion des données de chaque joueur, telles que les mains, les cartes jouées, les enchères, les évaluations et les conseils. Un gestionnaire d'erreur est également inclus pour traiter les problèmes lors du chargement des données.

## Mains des joueurs

- **Main Nord :**
  - 2 de Cœur, 2 de Trèfle, Valet de Carreau, Roi de Carreau, As de Pique, 4 de Cœur, Dame de Carreau, 10 de Pique, Dame de Trèfle, As de Cœur, 4 de Carreau, 9 de Trèfle, Valet de Pique.
- **Main Sud :**
  - 3 de Carreau, 5 de Cœur, Valet de Trèfle, 4 de Trèfle, 6 de Cœur, 6 de Carreau, 7 de Carreau, 4 de Pique, 7 de Trèfle, 5 de Trèfle, Roi de Trèfle, 7 de Pique, As de Carreau.
- **Main Est :**
  - 5 de Pique, 6 de Trèfle, 10 de Cœur, 10 de Carreau, 2 de Carreau, Roi de Cœur, 3 de Trèfle, Dame de Pique, As de Carreau, Roi de Pique, 3 de Cœur, 8 de Pique, 8 de Carreau.
- **Main Ouest :**
  - 5 de Carreau, 2 de Trèfle, 10 de Trèfle, Dame de Cœur, 9 de Carreau, 8 de Cœur, 3 de Trèfle, 9 de Cœur, 9 de Pique, 8 de Trèfle, Valet de Cœur, 7 de Cœur, 6 de Pique.
