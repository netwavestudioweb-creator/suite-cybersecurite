# -*- coding: utf-8 -*-
"""
Contrôle d'accès simple par mot de passe — CryptoTool (projet éducatif).

Au premier lancement, le mot de passe saisi est enregistré (haché en SHA-256) ;
aux lancements suivants, il est demandé pour déverrouiller l'outil.

Note pédagogique : un vrai système stockerait le hachage avec un SEL (salt) et
un algorithme lent dédié aux mots de passe (ex. bcrypt / argon2).
"""
import hashlib
import os

# Fichier de hachage stocké à côté de ce script (et non dans le dossier courant).
FICHIER_HASH = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".passwd_hash")


def hasher_mdp(mot_de_passe: str) -> str:
    return hashlib.sha256(mot_de_passe.encode("utf-8")).hexdigest()


def enregistrer_mdp(mot_de_passe: str) -> None:
    with open(FICHIER_HASH, "w", encoding="utf-8") as f:
        f.write(hasher_mdp(mot_de_passe))


def verifier_mdp(saisi: str) -> bool:
    if not os.path.exists(FICHIER_HASH):
        print("🔐 Aucun mot de passe enregistré — création du mot de passe maître.")
        enregistrer_mdp(saisi)
        return True
    with open(FICHIER_HASH, "r", encoding="utf-8") as f:
        hash_enregistre = f.read().strip()
    return hasher_mdp(saisi) == hash_enregistre
