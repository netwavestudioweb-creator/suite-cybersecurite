#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SecurePassGen — Générateur de mots de passe sécurisé (interface console)
========================================================================
Suite Cybersécurité — projet éducatif.
"""
import sys

from generator import generer_mot_de_passe
from strength_checker import entropie, evaluer_force

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def demander_oui_non(question: str, defaut: bool = True) -> bool:
    reponse = input(question).strip().lower()
    if reponse == "":
        return defaut
    return reponse in ("o", "oui", "y", "yes")


def demander_longueur(defaut: int = 12, minimum: int = 8) -> int:
    brut = input(f"Longueur du mot de passe (min {minimum}, défaut {defaut}) : ").strip()
    if brut == "":
        return defaut
    try:
        valeur = int(brut)
    except ValueError:
        print("⚠️  Valeur non numérique — utilisation de la valeur par défaut.")
        return defaut
    return max(valeur, minimum)


def main() -> None:
    print("🔐 Générateur de mots de passe sécurisé\n")

    longueur = demander_longueur()
    maj = demander_oui_non("Inclure MAJUSCULES ? (o/n) [o] : ")
    minusc = demander_oui_non("Inclure minuscules ? (o/n) [o] : ")
    chiffres = demander_oui_non("Inclure CHIFFRES ? (o/n) [o] : ")
    symboles = demander_oui_non("Inclure SYMBOLES ? (o/n) [o] : ")

    try:
        pwd = generer_mot_de_passe(longueur, maj, minusc, chiffres, symboles)
    except ValueError as err:
        print("❌ Erreur :", err)
        return

    e = entropie(pwd)
    print("\n🧾 Mot de passe généré :", pwd)
    print("🔐 Entropie :", e, "bits")
    print("📊 Force :", evaluer_force(e))


if __name__ == "__main__":
    main()
