import cv2
from ultralytics import YOLO

# Charger le modèle YOLOv8
model = YOLO(
    r'encheres_final_run2\cartes_test_run\weights\best.pt')  # Remplacez par le chemin vers votre modèle .pt

# Ouvrir la caméra
cap = cv2.VideoCapture(0)  # 0 pour la caméra par défaut

while True:
    # Lire une image de la caméra
    ret, frame = cap.read()
    if not ret:
        print("Erreur lors de la capture de l'image")
        break

    # Appliquer la détection d'objets avec YOLOv8
    results = model(frame)  # Cela retourne une liste de résultats

    # Récupérer les boîtes englobantes, les classes et les scores de confiance
    boxes = results[0].boxes  # Liste des boîtes englobantes
    class_ids = boxes.cls  # Liste des identifiants des classes détectées (utilisez .cls)
    scores = boxes.conf  # Liste des scores de confiance

    # Parcourir les résultats pour dessiner les boîtes et afficher les classes
    for box, class_id, score in zip(boxes.xyxy, class_ids,
                                    scores):  # Utilisez .xyxy pour obtenir les coordonnées des boîtes
        x1, y1, x2, y2 = map(int, box)  # Coordonnées de la boîte englobante
        label = results[0].names[int(class_id)]  # Nom de la classe (par exemple "3 de trèfle")

        # Dessiner la boîte englobante sur l'image
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)  # Boîte en rouge

        # Afficher le label avec la confiance au-dessus de la boîte
        cv2.putText(frame, f"{label} ({score:.2f})",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (255, 0, 0), 2)

    # Afficher l'image avec les résultats
    cv2.imshow('Detection des cartes', frame)

    # Quitter lorsque la touche 'q' est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la caméra et fermer la fenêtre
cap.release()
cv2.destroyAllWindows()
