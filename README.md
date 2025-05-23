# Consigne pour la Leçon 1: Types de données et structure de base

**Objectif:** Créer la structure de base de l'analyseur de texte en mettant l'accent sur les types de données natifs de Python.

**Tâches à réaliser:**
* Créer une classe TextAnalyzer pour analyser un texte donné
* Implémenter la validation de type dans le constructeur avec `isinstance()`
* Implémenter les méthodes d'analyse de base
* Gérer les cas particuliers (texte vide, absence de mots)
* Stocker les résultats dans des structures de données appropriées
* Afficher les statistiques avec indication des types de données

**Fonctionnalités attendues:**
* `__init__(text)` - validation du type avec `isinstance()` et exception `TypeError`
* `analyser_caracteres()` - compte nombre de caractères, lettres, chiffres, espaces, détecte texte vide
* `analyser_mots()` - analyse nombre de mots, mots uniques, mot le plus long, longueur moyenne
* `afficher_stats()` - affiche toutes les statistiques avec leurs types Python

**Concepts à appliquer:**
* Types natifs Python: `str`, `int`, `float`, `bool`, `dict`, `list`, `set`
* Validation de types avec `isinstance()` et gestion d'exceptions
* Manipulation de chaînes de caractères basique (`split()`, méthodes de caractères)
* Structures de données pour stocker les résultats (`dict()`, stockage organisé)
* Compréhensions et expressions génératrices (`set()`, `sum()`, `max()`)