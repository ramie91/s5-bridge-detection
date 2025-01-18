import json

import cv2
from ultralytics import YOLO

model = YOLO('best2.pt')  # Remplacez par le chemin vers votre modèle .pt
#cap = cv2.VideoCapture('0113.mp4')
cap = cv2.VideoCapture(0)
# Dictionnaire pour compter les occurrences de chaque classe
card_count = {}

# Sauter des frames pour accélérer le traitement
frame_skip = 5  # Modifier ce nombre pour sauter plus ou moins de frames

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        print("Erreur lors de la capture de l'image")
        break

    # Sauter des frames
    if frame_count % frame_skip != 0:
        frame_count += 1
        continue

    results = model(frame)  # Appliquer la détection YOLO

    # Récupération des boîtes, des IDs de classe et des scores de confiance
    boxes = results[0].boxes
    class_ids = boxes.cls
    scores = boxes.conf

    for box, class_id, score in zip(boxes.xyxy, class_ids, scores):
        x1, y1, x2, y2 = map(int, box)
        label = results[0].names[int(class_id)]

        # Compter les occurrences de chaque carte
        if label in card_count:
            card_count[label] += 1
        else:
            card_count[label] = 1

        # Dessiner et afficher les résultats sur la frame
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(frame, f"{label} ({score:.2f})", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    cv2.imshow('Detection des cartes', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_count += 1

cap.release()
cv2.destroyAllWindows()

# Afficher les résultats finaux
print(json.dumps(card_count, indent=4))
