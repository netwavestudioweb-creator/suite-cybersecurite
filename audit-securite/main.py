#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Audit de fichiers sensibles — Suite Cybersécurité (projet éducatif)
==================================================================

Parcourt un dossier et repère les fichiers « exécutables » dont l'extension
est sensible (.sh, .py, .exe, .bat…), en affichant leurs permissions.

But : sensibilisation / audit défensif. Outil pédagogique.

Note : les bits de permission (lecture/écriture/exécution par propriétaire /
groupe / monde) sont une notion POSIX (Linux/macOS). Sous Windows, ils sont
peu significatifs ; le script se rabat alors sur l'extension du fichier.

Exemples :
    python main.py
    python main.py -c "C:/mon/dossier"
    python main.py -c /etc --ext .sh .py
"""
from __future__ import annotations

import argparse
import os
import stat
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

EXTENSIONS_SENSIBLES_DEFAUT = [".sh", ".py", ".exe", ".bat", ".ps1", ".cmd"]


def auditer(chemin: str, extensions: list[str]) -> int:
    """Audite un dossier. Renvoie le nombre de fichiers signalés."""
    extensions = [e.lower() for e in extensions]
    signales = 0

    print(f"\n🔍 Audit de : {os.path.abspath(chemin)}")
    print(f"   Extensions surveillées : {', '.join(extensions)}\n")

    for racine, _dirs, fichiers in os.walk(chemin):
        for fichier in fichiers:
            extension = os.path.splitext(fichier)[1].lower()
            if extension not in extensions:
                continue

            chemin_fichier = os.path.join(racine, fichier)
            try:
                stats = os.stat(chemin_fichier)
                permissions = stat.filemode(stats.st_mode)
                mode = stats.st_mode
                executable_par_tous = bool(mode & stat.S_IXOTH)

                risque = "⚠️  Risque (exécutable par tous)" if executable_par_tous else "ℹ️  À surveiller"
                print(f"{risque} : {chemin_fichier}  |  {permissions}")
                signales += 1
            except OSError as err:
                print(f"❌ Analyse impossible de {chemin_fichier} : {err}")

    print(f"\n📊 Terminé — {signales} fichier(s) signalé(s).")
    return signales


def construire_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Audit de fichiers exécutables sensibles (éducatif).")
    parser.add_argument("-c", "--chemin", default=".",
                        help="Dossier à auditer (défaut : dossier courant)")
    parser.add_argument("--ext", nargs="+", default=EXTENSIONS_SENSIBLES_DEFAUT,
                        help="Extensions à surveiller (défaut : .sh .py .exe .bat .ps1 .cmd)")
    return parser


def main() -> None:
    args = construire_parser().parse_args()
    if not os.path.isdir(args.chemin):
        raise SystemExit(f"❌ Dossier introuvable : {args.chemin}")
    auditer(args.chemin, args.ext)


if __name__ == "__main__":
    main()
