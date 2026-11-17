# -*- coding: utf-8 -*-
"""Génération de mots de passe — moteur cryptographiquement sûr (module `secrets`)."""
import secrets
import string


def generer_mot_de_passe(longueur: int = 12, majuscules: bool = True,
                         minuscules: bool = True, chiffres: bool = True,
                         symboles: bool = True) -> str:
    """
    Génère un mot de passe aléatoire sécurisé.

    Utilise `secrets` (générateur cryptographique) plutôt que `random`, et
    garantit la présence d'au moins un caractère de chaque classe sélectionnée.
    """
    classes: list[str] = []
    if majuscules:
        classes.append(string.ascii_uppercase)
    if minuscules:
        classes.append(string.ascii_lowercase)
    if chiffres:
        classes.append(string.digits)
    if symboles:
        classes.append(string.punctuation)

    if not classes:
        raise ValueError("Aucun type de caractères sélectionné !")

    # Au moins un caractère par classe choisie.
    longueur = max(longueur, len(classes))

    mot = [secrets.choice(classe) for classe in classes]
    tous_les_caracteres = "".join(classes)
    mot += [secrets.choice(tous_les_caracteres) for _ in range(longueur - len(mot))]

    secrets.SystemRandom().shuffle(mot)
    return "".join(mot)
