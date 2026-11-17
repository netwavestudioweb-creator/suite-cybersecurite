#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Détecteur local de brute-force — Suite Cybersécurité (projet éducatif)
=====================================================================

Analyse un fichier de logs et repère les adresses IP qui dépassent un seuil
de tentatives de connexion échouées (comportement typique d'une attaque par
force brute).

But : DÉFENSE / détection. Outil pédagogique d'analyse de journaux.

Format de log attendu (une ligne par évènement) :
    [2025-08-05 09:00:01] IP: 192.168.1.10 - Tentative échouée - utilisateur: admin

Exemples :
    python detecteur.py
    python detecteur.py -f logs.txt -s 5
    python detecteur.py -f /var/log/auth.log -s 10 --verbose
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from collections import defaultdict

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Expression régulière : capture l'adresse IPv4 d'une ligne.
REGEX_IP = re.compile(r"IP:\s*(\d{1,3}(?:\.\d{1,3}){3})")
MARQUEUR_ECHEC = "Tentative échouée"

# Chemin par défaut : fichier logs.txt situé à côté de ce script.
LOG_PAR_DEFAUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs.txt")


def analyser_logs(chemin: str, verbose: bool = False) -> dict[str, int]:
    """Compte les tentatives échouées par adresse IP."""
    tentatives: dict[str, int] = defaultdict(int)

    with open(chemin, "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            if MARQUEUR_ECHEC in ligne:
                match = REGEX_IP.search(ligne)
                if match:
                    ip = match.group(1)
                    tentatives[ip] += 1
                    if verbose:
                        print(f"➕ Échec détecté : {ip} ({tentatives[ip]})")
    return tentatives


def rapport(tentatives: dict[str, int], seuil: int) -> list[str]:
    """Affiche les IP suspectes et renvoie la liste des IP signalées."""
    suspectes = sorted(
        ((ip, n) for ip, n in tentatives.items() if n >= seuil),
        key=lambda x: x[1],
        reverse=True,
    )

    print(f"\n🚨 IP suspectes (≥ {seuil} tentatives échouées) :")
    if suspectes:
        for ip, n in suspectes:
            print(f"   - {ip} : {n} tentatives")
    else:
        print("   Aucune IP suspecte détectée. ✅")

    return [ip for ip, _ in suspectes]


def construire_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Détecteur local de brute-force par analyse de logs (éducatif).")
    parser.add_argument("-f", "--fichier", default=LOG_PAR_DEFAUT,
                        help="Chemin du fichier de logs (défaut : logs.txt du projet)")
    parser.add_argument("-s", "--seuil", type=int, default=5,
                        help="Seuil d'alerte (nb de tentatives, défaut : 5)")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Affiche chaque échec détecté")
    return parser


def main() -> None:
    args = construire_parser().parse_args()

    if not os.path.exists(args.fichier):
        raise SystemExit(f"❌ Fichier de logs introuvable : {args.fichier}")

    print(f"📄 Analyse de : {args.fichier}")
    tentatives = analyser_logs(args.fichier, verbose=args.verbose)
    rapport(tentatives, args.seuil)


if __name__ == "__main__":
    main()
