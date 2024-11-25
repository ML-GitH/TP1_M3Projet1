#  password_analysis.py 
import re
# Demande à l'utilisateur d'entrer un mot de passe
password = input("Entrez un mot de passe : ")

# Vérifier la longueur du mot de passe
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