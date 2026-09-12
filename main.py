import os
from pathlib import Path

# Active les couleurs ANSI dans le terminal Windows
os.system("")

ROUGE = "\033[31m"
RESET = "\033[0m"


# --------------------------------------------------
# VALEUR DES LETTRES AU SCRABBLE
# --------------------------------------------------

valeurs_lettres = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1,
    "F": 4, "G": 2, "H": 4, "I": 1, "J": 8,
    "K": 10, "L": 1, "M": 2, "N": 1, "O": 1,
    "P": 3, "Q": 8, "R": 1, "S": 1, "T": 1,
    "U": 1, "V": 4, "W": 10, "X": 10, "Y": 10,
    "Z": 10
}


# --------------------------------------------------
# CHARGEMENT DU DICTIONNAIRE
# --------------------------------------------------

def charger_dictionnaire(chemin):
    mots = []

    with open(chemin, "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            mot = ligne.strip().upper()

            if 2 <= len(mot):
                mots.append(mot)

    return mots


# --------------------------------------------------
# CALCUL DU SCORE + DÉTECTION DES JOKERS
# --------------------------------------------------

def calculer_score_et_jokers(mot, lettres):
    score = 0
    lettres_restantes = list(lettres)
    positions_joker = []

    for i, lettre in enumerate(mot):

        # La vraie lettre est disponible
        if lettre in lettres_restantes:
            lettres_restantes.remove(lettre)
            score += valeurs_lettres[lettre]

        # Sinon on utilise un joker
        elif "?" in lettres_restantes:
            lettres_restantes.remove("?")
            positions_joker.append(i)

        # Impossible de fabriquer le mot
        else:
            return None, None

    return score, positions_joker


# --------------------------------------------------
# RECHERCHE DES MOTS POSSIBLES
# --------------------------------------------------

def trouver_mots_possibles(lettres, dictionnaire):
    mots_possibles = []

    for mot in dictionnaire:
        score, positions_joker = calculer_score_et_jokers(mot, lettres)

        if score is not None:
            mots_possibles.append((mot, score, positions_joker))

    # Score décroissant
    # Puis longueur décroissante
    # Puis ordre alphabétique
    mots_possibles.sort(
        key=lambda x: (-len(x[0]), -x[1], x[0])
    )
    return mots_possibles


# --------------------------------------------------
# COLORATION DES LETTRES UTILISÉES PAR UN JOKER
# --------------------------------------------------

def colorer_mot_joker(mot, positions_joker):
    resultat = ""

    for i, lettre in enumerate(mot):

        if i in positions_joker:
            resultat += ROUGE + lettre + RESET
        else:
            resultat += lettre

    return resultat


# --------------------------------------------------
# AFFICHAGE DES RÉSULTATS
# --------------------------------------------------

def afficher_resultats(resultats, taille_page=1000):

    if len(resultats) == 0:
        print("\nAucun mot trouvé.")
        return

    print(f"\n{len(resultats)} mots trouvés.\n")

    for i, (mot, score, positions_joker) in enumerate(resultats, start=1):

        mot_colore = colorer_mot_joker(mot, positions_joker)

        print(f"{i}. {mot_colore} : {score} points")

        # Toutes les 30 lignes
        if i % taille_page == 0 and i < len(resultats):

            choix = input(
                "\nEntrée = afficher la suite | Q = quitter : "
            )

            if choix.upper() == "Q":
                break

            print()


# --------------------------------------------------
# PROGRAMME PRINCIPAL
# --------------------------------------------------

def main():

    # Cherche automatiquement ods9.txt dans le même dossier que main.py
    dossier = Path(__file__).parent
    chemin_dictionnaire = dossier / "ods9.txt"

    dictionnaire = charger_dictionnaire(chemin_dictionnaire)

    print("================================")
    print("           ANAGRAMMEUR           ")
    print("================================")

    print(f"\n{len(dictionnaire)} mots chargés.")

    while True:

        lettres = input(
            "\nEntre tes lettres (? pour un joker, Q pour quitter) : "
        ).strip().upper()

        if lettres == "Q":
            print("\nAu revoir !")
            break

        if len(lettres) < 2:
            print("Entre au moins 2 lettres.")
            continue

        # Vérifie qu'il n'y a que des lettres ou ?
        if not all(lettre.isalpha() or lettre == "?" for lettre in lettres):
            print("Utilise uniquement des lettres et des ? pour les jokers.")
            continue

        resultats = trouver_mots_possibles(
            lettres,
            dictionnaire
        )

        afficher_resultats(resultats)


# --------------------------------------------------

if __name__ == "__main__":
    main()