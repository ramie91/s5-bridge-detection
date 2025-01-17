from Debut import recupMain
from testGPT import conseil_carte_bridge_bref_Ench, conseil_tour_suivant
import json

# Fonction pour générer un jeu de cartes complet
def generer_jeu_de_cartes():
    valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    enseignes = ['c', 'd', 'h', 's']
    return set(f"{valeur}{enseigne}" for valeur in valeurs for enseigne in enseignes)

# Initialiser les structures de données pour les cartes disponibles et les comptages
cartes_disponibles = generer_jeu_de_cartes()
carte_count = {carte: 0 for carte in cartes_disponibles}

# Chemins vers les vidéos pour chaque direction
flux_nord = "Nord.mp4"
flux_sud = "Sud.mp4"
flux_est = "Est.mp4"
flux_ouest = "Ouest.mp4"

# Mains initiales vides
main_nord = []
main_sud = []
main_est = []
main_ouest = []

# Récupérer les mains à partir des vidéos
main_nord = recupMain(main_nord, flux_nord, cartes_disponibles=cartes_disponibles, carte_count=carte_count)
main_sud = recupMain(main_sud, flux_sud, cartes_disponibles=cartes_disponibles, carte_count=carte_count)
main_est = recupMain(main_est, flux_est, cartes_disponibles=cartes_disponibles, carte_count=carte_count)
main_ouest = recupMain(main_ouest, flux_ouest, cartes_disponibles=cartes_disponibles, carte_count=carte_count)

print(main_nord)
print(main_sud)
print(main_est)
print(main_ouest)

# Évaluer les mains en utilisant GPT
evaluation_nord = conseil_carte_bridge_bref_Ench(main_nord)
evaluation_sud = conseil_carte_bridge_bref_Ench(main_sud)
evaluation_est = conseil_carte_bridge_bref_Ench(main_est)
evaluation_ouest = conseil_carte_bridge_bref_Ench(main_ouest)

# Afficher les évaluations pour chaque main
print("Évaluation pour la main Nord:", evaluation_nord)
print("Évaluation pour la main Sud:", evaluation_sud)
print("Évaluation pour la main Est:", evaluation_est)
print("Évaluation pour la main Ouest:", evaluation_ouest)

# Initialiser un dictionnaire pour stocker l'historique du jeu
# Initialize a dictionary to store the game history
historique_jeu = {
    "mains": {},
    "evaluations": {},
    "cartes_jouees": [],
    "encheres": [],
    "conseils": {}
}


# Function to record in the history for each player
def enregistrer_dans_historique(joueur, carte_jouee, enchere, main, evaluation):
    historique_jeu["mains"][joueur] = main
    historique_jeu["evaluations"][joueur] = evaluation
    historique_jeu["cartes_jouees"].append({"joueur": joueur, "carte": carte_jouee})
    historique_jeu["encheres"].append({"joueur": joueur, "enchere": enchere})

    # Generate advice based on current game state
    conseil = conseil_tour_suivant([carte_jouee], [enchere], mains=historique_jeu["mains"],
                                   evaluations=historique_jeu["evaluations"])
    historique_jeu["conseils"][joueur] = conseil


# Record complete with hands and evaluations for each player
enregistrer_dans_historique("Nord", "AH", "1C", main_nord, evaluation_nord)
enregistrer_dans_historique("Sud", "2D", "1D", main_sud, evaluation_sud)
enregistrer_dans_historique("Est", "KS", "1H", main_est, evaluation_est)
enregistrer_dans_historique("Ouest", "10C", "1S", main_ouest, evaluation_ouest)


# Save the game history in a JSON file
def sauvegarder_historique():
    with open("historique_jeu.json", "w", encoding='utf-8') as f:
        json.dump(historique_jeu, f, indent=4)


sauvegarder_historique()


# Function to load the game history after saving
def charger_historique():
    with open("historique_jeu.json", "r", encoding='utf-8') as f:
        return json.load(f)


historique = charger_historique()

# Extract bids from the history
encheres_actuelles = [enchere["enchere"] for enchere in historique["encheres"]]

# Send played cards for advice
for action in historique["cartes_jouees"]:
    joueur = action["joueur"]
    carte = action["carte"]

    # Pass the card and current bids
    conseil = conseil_tour_suivant([carte], encheres_actuelles)

    print(f"Conseil pour {joueur} avec la carte {carte} : {conseil}")
