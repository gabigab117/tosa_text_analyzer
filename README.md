# Consigne pour la Leçon 2: Manipulation avancée des chaînes

**Objectif:** Enrichir l'analyseur de texte avec des techniques avancées de manipulation de chaînes et de formatage.

**Tâches à réaliser:**
* Ajouter l'analyse des lignes avec `splitlines()` et `strip()`
* Implémenter la détection de patterns avec `startswith()` et `endswith()`
* Créer une extraction interactive de mots avec `input()` et validation
* Ajouter la détection de patterns avec expressions régulières
* Implémenter un rapport formaté utilisant `.format()` et f-strings

**Fonctionnalités attendues:**
* `analyser_lignes()` - analyse nombre de lignes, lignes vides, ligne la plus longue
* `detecter_patterns()` - détecte mots commençant par voyelles/majuscules, finissant par point
* `extraire_mots_input()` - filtrage interactif par longueur, première lettre ou majuscule
* `detecter_avec_regex()` - extraction d'emails et nombres avec expressions régulières
* `generer_rapport()` - rapport formaté avec template `.format()` et f-strings

**Concepts à appliquer:**
* Méthodes de chaînes avancées: `splitlines()`, `strip()`, `startswith()`, `endswith()`
* Formatage mixte avec `.format()` et f-strings (séparateurs, décimales)
* Utilisation du module `re` pour les expressions régulières
* Interaction utilisateur avec `input()` et gestion d'erreurs
* Assemblage de texte avec `join()` et séparateurs personnalisés