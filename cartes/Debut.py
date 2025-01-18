import cv2
from ultralytics import YOLO

# Fonction pour générer un jeu de cartes complet
# Crée une fonction pour générer l'ensemble complet des cartes si ce n'est pas déjà fait
'''def generer_jeu_de_cartes():
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    enseignes = ['c', 'd', 'h', 's']  # Coeurs, Carreaux, Trèfles, Piques
    return set(f"{valeur}{enseigne}" for valeur in valeurs for enseigne in enseignes)

# Crée l'ensemble de cartes disponibles et le compteur de cartes
cartes_disponibles = generer_jeu_de_cartes()
carte_count = {carte: 0 for carte in cartes_disponibles}
'''

# Fonction principale pour récupérer les cartes à partir d'une vidéo
def recupMain(main, flux, frame_skip=5, cartes_disponibles=None, carte_count=None):
    model = YOLO('PID5N0s.pt')
    cap = cv2.VideoCapture(flux)
    if not cap.isOpened():
        print("Erreur : Impossible d'ouvrir le flux vidéo.")
        return None  # Retourne None si le flux ne peut pas être ouvert

    frame_count = 0
    try:
        while len(main) < 13:
            ret, frame = cap.read()
            if not ret:
                print("Erreur lors de la capture de l'image")
                break

            if frame_count % frame_skip != 0:
                frame_count += 1
                continue

            results = model(frame)
            boxes = results[0].boxes
            class_ids = boxes.cls
            scores = boxes.conf

            for box, class_id, score in zip(boxes.xyxy, class_ids, scores):
                if score < 0.5:
                    continue
                label = results[0].names[int(class_id)]

                if label in cartes_disponibles and carte_count[label] < 3:
                    carte_count[label] += 1
                    if carte_count[label] == 3:
                        cartes_disponibles.remove(label)
                        main.append(label)
                        if len(main) == 13:
                            break

            frame_count += 1
    finally:
        cap.release()
        cv2.destroyAllWindows()
    return main  # Retourne la main complétée à la fin de la fonction

'''
# Initialisation des mains, des cartes disponibles et du compteur pour chaque carte
cartes_disponibles = generer_jeu_de_cartes()
carte_count = {carte: 0 for carte in cartes_disponibles}
main_nord = []
main_sud = []
main_est = []
main_ouest = []

# Appel de la fonction pour chaque main avec les vidéos respectives
recupMain(main_nord, 'Nord.mp4', cartes_disponibles=cartes_disponibles, carte_count=carte_count)
recupMain(main_sud, 'Sud.mp4', cartes_disponibles=cartes_disponibles, carte_count=carte_count)
recupMain(main_est, 'Est.mp4', cartes_disponibles=cartes_disponibles, carte_count=carte_count)
recupMain(main_ouest, 'Ouest.mp4', cartes_disponibles=cartes_disponibles, carte_count=carte_count)

# Affichage des résultats
print("Cartes dans main_nord :", main_nord)
print("Cartes dans main_sud :", main_sud)
print("Cartes dans main_est :", main_est)
print("Cartes dans main_ouest :", main_ouest)
print("Cartes restantes :", cartes_disponibles)  # Cartes non détectées ou en excès
'''