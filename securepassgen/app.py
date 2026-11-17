# -*- coding: utf-8 -*-
"""
SecurePassGen — interface web (Flask)
=====================================
Suite Cybersécurité — projet éducatif.

Lancement :
    pip install -r requirements.txt
    python app.py
    → http://127.0.0.1:5000
"""
from flask import Flask, render_template, request

from generator import generer_mot_de_passe
from strength_checker import entropie, evaluer_force

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    mot_de_passe = ""
    force = ""
    entropy = 0
    erreur = ""

    if request.method == "POST":
        try:
            longueur = max(int(request.form.get("longueur", 12)), 8)
        except (TypeError, ValueError):
            longueur = 12

        maj = "maj" in request.form
        minusc = "minusc" in request.form
        chiffres = "chiffres" in request.form
        symboles = "symboles" in request.form

        try:
            mot_de_passe = generer_mot_de_passe(longueur, maj, minusc, chiffres, symboles)
            entropy = entropie(mot_de_passe)
            force = evaluer_force(entropy)
        except ValueError as err:
            erreur = str(err)

    return render_template("index.html", password=mot_de_passe,
                           force=force, entropy=entropy, erreur=erreur)


if __name__ == "__main__":
    # 127.0.0.1 (et non 0.0.0.0) + debug désactivé : valeurs sûres par défaut.
    app.run(host="127.0.0.1", port=5000, debug=False)
