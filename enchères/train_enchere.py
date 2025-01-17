import torch
from ultralytics import YOLO
import os
import multiprocessing

# Forcer le démarrage des processus avec 'spawn' sous Windows
multiprocessing.set_start_method('spawn', force=True)

# Vérification de la disponibilité du GPU
if not torch.cuda.is_available():
    raise RuntimeError("Aucun GPU détecté ! Vérifiez CUDA et votre configuration.")

device = torch.device("cuda:0")  # Utiliser le GPU 0
print(f"Utilisation de l'appareil : {torch.cuda.get_device_name(0)}")

# Spécifier le chemin local où le dataset est situé
dataset_path = "encheres_final2"

# Construire le chemin absolu du fichier data.yaml
data_yaml_path = os.path.join(dataset_path, "data.yaml")

# Vérifier si le fichier data.yaml existe
if not os.path.exists(data_yaml_path):
    raise FileNotFoundError(f"Le fichier '{data_yaml_path}' n'existe pas. Vérifiez le chemin du dataset.")

# Charger le modèle YOLOv8
model = YOLO("yolov8m.pt")  # Utilisez "yolov8n.pt" (nano) pour débuter ou "yolov8x.pt" pour un modèle plus grand

# Entraîner le modèle
if __name__ == "__main__":
    print("Début de l'entraînement...")
    outut_path = "encheres_final_run3"
    model.train(
        data=data_yaml_path,
        epochs=100,
        imgsz=720,  # Taille des images (720x720)
        batch=8,
        device=0,
        patience=5,
        workers=8,
        project=outut_path,
        name="cartes_test_run",

    )

    print("Entraînement terminé avec succès !")