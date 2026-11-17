# 🔏 CryptoTool

Outil console pour **chiffrer / déchiffrer** un fichier texte, protégé par un mot de passe maître.

> Projet éducatif — **Suite Cybersécurité**.

---

## ⚠️ Avertissement de sécurité

Cet outil utilise un **chiffrement XOR** (+ encodage base64). **Ce n'est PAS un chiffrement sûr** : il est trivial à casser. Le projet sert uniquement à **comprendre le principe** du chiffrement symétrique.

👉 Pour de vraies données sensibles, utilisez une bibliothèque éprouvée (ex. [`cryptography`](https://cryptography.io/), AES-GCM).

---

## ✨ Fonctionnalités

- Chiffrement / déchiffrement d'un fichier texte
- Verrou par **mot de passe maître** (haché en SHA-256)
- Gestion des erreurs (fichier introuvable, clé vide…)

---

## 📂 Structure

| Fichier | Rôle |
|---|---|
| `main.py` | Menu console |
| `crypto_engine.py` | Chiffrement XOR + base64 |
| `security.py` | Mot de passe maître (SHA-256) |

---

## 🚀 Utilisation

### Prérequis
- Python 3.8+ (aucune dépendance externe)

```bash
python main.py
```

> Au **premier lancement**, le mot de passe saisi devient le mot de passe maître (enregistré dans `.passwd_hash`).

---

## 🧪 Exemple

```
=== CryptoTool (éducatif — XOR non sécurisé) ===
1. Chiffrer un fichier
2. Déchiffrer un fichier
Ton choix (1 ou 2) : 1
🔑 Mot de passe maître : ****
📄 Fichier source : message.txt
💾 Fichier de sortie : message.enc
🗝️  Clé de chiffrement : macle
✅ Fichier chiffré et sauvegardé : message.enc
```
