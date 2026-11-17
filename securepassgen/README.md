# 🔐 SecurePassGen

Générateur de mots de passe **sécurisé** avec évaluation de la force, disponible en **console** et en **interface web**.

> Projet éducatif — **Suite Cybersécurité**.

---

## ✨ Points forts

- Génération **cryptographiquement sûre** via le module `secrets` (et non `random`)
- Garantit **au moins un caractère de chaque type** sélectionné
- Calcul de l'**entropie** (en bits) et évaluation de la **force**
- Deux interfaces : **ligne de commande** et **web (Flask)**
- Entrées fiabilisées (aucun crash sur saisie invalide)

---

## 📂 Structure

| Fichier | Rôle |
|---|---|
| `generator.py` | Moteur de génération (module `secrets`) |
| `strength_checker.py` | Calcul d'entropie et niveau de force |
| `main.py` | Interface **console** |
| `app.py` | Interface **web** (Flask) |
| `templates/index.html` | Page web |

---

## 🚀 Utilisation

### Prérequis
- Python 3.8+

### Console (sans dépendance)

```bash
python main.py
```

### Web

```bash
pip install -r requirements.txt
python app.py
```

Puis ouvrir **http://127.0.0.1:5000**

> L'app écoute sur `127.0.0.1` (local uniquement) et `debug=False` — valeurs sûres par défaut.

---

## 🧪 Exemple (console)

```
🧾 Mot de passe généré : g7#Kq2!vXm9pL@
🔐 Entropie : 85.27 bits
📊 Force : 🟩 Très forte
```

---

## 📊 Échelle de force

| Entropie | Niveau |
|---|---|
| < 40 bits | 🟥 Faible |
| 40–60 bits | 🟧 Moyenne |
| 60–80 bits | 🟨 Forte |
| ≥ 80 bits | 🟩 Très forte |
