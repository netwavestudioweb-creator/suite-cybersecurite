# 🔍 Scanner de ports TCP

Outil en ligne de commande pour scanner les ports TCP ouverts sur une machine, écrit en Python (bibliothèque standard uniquement).

> Projet éducatif — **Suite Cybersécurité**.

---

## ⚠️ Usage éthique & légal

N'utilisez cet outil **que** sur des machines ou réseaux qui vous appartiennent, ou pour lesquels vous disposez d'une **autorisation écrite**. Scanner un système tiers sans autorisation est **illégal**. Ce projet sert à l'apprentissage de l'audit et de la défense.

---

## 🎯 Objectif

- Scanner une plage de ports (par défaut 1 → 1024) sur une IP ou un domaine
- Identifier les ports **ouverts** et le **service courant** associé
- Produire un rapport clair et chronométré

---

## ✨ Fonctionnalités

- Scan **multi-thread** (rapide)
- Résolution automatique des noms de domaine
- Détection des services courants (HTTP, SSH, MySQL…)
- Interface **ligne de commande** (`argparse`) **ou** mode interactif
- Gestion des erreurs (cible introuvable, plage invalide, interruption clavier)

---

## 🚀 Installation & exécution

### Prérequis
- Python 3.8+ (aucune dépendance externe)

### Exemples

```bash
# Scan local
python scanner_ports.py 127.0.0.1

# Scan d'une plage précise avec 200 threads
python scanner_ports.py exemple.com -d 1 -f 1024 -w 200

# Mode interactif (demande la cible)
python scanner_ports.py
```

### Options

| Option | Description | Défaut |
|---|---|---|
| `cible` | IP ou domaine à scanner | (demandé) |
| `-d`, `--debut` | Port de début | `1` |
| `-f`, `--fin` | Port de fin | `1024` |
| `-t`, `--timeout` | Timeout par port (s) | `0.5` |
| `-w`, `--workers` | Nombre de threads | `100` |

---

## 🧪 Exemple de sortie

```
📡 Scan de 127.0.0.1 (127.0.0.1) — ports 1 à 1024
   timeout=0.5s  threads=100

✅ Port 135   OUVERT   (inconnu)
✅ Port 445   OUVERT   (SMB)

⏱️  Scan terminé en 0.42s — 2 port(s) ouvert(s).
```
