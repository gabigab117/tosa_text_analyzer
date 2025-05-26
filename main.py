"""
TextAnalyzer - Analyseur de texte
Leçon 3: Opérateurs et expressions
"""

import re


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
    
    def analyser_lignes(self):
        if not self.text:
            return dict()
        
        lignes = self.text.splitlines()
        if lignes:
            stats = {
                "nombre_lignes": len(lignes), # int
                "lignes_vides": sum(1 for ligne in lignes if not ligne.strip()), # int
                "lignes_avec_texte": sum(1 for ligne in lignes if ligne.strip()), # int
                "ligne_la_plus_longue": max(lignes, key=len), # str
                "mots_par_ligne": [len(ligne.split()) for ligne in lignes], # list
            }
            self.stats["lignes"] = stats
            return stats
        else:
            return dict()
    
    def detecter_patterns(self):
        if not self.text:
            return dict()
        
        mots = self.text.split()
        
        stats = {
            "commence_par_voyelle": sum(1 for mot in mots if mot[0].lower() in "aeiouy"), # int
            "fini_par_un_point": sum(1 for mot in mots if mot.endswith(".")), # int
            "commence_par_majuscule": sum(1 for mot in mots if mot[0].isupper()), # int
        }
        
        self.stats["patterns"] = stats
        return stats
    
    def extraire_mots_input(self):
        if not self.text:
            return ""
        
        mots = self.text.split()
        print("""
              Voulez-vous filtrer les mots ?
              1. Par longueur (Supérieur ou égal à)
              2. Par première lettre
              3. Par majuscule
              """)
        choix = input("Entrez votre choix (1, 2 ou 3) : ")
        if choix == "1":
            try:
                longueur = int(input("Entrez la longueur minimale : "))
                mots_filtres = [mot for mot in mots if len(mot) >= longueur]
            except ValueError:
                print("Veuillez entrer un nombre valide.")
                return ""
        elif choix == "2":
            lettre = input("Entrez la première lettre : ")
            mots_filtres = [mot for mot in mots if mot.startswith(lettre)]
        elif choix == "3":
            mots_filtres = [mot for mot in mots if mot[0].isupper()]
        else:
            print("Choix invalide.")
            return ""
        return " | ".join(mots_filtres)
    
    def detecter_avec_regex(self):
        if not self.text:
            return dict()
        
        patterns = {
            "emails": re.findall(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b", self.text), # list
            "nombres": re.findall(r"\b\d+\b", self.text), # list
        }
        
        self.stats["regex"] = patterns
        return patterns
    
    def verifier_conditions_texte(self):
        if not self.text:
            return dict()
        
        mots = self.text.split()
        
        conditions = {
            "contient_chiffres": any(char.isdigit() for char in self.text), # bool
            "contient_lettres": any(char.isalpha() for char in self.text), # bool
            "contient_espaces": any(char.isspace() for char in self.text), # bool
            "tous_mots_courts": all(len(mot) <= 3 for mot in mots), # bool
            "au_moins_un_mot_long": any(len(mot) > 3 for mot in mots), # bool
            "tous_alphabetiques": all(char.isalpha() for char in self.text), # bool
        }
        self.stats["conditions"] = conditions
        return conditions
    
    def analyser_taille_mots(self):
        if not self.text:
            return dict()
        
        mots = self.text.split()
        longueur_moyenne = sum(len(mot) for mot in mots) / len(mots) if mots else 0
        analyse = {
            "longueur_moyenne": longueur_moyenne,
            "mots_courts": sum(1 for mot in mots if len(mot) < longueur_moyenne), # int
            "mots_longs": sum(1 for mot in mots if len(mot) > longueur_moyenne), # int
            "mots_egaux": sum(1 for mot in mots if len(mot) == longueur_moyenne), # int
        }
        
        self.stats["taille_mots"] = analyse
        return analyse

    def afficher_stats(self):
        print(f"Texte analysé : {self.text}")
        for category, stats in self.stats.items():
            print(f"\nStatistiques pour {category} :")
            for key, value in stats.items():
                print(f"{key}: {value}")
    
    def generer_rapport(self):
        if not self.stats:
            return "Aucun rapport généré, veuillez d'abord analyser un texte."
        
        template = "{titre}: {valeur}"
        
        rapport = list()
        rapport.append("=" * 20)
        rapport.append("Rapport d'analyse")
        rapport.append("=" * 20)
        
        rapport.append(f"Texte : {self.text[:25]}{'...' if len(self.text) > 25 else ''}")
        rapport.append(f"Nombre de caractères : {self.stats['caracteres']['nombre_caracteres']:,} caractères")
        
        if "mots" in self.stats:
            mots = self.stats["mots"]
            rapport.append(template.format(titre="Nombre de mots", valeur=mots['nombre_mots']))
            rapport.append(f" . Longueur moyenne : {mots['longueur_moyenne']:.2f}")
        
        if "caracteres" in self.stats:
            caracteres = self.stats["caracteres"]
            rapport.append(template.format(titre="Nombre de lettres", valeur=caracteres['lettres']))
            pourcentage_lettres = caracteres['lettres'] / self.stats['caracteres']['nombre_caracteres'] * 100
            rapport.append(f" . Pourcentage de lettres : {pourcentage_lettres:.1f}%")
        
        if "regex" in self.stats:
            regex = self.stats["regex"]
            rapport.append(f"Emails trouvés : {len(regex['emails'])}")
        
        return "\n".join(rapport)


# Test de la classe TextAnalyzer
if __name__ == "__main__":
    texte = "Bonjour, le monde 123 ! Et je suis content. Ah que oui.\n Mes adresses email sont : test@test.com et ggfghfgh.rt@rien.com"
    analyseur = TextAnalyzer(texte)
    
    analyseur.analyser_caracteres()
    analyseur.analyser_mots()
    analyseur.analyser_lignes()
    analyseur.detecter_patterns()
    analyseur.detecter_avec_regex()
    
    # Analyser taille des mots
    print("Analyse de la taille des mots :")
    a = analyseur.analyser_taille_mots()
    print(a)
    b = analyseur.verifier_conditions_texte()
    print(b)
    analyseur.afficher_stats()
    # Générer et afficher le rapport
    print("\nGénération du rapport :")
    r = analyseur.generer_rapport()
    print(r)