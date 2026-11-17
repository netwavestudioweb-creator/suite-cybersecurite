# -*- coding: utf-8 -*-
"""
Moteur de (dé)chiffrement — CryptoTool (projet éducatif).

⚠️  AVERTISSEMENT IMPORTANT
    Le chiffrement XOR implémenté ici N'EST PAS sûr sur le plan
    cryptographique. Il sert uniquement à COMPRENDRE le principe du
    chiffrement symétrique. Ne l'utilisez JAMAIS pour protéger de vraies
    données sensibles — utilisez une bibliothèque éprouvée (ex. `cryptography`,
    AES-GCM) pour cela.
"""
import base64


def xor_crypt(data: str, key: str) -> str:
    """Applique un XOR répété entre les données et la clé."""
    if not key:
        raise ValueError("La clé ne peut pas être vide.")
    return "".join(
        chr(ord(data[i]) ^ ord(key[i % len(key)]))
        for i in range(len(data))
    )


def chiffrer_fichier(source: str, destination: str, key: str) -> None:
    # newline="" : on désactive la traduction des fins de ligne pour garantir
    # un aller-retour identique à l'octet près (notamment sous Windows).
    with open(source, "r", encoding="utf-8", newline="") as f:
        contenu = f.read()
    contenu_chiffre = xor_crypt(contenu, key)
    contenu_encode = base64.b64encode(contenu_chiffre.encode("utf-8")).decode("ascii")
    with open(destination, "w", encoding="utf-8", newline="") as f:
        f.write(contenu_encode)


def dechiffrer_fichier(source: str, destination: str, key: str) -> None:
    with open(source, "r", encoding="utf-8", newline="") as f:
        contenu_encode = f.read()
    contenu_chiffre = base64.b64decode(contenu_encode.encode("ascii")).decode("utf-8")
    contenu_clair = xor_crypt(contenu_chiffre, key)
    with open(destination, "w", encoding="utf-8", newline="") as f:
        f.write(contenu_clair)
