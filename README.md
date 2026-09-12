# Anagrammeur Python

Un petit programme en **Python** permettant de trouver des mots à partir d’un ensemble de lettres, dans l’esprit d’un anagrammeur pour le **Scrabble**.

Le programme prend en compte les lettres disponibles, les jokers `?`, calcule les points des mots trouvés et trie les résultats pour afficher en priorité les mots les plus intéressants.

## Fonctionnalités

* Recherche de mots à partir des lettres saisies
* Gestion des jokers avec le caractère `?`
* Mise en évidence en rouge de la lettre remplacée par un joker
* Calcul du score Scrabble de chaque mot
* Tri des résultats :

  1. par longueur du mot
  2. puis par nombre de points en cas d’égalité
* Affichage des résultats directement dans le terminal

## Exemple

Pour les lettres :

```text
CHIE?
```

Le programme peut par exemple proposer :

```text
CHIEN
CHIER
NICHE
```

Lorsqu’un joker est utilisé, la lettre correspondant au joker est affichée en rouge dans le terminal.

## Installation

Le projet nécessite **Python 3**.

Clonez le dépôt :

```bash
git clone https://github.com/matteo-974/anagrammeur_python.git
```

Puis placez-vous dans le dossier :

```bash
cd anagrammeur_python
```

Le programme utilise également la bibliothèque `colorama` pour afficher les lettres utilisées par les jokers en couleur.

Installation :

```bash
pip install colorama
```

Si plusieurs versions de Python sont installées :

```bash
python -m pip install colorama
```

## Utilisation

Lancez simplement :

```bash
python main.py
```

Puis entrez les lettres que vous souhaitez utiliser.

Exemple :

```text
Entrez vos lettres : CHIE?
```

Le caractère `?` représente un joker et peut remplacer n’importe quelle lettre.

## Classement des résultats

Les mots trouvés sont triés selon les règles suivantes :

* les mots les plus longs sont affichés en premier ;
* lorsque deux mots ont la même longueur, celui qui rapporte le plus de points est affiché en premier.

Par exemple :

```text
LONGMOT     14 points
AUTREMOT    11 points
PETIT       10 points
AUTRE        7 points
```

## Technologies utilisées

* Python
* Colorama
* Git / GitHub

## Objectif du projet

Ce projet a été réalisé afin de créer un outil simple permettant de rechercher rapidement les mots réalisables à partir de lettres données, notamment pour des jeux de lettres comme le Scrabble.

Le projet pourra être amélioré progressivement avec de nouvelles fonctionnalités.

## Auteur

**Matteo**

GitHub : [matteo-974](https://github.com/matteo-974)
