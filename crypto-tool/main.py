#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CryptoTool — (dé)chiffrement de fichiers par XOR (projet éducatif)
==================================================================
Suite Cybersécurité.

⚠️  Le XOR n'est PAS un chiffrement sûr — usage pédagogique uniquement
    (voir l'avertissement dans crypto_engine.py).
"""
import sys

from crypto_engine import chiffrer_fichier, dechiffrer_fichier
from security import verifier_mdp

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def menu() -> None:
    print("=== CryptoTool (éducatif — XOR non sécurisé) ===")
    print("1. Chiffrer un fichier")
    print("2. Déchiffrer un fichier")
    choix = input("Ton choix (1 ou 2) : ").strip()

    if choix not in ("1", "2"):
        print("❌ Choix invalide.")
        return

    mot_de_passe = input("🔑 Mot de passe maître : ")
    if not verifier_mdp(mot_de_passe):
        print("❌ Mot de passe incorrect.")
        return

    src = input("📄 Fichier source : ").strip()
    if not src:
        print("❌ Aucun fichier source.")
        return
    dst = input("💾 Fichier de sortie : ").strip()
    if not dst:
        print("❌ Aucun fichier de sortie.")
        return
    cle = input("🗝️  Clé de chiffrement : ")

    try:
        if choix == "1":
            chiffrer_fichier(src, dst, cle)
            print(f"✅ Fichier chiffré et sauvegardé : {dst}")
        else:
            dechiffrer_fichier(src, dst, cle)
            print(f"🔓 Fichier déchiffré et sauvegardé : {dst}")
    except FileNotFoundError:
        print(f"❌ Fichier introuvable : {src}")
    except ValueError as err:
        print(f"❌ Erreur : {err}")
    except Exception as err:  # garde-fou pédagogique
        print(f"❌ Échec de l'opération : {err}")


if __name__ == "__main__":
    menu()
