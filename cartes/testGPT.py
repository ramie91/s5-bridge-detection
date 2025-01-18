import cv2
from ultralytics import YOLO
import openai

# Set your OpenAI API key
openai.api_key = "YOUR-API-KEY"
def conseil_carte_bridge_bref_Ench(main):
    if not main or not isinstance(main, list):
        return "Aucune carte détectée ou format incorrect."

    cards_str = ', '.join(main)
    prompt = f"Je joue au bridge et j'ai cette main : {cards_str}. Quelle enchère me conseillez-vous de faire en français ?"

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Vous êtes un expert en bridge et vous devez donner des conseils brefs."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

def conseil_tour_suivant(cartes_jouees, encheres, mains=None, evaluations=None):
    if not cartes_jouees or not isinstance(cartes_jouees, list):
        return "Aucune carte jouée détectée ou format incorrect."

    if not encheres or not isinstance(encheres, list):
        return "Aucune enchère détectée ou format incorrect."

    cartes_str = ', '.join(cartes_jouees)
    encheres_str = ', '.join(encheres)

    mains_str = "\n".join([f"{joueur}: {', '.join(cartes)}" for joueur, cartes in (mains or {}).items()])
    evaluations_str = "\n".join([f"{joueur}: {commentaire}" for joueur, commentaire in (evaluations or {}).items()])

    prompt = (
        f"Je joue au bridge. Voici les cartes qui ont été jouées : {cartes_str}.\n"
        f"Voici les enchères actuelles : {encheres_str}.\n"
        f"Voici les mains des joueurs :\n{mains_str}\n"
        f"Voici les évaluations des mains :\n{evaluations_str}\n"
        f"Dis-moi la prochaine carte à jouer pour chaque position sous forme : Carte à jouer, explication courte ne met pas d'accent 'é' dans la réponse FAIT UNE PHRASE MAX"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Vous êtes un expert en bridge et vous devez donner des conseils stratégiques."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']

# Example usage
'''
main_test = ['As', 'Kd', 'Qs', 'Jh', '10c', '9d', '8s', '7h', '6c', '5d', '4s', '3h', '2c']
advice = conseil_carte_bridge_bref_Ench(main_test)
print("Conseil d'enchère pour la main:", advice)
'''