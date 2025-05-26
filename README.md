# Cahier des charges pour le projet TextAnalyzer (Module 1)

## Description générale
TextAnalyzer est un analyseur de texte modulaire permettant d'extraire des statistiques et d'analyser le contenu textuel. Le projet final intègre les concepts fondamentaux de Python abordés à travers les trois leçons du module "Syntaxe et types de données avancés".

## Fonctionnalités implémentées
- Analyse des types de caractères (lettres, chiffres, espaces)
- Statistiques sur les mots (nombre, unicité, longueurs)
- Analyse des lignes et détection de contenu vide
- Extraction interactive de mots selon différents critères
- Détection de patterns avec expressions régulières (emails, nombres)
- Vérifications conditionnelles avec expressions booléennes
- Génération de rapports formatés avec templates

## Structure de données
Chaque analyse stocke ses résultats dans `self.stats` :
- Types de caractères et comptages
- Statistiques des mots et longueurs moyennes
- Informations sur les lignes et leur contenu
- Patterns détectés et conditions vérifiées
- Classifications basées sur des critères de comparaison

## Plan d'implémentation par leçon

### Consigne pour la Leçon 1: Types de données et structure de base
**Objectif:** Créer la structure de base de l'analyseur de texte en mettant l'accent sur les types de données natifs de Python.

**Tâches à réaliser:**
- Créer une classe TextAnalyzer pour analyser un texte donné
- Implémenter la validation de type dans le constructeur avec `isinstance()`
- Implémenter les méthodes d'analyse de base
- Gérer les cas particuliers (texte vide, absence de mots)
- Stocker les résultats dans des structures de données appropriées
- Afficher les statistiques avec indication des types de données

**Fonctionnalités attendues:**
- `__init__(text)` - validation du type avec `isinstance()` et exception `TypeError`
- `analyser_caracteres()` - compte lettres, chiffres, espaces, détecte texte vide
- `analyser_mots()` - analyse nombre de mots, mots uniques, mot le plus long, longueur moyenne
- `afficher_stats()` - affiche toutes les statistiques avec leurs types Python

**Concepts à appliquer:**
- Types natifs Python: `str`, `int`, `float`, `bool`, `dict`, `list`, `set`
- Validation de types avec `isinstance()` et gestion d'exceptions
- Manipulation de chaînes de caractères basique (`split()`, méthodes de caractères)
- Structures de données pour stocker les résultats (`dict()`, stockage organisé)
- Compréhensions et expressions génératrices (`set()`, `sum()`, `max()`)

### Consigne pour la Leçon 2: Manipulation avancée des chaînes
**Objectif:** Enrichir l'analyseur de texte avec des techniques avancées de manipulation de chaînes et de formatage.

**Tâches à réaliser:**
- Ajouter l'analyse des lignes avec `splitlines()` et `strip()`
- Implémenter la détection de patterns avec `startswith()` et `endswith()`
- Créer une extraction interactive de mots avec `input()` et validation
- Ajouter la détection de patterns avec expressions régulières
- Implémenter un rapport formaté utilisant `.format()` et f-strings
- Gérer l'affichage des statistiques de manière structurée

**Fonctionnalités attendues:**
- `analyser_lignes()` - analyse nombre de lignes, lignes vides, ligne la plus longue
- `detecter_patterns()` - détecte mots commençant par voyelles/majuscules, finissant par point
- `extraire_mots_input()` - filtrage interactif par longueur, première lettre ou majuscule
- `detecter_avec_regex()` - extraction d'emails et nombres avec expressions régulières
- `generer_rapport()` - rapport formaté avec template `.format()` et f-strings stylés

**Concepts à appliquer:**
- Méthodes de chaînes avancées: `splitlines()`, `strip()`, `startswith()`, `endswith()`
- Formatage mixte avec `.format()` et f-strings (séparateurs, décimales)
- Utilisation du module `re` pour les expressions régulières
- Interaction utilisateur avec `input()` et gestion d'erreurs
- Assemblage de texte avec `join()` et séparateurs personnalisés

### Consigne pour la Leçon 3: Opérateurs et expressions
**Objectif:** Enrichir l'analyseur de texte avec des analyses conditionnelles utilisant les opérateurs et expressions booléennes.

**Tâches à réaliser:**
- Implémenter des vérifications avec `all()` et `any()`
- Ajouter des analyses utilisant les opérateurs de comparaison
- Appliquer les expressions booléennes pour analyser le contenu
- Utiliser les opérateurs logiques dans des conditions pratiques

**Fonctionnalités attendues:**
- `verifier_conditions_texte()` - utilise `any()` et `all()` pour vérifier la présence de chiffres, lettres, espaces et analyser les mots
- `analyser_taille_mots()` - compare les longueurs avec opérateurs `<`, `>`, `==` par rapport à la moyenne

**Concepts à appliquer:**
- Expressions booléennes avec `any()` et `all()` pour vérifications globales
- Opérateurs de comparaison (`<`, `>`, `==`) pour classification et analyse
- Expressions conditionnelles
- Calculs statistiques avec opérateurs arithmétiques et comparaisons