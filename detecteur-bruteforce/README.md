# 🔐 Détecteur local de brute-force

Script Python qui analyse un fichier de logs et repère les adresses IP effectuant trop de tentatives de connexion échouées — comportement typique d'une **attaque par force brute**.

> Projet éducatif — **Suite Cybersécurité**. Orientation **défense / détection**.

---

## 🧠 Objectif

- Lire un fichier de logs de connexions (réussies / échouées)
- Compter les tentatives **échouées** par adresse IP
- Signaler toute IP qui dépasse un **seuil configurable**

---

## 📁 Format de log attendu

Une ligne par évènement, par exemple :

```
[2025-08-05 09:00:01] IP: 192.168.1.10 - Tentative échouée - utilisateur: admin
[2025-08-05 09:01:00] IP: 10.0.0.2 - Connexion réussie - utilisateur: guest
```

Le script repère les lignes contenant « Tentative échouée » et en extrait l'IP.

---

## 🚀 Exécution

### Prérequis
- Python 3.8+ (aucune dépendance externe)

### Exemples

```bash
# Utilise le fichier logs.txt fourni avec le projet
python detecteur.py

# Fichier et seuil personnalisés
python detecteur.py -f logs.txt -s 5

# Mode détaillé (affiche chaque échec)
python detecteur.py -f logs.txt -s 10 --verbose
```

### Options

| Option | Description | Défaut |
|---|---|---|
| `-f`, `--fichier` | Chemin du fichier de logs | `logs.txt` du projet |
| `-s`, `--seuil` | Seuil d'alerte (nb de tentatives) | `5` |
| `-v`, `--verbose` | Affiche chaque échec détecté | désactivé |

---

## 🧪 Exemple de sortie

```
📄 Analyse de : logs.txt

🚨 IP suspectes (≥ 5 tentatives échouées) :
   - 192.168.1.10 : 6 tentatives
```

---

## 📌 Note

Une première version plus simple existe dans le dossier `Projet2Détecteurdebruteforcelocal` (comptage global sans distinction d'IP). Cette version-ci la remplace.
