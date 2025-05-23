
"""
TextAnalyzer - Analyseur de texte
Leçon 1: Types de données et structure de base
"""


class TextAnalyzer:
    def __init__(self, text):
        
        if not isinstance(text, str):
            raise TypeError("Le texte doit être une chaîne de caractères")
        
        self.text = text
        self.stats = dict()
    
    def analyser_caracteres(self):
        if not self.text:
            return dict()
        
        stats = {
            "nombre_caracteres": len(self.text), # int
            "lettres": 0, # int
            "chiffres": 0, # int
            "espaces": 0, # int
            "text_vide": not self.text # bool
        }
        
        for char in self.text:
            if char.isalpha():
                stats["lettres"] += 1
            elif char.isdigit():
                stats["chiffres"] += 1
            elif char.isspace():
                stats["espaces"] += 1

        self.stats["caracteres"] = stats
        
        return stats
    
    def analyser_mots(self):
        if not self.text:
            return dict()
        
        mots = self.text.split() # list
        
        if mots:
            stats = {
                "nombre_mots": len(mots), # int
                "mots_uniques": len(set(mot.lower() for mot in mots)), # int
                "mot_le_plus_long": max(mots, key=len), # str
                "longueur_moyenne": sum(len(mot) for mot in mots) / len(mots), # float
            }

            self.stats["mots"] = stats
            return stats
        
        else:
            return dict()
    
    def afficher_stats(self):
        print(f"Texte analysé : {self.text}")
        print("Statistiques caractères :")
        for key, value in self.stats.get("caracteres", {}).items():
            print(f"{key}: {value} ({type(value).__name__})")

        print("Statistiques mots :")
        for key, value in self.stats.get("mots", {}).items():
            print(f"{key}: {value} ({type(value).__name__})")


# Test de la classe TextAnalyzer
if __name__ == "__main__":
    texte = "Bonjour, le monde 123 !"
    analyseur = TextAnalyzer(texte)
    
    analyseur.analyser_caracteres()
    analyseur.analyser_mots()

    analyseur.afficher_stats()
