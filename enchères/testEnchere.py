import cv2
from ultralytics import YOLO
import json

def add_bidding_phase(current_phase, all_bidding_phases, directions):
    if current_phase:
        phase_name = f"Derniere phase {len(all_bidding_phases)}"
        phase_with_directions = {"nom": phase_name}
        for i, card in enumerate(current_phase):
            phase_with_directions[directions[i % 4]] = card
        all_bidding_phases.append(phase_with_directions)
        return current_phase[-1]  # Retourne la dernière carte de la phase actuelle

# Chargement du modèle YOLO pour la détection des cartes d'enchères
model = YOLO('best2.pt')

# Initialisation de la capture vidéo
cap = cv2.VideoCapture('enchere3.mp4')

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la vidéo.")
    exit()

frame_skip = 22
current_frame = 0
previous_cards = set()
all_bidding_phases = []
all_detected_cards = []
current_phase = []
pass_count = 0
last_valid_card = None
directions = ['N', 'E', 'S', 'O']
test = True
target_label = "PA"
target_class_id = None


while test:
    ret, frame = cap.read()
    if not ret:
        break

    if current_frame % frame_skip == 0:
        results = model.predict(source=frame, show=False, conf=0.70)

        for result in results:
            for box, score, label in zip(result.boxes.xyxy, result.boxes.conf, result.boxes.cls):
                label_name = model.names[int(label)]
                confidence = f"{score * 100:.2f}%"
                card_info = f"{label_name} ({confidence})"

                if label_name not in previous_cards or label_name == 'PA':
                    if label_name != 'PA':
                     all_detected_cards.append(card_info)
                    previous_cards.add(label_name)
                    current_phase.append(card_info)

                    if label_name == "PA":

                        pass_count += 1
                    else:
                        pass_count = 0  # Réinitialisation du compteur de "PA" pour toute carte non-"PA"
                        last_valid_card = card_info  # Mise à jour de la dernière carte valide

                    if pass_count == 3:
                        print("test-1")
                        if len(current_phase) > 3:
                            pass_count=0
                            #current_phase = current_phase[:-3]  # Enlever les "PA" de la phase actuelle
                            print("test-2")
                            add_bidding_phase(current_phase, all_bidding_phases, directions)
                            current_phase = []

                            test = False

                        break

                    if len(current_phase) == 4:
                        #last_valid_card = add_bidding_phase(current_phase, all_bidding_phases, directions)
                        current_phase = []

    cv2.imshow('Détection de cartes YOLOv8', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    current_frame += 1

cap.release()
cv2.destroyAllWindows()

# Traitement de toutes cartes restantes après la sortie de la boucle
if current_phase:
    add_bidding_phase(current_phase, all_bidding_phases, directions)

# Sauvegarde des données d'enchères
with open('enchere_data.json', 'w', encoding='utf-8') as file:
    json.dump({
        "Liste des cartes détecter au total": all_detected_cards,
        "enchere": all_bidding_phases,
        "enchere gagnante": last_valid_card
    }, file, indent=4)

print("Les données d'enchères et la liste des cartes détectées ont été sauvegardées dans 'enchere_data.json'.")
