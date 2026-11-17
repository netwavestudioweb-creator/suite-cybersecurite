# 🛡️ Suite Cybersécurité

Collection d'outils Python à visée **défensive et pédagogique** : audit, détection d'intrusion, génération de secrets, cryptographie d'apprentissage.

> Par **Adriano DODO**.

---

## ⚠️ Usage éthique

Ces outils servent à **apprendre la sécurité** et à protéger des systèmes **qui vous appartiennent** ou pour lesquels vous avez une **autorisation écrite**. Toute utilisation contre un tiers sans autorisation est illégale.

---

## 📦 Outils

| Outil | Description | Type |
|---|---|---|
| [`scanner-ports`](scanner-ports) | Scanner de ports TCP multi-thread, avec détection des services | Audit réseau |
| [`detecteur-bruteforce`](detecteur-bruteforce) | Détection d'IP suspectes dans des logs (seuil configurable) | Détection |
| [`securepassgen`](securepassgen) | Générateur de mots de passe sûr (console **+ web**), avec mesure d'entropie | Secrets |
| [`crypto-tool`](crypto-tool) | Chiffrement de fichiers (XOR — éducatif, non sécurisé par design) | Crypto |
| [`audit-securite`](audit-securite) | Audit des fichiers exécutables sensibles d'un dossier | Audit |

Chaque outil a son propre `README.md`, son `requirements.txt` et une bannière d'usage éthique.

---

## ✨ Standard commun

- Code structuré en fonctions, avec **gestion d'erreurs**
- Interface **ligne de commande** (`argparse`) — `securepassgen` a en plus une interface **web (Flask)**
- Compatibilité **Windows** (sortie console UTF-8)
- Génération de secrets **cryptographiquement sûre** (`secrets`, et non `random`)

---

## 🚀 Démarrage

Python 3.8+. Chaque outil se lance depuis son dossier, par ex. :

```bash
cd scanner-ports
python scanner_ports.py 127.0.0.1
```
