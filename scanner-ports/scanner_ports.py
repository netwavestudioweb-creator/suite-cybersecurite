#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scanner de ports TCP — Suite Cybersécurité (projet éducatif)
============================================================

Scanne une plage de ports TCP sur une machine et liste les ports ouverts,
avec le nom du service courant associé.

⚠️  USAGE ÉTHIQUE & LÉGAL
    N'utilisez cet outil QUE sur des machines / réseaux qui vous appartiennent
    ou pour lesquels vous disposez d'une autorisation écrite explicite.
    Scanner un système tiers sans autorisation est illégal dans la plupart
    des pays. Ce projet a un but strictement pédagogique (défense / audit).

Exemples :
    python scanner_ports.py 127.0.0.1
    python scanner_ports.py exemple.com -d 1 -f 1024 -w 200
    python scanner_ports.py            (mode interactif)
"""
from __future__ import annotations

import argparse
import socket
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Sous Windows, la console est souvent en cp1252 et ne sait pas afficher les
# emojis → on force la sortie en UTF-8 pour éviter UnicodeEncodeError.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Services les plus courants, pour rendre le rapport lisible
SERVICES_COURANTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 445: "SMB",
    993: "IMAPS", 995: "POP3S", 3306: "MySQL", 3389: "RDP",
    5432: "PostgreSQL", 6379: "Redis", 8080: "HTTP-alt", 8443: "HTTPS-alt",
}


def resoudre_cible(cible: str) -> str:
    """Convertit un nom de domaine en adresse IP. Lève SystemExit si échec."""
    try:
        return socket.gethostbyname(cible)
    except socket.gaierror:
        raise SystemExit(f"❌ Impossible de résoudre la cible : {cible!r}")


def scanner_port(ip: str, port: int, timeout: float) -> int | None:
    """Teste un port. Renvoie le numéro de port s'il est ouvert, sinon None."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        if sock.connect_ex((ip, port)) == 0:
            return port
    return None


def scanner(cible: str, port_min: int, port_max: int,
            timeout: float, threads: int) -> list[int]:
    """Scanne une plage de ports en parallèle et affiche un rapport."""
    ip = resoudre_cible(cible)
    print(f"\n📡 Scan de {cible} ({ip}) — ports {port_min} à {port_max}")
    print(f"   timeout={timeout}s  threads={threads}\n")

    ouverts: list[int] = []
    debut = time.time()

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {
            executor.submit(scanner_port, ip, port, timeout): port
            for port in range(port_min, port_max + 1)
        }
        for future in as_completed(futures):
            port = future.result()
            if port is not None:
                service = SERVICES_COURANTS.get(port, "inconnu")
                print(f"✅ Port {port:<5} OUVERT   ({service})")
                ouverts.append(port)

    duree = round(time.time() - debut, 2)
    print(f"\n⏱️  Scan terminé en {duree}s — {len(ouverts)} port(s) ouvert(s).")
    return sorted(ouverts)


def construire_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Scanner de ports TCP (projet éducatif - usage autorisé uniquement).")
    parser.add_argument("cible", nargs="?", help="IP ou nom de domaine à scanner")
    parser.add_argument("-d", "--debut", type=int, default=1,
                        help="Port de début (défaut : 1)")
    parser.add_argument("-f", "--fin", type=int, default=1024,
                        help="Port de fin (défaut : 1024)")
    parser.add_argument("-t", "--timeout", type=float, default=0.5,
                        help="Timeout par port en secondes (défaut : 0.5)")
    parser.add_argument("-w", "--workers", type=int, default=100,
                        help="Nombre de threads (défaut : 100)")
    return parser


def main() -> None:
    args = construire_parser().parse_args()

    cible = args.cible or input("🔍 Adresse IP ou domaine à scanner : ").strip()
    if not cible:
        raise SystemExit("❌ Aucune cible fournie.")
    if not (1 <= args.debut <= args.fin <= 65535):
        raise SystemExit("❌ Plage de ports invalide (attendu : 1 ≤ début ≤ fin ≤ 65535).")

    try:
        scanner(cible, args.debut, args.fin, args.timeout, args.workers)
    except KeyboardInterrupt:
        print("\n⏹️  Scan interrompu par l'utilisateur.")


if __name__ == "__main__":
    main()
