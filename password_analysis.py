#  password_analysis.py 
import re


# Boucle infinie pour continuer à demander un mot de passe jusqu'à ce qu'il soit robuste
while True:
    # Demande à l'utilisateur d'entrer un mot de passe
    password = input("Entrez un mot de passe : ")


    # Vérification des conditions
    if len(password) < 8:
        print("Le mot de passe doit contenir au moins 8 caractères.")
    elif not re.search(r"[A-Z]", password):
        print("Le mot de passe doit contenir au moins une majuscule.")
    elif not re.search(r"[0-9]", password):
        print("Le mot de passe doit contenir au moins un chiffre.")
    elif not re.search(r"[@#$%^&*!]", password):
        print("Le mot de passe doit contenir au moins un caractère spécial.")
    else:
        print("Le mot de passe est robuste.")
        break  # Sortir de la boucle lorsque le mot de passe est valide
