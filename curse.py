class Mesure:
    def __init__(self, temperature, humidite, pression, ville, pluvieux):
        """
        Initialise une nouvelle mesure météorologique.
        Args:
            temperature (float ou int): Température en degrés Celsius
            humidite (int): Taux d'humidité en pourcentage
            pression (int): Pression atmosphérique en hPa
            ville (str): Nom de la ville où la mesure a été prise
            pluvieux (bool): Indique s'il pleut ou non
        
        Exemple:
            >>> mesure_paris = Mesure(18.5, 65, 1013, "Paris", False)
            >>> mesure_lyon = Mesure(22.3, 78, 1008, "Lyon", True)
        """
        if not isinstance(temperature, (int, float)):
            raise TypeError(f"Température doit être int ou float, reçu {type(temperature).__name__}")
    
        if not isinstance(humidite, int):
            raise TypeError(f"Humidité doit être int, reçu {type(humidite).__name__}")
        
        if not isinstance(ville, str):
            raise TypeError(f"Ville doit être str, reçu {type(ville).__name__}")
    
        if not isinstance(pluvieux, bool):
            raise TypeError(f"Pluvieux doit être bool, reçu {type(pluvieux).__name__}")
        
        self.temperature = temperature    # float ou int
        self.humidite = humidite         # int
        self.pression = pression         # int
        self.ville = ville               # str
        self.pluvieux = pluvieux         # bool
        
    def analyser_humidite(self):
        """Analyse le taux d'humidité (toujours un entier entre 0 et 100)"""
        # L'humidité est stockée comme un int
        humidite_actuelle = self.humidite        # int: 65
        
        # Calculs avec des entiers
        seuil_bas = 30                           # int
        seuil_haut = 80                          # int
        difference_seuil = humidite_actuelle - seuil_bas  # int: 35
        
        # Classification simple
        if humidite_actuelle < seuil_bas:
            niveau = 1                           # int
            description = "Sec"                  # str
            ecart_info = f" Manque {abs(difference_seuil)} pour atteindre le seuil bas de {seuil_bas}."  # str

        elif humidite_actuelle < seuil_haut:
            niveau = 2                           # int
            description = "Normal"               # str
            ecart_info = f" Manque {abs(difference_seuil)} pour atteindre le seuil haut de {seuil_haut}."  # str
        else:
            niveau = 3                           # int
            description = "Humide"               # str
            ecart_info = f" Dépasse de {abs(difference_seuil)} le seuil haut de {seuil_haut}."  # str

        return niveau, description, ecart_info               # tuple(int, str, str)
    
    def analyser_temperature(self):
        """Analyse la température avec précision décimale"""
        # La température est stockée comme un float ou int selon l'entrée
        temp_celsius = self.temperature          # float ou int: 18.5 ou 18
        
        # Calculs avec des flottants
        temp_fahrenheit = temp_celsius * 1.8 + 32.0    # float: 65.3 (conversion auto)
        temp_kelvin = temp_celsius + 273.15            # float: 291.65 (conversion auto)
        
        # Arrondis et précision
        temp_arrondie = round(temp_celsius, 1)         # float: 18.5 ou 18.0
        temp_entiere = round(temp_celsius)             # int: 19 ou 18
        
        # Seuils avec décimales
        seuil_gel = 0.0                         # float
        seuil_canicule = 35.5                   # float
        
        return {
            "celsius": temp_celsius,             # float ou int (type original)
            "fahrenheit": temp_fahrenheit,       # float (conversion auto)
            "kelvin": temp_kelvin,              # float (conversion auto)
            "arrondie": temp_arrondie           # float
        }
    
    def analyser_ville(self):
        """Analyse et valide le nom de la ville"""
        # La ville est stockée comme un str
        nom_ville = self.ville                   # str: "Paris"
        
        # Propriétés basiques des chaînes
        longueur = len(nom_ville)               # int: 5
        premier_char = nom_ville[0]             # str: "P"
        dernier_char = nom_ville[-1]            # str: "s"
        
        # Vérifications de contenu
        contient_espaces = " " in nom_ville     # bool: False
        est_alphabetique = nom_ville.isalpha()  # bool: True
        est_majuscule = nom_ville.isupper()     # bool: False
        
        # Transformations (création de nouvelles chaînes)
        en_majuscule = nom_ville.upper()        # str: "PARIS"
        en_minuscule = nom_ville.lower()        # str: "paris"
        premiere_maj = nom_ville.capitalize()   # str: "Paris"
        
        return {
            "nom": nom_ville,                    # str
            "longueur": longueur,               # int
            "premier_char": premier_char,       # str
            "dernier_char": dernier_char,       # str
            "contient_espaces": contient_espaces, # bool
            "alphabetique": est_alphabetique,   # bool
            "tout_majuscule": est_majuscule,    # bool
            "en_majuscule": en_majuscule,       # str
            "en_minuscule": en_minuscule,       # str
            "premiere_maj": premiere_maj        # str
        }
    
    def analyser_conditions_meteo(self):
        """Analyse les conditions météorologiques avec des booléens"""
        # Le statut pluvieux est stocké comme un bool
        il_pleut = self.pluvieux                # bool: True ou False
        
        # Conditions basées sur les seuils
        temperature_basse = self.temperature < 5.0     # bool
        temperature_haute = self.temperature > 30.0    # bool
        humidite_elevee = self.humidite > 85           # bool
        
        # Combinaisons logiques
        temps_froid_et_humide = temperature_basse and humidite_elevee   # bool
        temps_extreme = temperature_basse or temperature_haute          # bool
        temps_agreable = not il_pleut and not temps_extreme            # bool
        
        # Négations
        temps_sec = not il_pleut                # bool
        temperature_normale = not temps_extreme # bool
        
        return {
            "pluie": il_pleut,                  # bool
            "froid": temperature_basse,         # bool
            "chaud": temperature_haute,         # bool
            "agreable": temps_agreable          # bool
        }
    
    def analyser_mesure_complete(self):
        """Retourne un résumé complet sous forme de tuple"""
        # Récupération des analyses précédentes
        niveau_humidite, desc_humidite, ecart_humidite = self.analyser_humidite()  # tuple
        
        # Création d'un tuple avec des types mixtes
        resume = (
            self.ville,                    # str
            self.temperature,              # float ou int
            niveau_humidite,               # int
            self.pluvieux                  # bool
        )
        
        # Tuple avec résultats de calculs
        coordonnees = (48.8566, 2.3522)   # tuple: (float, float)
        
        # Accès aux éléments (comme une liste)
        ville_tuple = resume[0]            # str
        temp_tuple = resume[1]             # float ou int
        
        # Décomposition (unpacking) du tuple
        ville, temperature, niveau, pluie = resume  # Assignation multiple
        
        return resume                      # tuple

    def stocker_mesures_simples(self):
        """Stockage simple de mesures dans des listes"""
        # Listes de valeurs du même type
        temperatures = []                       # list vide
        temperatures.append(18.5)               # list: [18.5]
        temperatures.append(19.2)               # list: [18.5, 19.2]
        temperatures.append(17.8)               # list: [18.5, 19.2, 17.8]
        
        # Listes de types mixtes
        infos_ville = ["Paris", 2161000, True] # list: [str, int, bool]
        
        # Accès aux éléments
        premiere_temp = temperatures[0]         # float: 18.5
        nombre_mesures = len(temperatures)      # int: 3
        derniere_temp = temperatures[-1]        # float: 17.8
        
        return {
            "toutes_temperatures": temperatures, # list
            "nombre": nombre_mesures,           # int
            "premiere": premiere_temp,           # float
            "derniere": derniere_temp,           # float
        }
        

class StationMeteo:
    def __init__(self):
        self.mesures = []                # list
        self.config = {}                 # dict
        self.villes_observees = set()    # set
        self.derniere_mesure = None      # None
    
    def creer_config_station(self):
        """Création d'une configuration avec un dictionnaire"""
        # Dictionnaire avec différents types de valeurs
        configuration = {}                      # dict vide
        
        # Ajout d'éléments un par un
        configuration["nom"] = "Station-Paris"  # str
        configuration["altitude"] = 35          # int
        configuration["latitude"] = 48.8566     # float
        configuration["active"] = True          # bool
        
        # Ou création directe
        config_complete = {
            "nom": "Station-Paris",             # str
            "altitude": 35,                     # int
            "latitude": 48.8566,                # float
            "longitude": 2.3522,                # float
            "active": True,                     # bool
            "capteurs": ["temperature", "humidite", "pression"]  # list
        }
        
        # Accès aux valeurs
        nom_station = config_complete["nom"]           # str
        est_active = config_complete["active"]         # bool
        nombre_capteurs = len(config_complete["capteurs"])  # int
        
        return config_complete                  # dict
    
    def gerer_villes_et_types_meteo(self):
        """Gestion des villes et types de météo avec sets et frozensets"""
        # Set mutable classique
        villes = set()                          # set vide
        villes.add("Paris")                     # set: {"Paris"}
        villes.add("Lyon")                      # set: {"Paris", "Lyon"}
        villes.add("Paris")                     # set: {"Paris", "Lyon"} (pas de doublon)
        
        # Conversion tuple → set pour modification
        types_meteo_tuple = ("ensoleillé", "pluvieux", "nuageux", "ensoleillé")  # tuple avec doublon
        types_meteo_set = set(types_meteo_tuple)    # set: {"ensoleillé", "pluvieux", "nuageux"} (doublons éliminés)
        
        # Conversion liste → set pour éliminer doublons
        temperatures_liste = [18, 22, 18, 25, 22, 20]  # list avec doublons
        temperatures_uniques = set(temperatures_liste)  # set: {18, 22, 25, 20} (doublons éliminés)
        
        types_meteo_set.add("orageux")              # set: {"ensoleillé", "pluvieux", "nuageux", "orageux"}
        
        # Conversion set → tuple si on veut l'immutabilité
        types_finaux = tuple(types_meteo_set)       # tuple: ("ensoleillé", "pluvieux", "nuageux", "orageux")
        
        # Frozenset : set immutable
        conditions_fixes = frozenset(["sec", "humide", "venteux"])  # frozenset
        # conditions_fixes.add("nouveau")  # ❌ Erreur : frozenset immutable
        
        # Opérations sur sets
        villes_france = {"Paris", "Lyon", "Marseille"}     # set
        villes_observees = {"Paris", "Berlin", "Madrid"}   # set
        villes_communes = villes_france & villes_observees  # set: {"Paris"} (intersection)
        toutes_villes = villes_france | villes_observees    # set: {"Paris", "Lyon", "Marseille", "Berlin", "Madrid"} (union)
        
        # Suppression d'éléments
        if "Berlin" in villes_observees:
            villes_observees.remove("Berlin")          # Supprime Berlin, erreur si absent
        villes_observees.discard("Tokyo")               # Supprime Tokyo si présent, sinon rien
        ville_supprimee = villes_observees.pop()        # Supprime et retourne un élément aléatoire : str
        
        # Tests de relations entre sets
        sont_disjoints = villes_france.isdisjoint({"Tokyo", "New York"})  # bool: True (aucun élément commun)
        
        # Vérifications
        paris_present = "Paris" in villes       # bool: True
        nombre_villes = len(villes)             # int: 2
        
        return {
            "villes_set": villes,               # set
            "types_meteo": types_meteo_set,     # set
            "temperatures_uniques": temperatures_uniques, # set
            "types_tuple": types_finaux,        # tuple
            "conditions_fixes": conditions_fixes, # frozenset
            "villes_communes": villes_communes,  # set
            "toutes_villes": toutes_villes,      # set
            "ville_supprimee": ville_supprimee,  # str
            "sont_disjoints": sont_disjoints,    # bool
            "nombre": nombre_villes             # int
        }
    
    def obtenir_mesure_ou_defaut(self, index=None):
        """Retourne une mesure spécifique ou la dernière si index=None"""
        if index is None:                   # Valeur par défaut
            return self.mesures[-1] if self.mesures else None
        return self.mesures[index]

    def configurer_seuils(self, temp_min=None, temp_max=None):
        """Configure les seuils de la station ou garde les valeurs par défaut"""
        if temp_min is None:
            temp_min = -10.0                # Valeur par défaut
        if temp_max is None:
            temp_max = 40.0                 # Valeur par défaut
        
        self.config["seuils"] = {"min": temp_min, "max": temp_max}
        return self.config
    
    def analyser_donnees_brutes(self, donnees_brutes):
        """Analyse des données brutes et retourne un résumé avec détection de patterns"""
        if not donnees_brutes:
            return dict()
        
        # Division en lignes individuelles
        lignes = donnees_brutes.splitlines()  # Sépare les lignes
        
        # Nettoyage des lignes
        lignes_nettoyees = [ligne.strip() for ligne in lignes]  # Nettoyage des espaces
        lignes_valides = [ligne for ligne in lignes_nettoyees if ligne]  # Filtre les lignes non vides
        
        # Détection de patterns avec différentes méthodes
        commentaires = [ligne for ligne in lignes_valides if ligne.startswith("#")]  # Commentaires
        mesures_temperature = [ligne for ligne in lignes_valides if "Température" in ligne and ligne.endswith("°C")]  # Températures
        alertes = [ligne for ligne in lignes_valides if "!" in ligne]  # Alertes
        
        stats = {
            "total_lignes": len(lignes_valides),  # Nombre total de lignes valides
            "lignes_commentaires": len(commentaires),  # Nombre de commentaires
            "lignes_temp": len(mesures_temperature),  # Lignes de température
            "lignes_alertes": len(alertes)  # Lignes d'alertes
        }
        return stats
    
    def filtrer_mesure_interactif(self):
        if not self.mesures:
            return list()
        
        print("""
        Sélectionnez un critère de filtrage:
        1. Par température (seuil minimum)
        2. Par ville (commence par)
        3. Par conditions (pluvieux ou non)
              """)
        choix = input("Entrez votre choix: ")
        if choix == "1":
            try:
                seuil = float(input("Entrez le seuil de température minimum: "))
                mesures_filtrees = ...
            except ValueError:
                ...


# Exemple d'utilisation

station = StationMeteo()
station.mesures.append({
    "humidité": 65,
    "température": 18.5,
    "ville": "Paris"
})
mesure_paris = Mesure(18.5, 65, 1013, "Paris", False)
print(mesure_paris.analyser_humidite())
print(mesure_paris.analyser_temperature())
print(mesure_paris.analyser_ville())
print(mesure_paris.analyser_conditions_meteo())
print(*mesure_paris.analyser_mesure_complete())
print(mesure_paris.stocker_mesures_simples())
print(station.gerer_villes_et_types_meteo())
# Exemple de création de configuration de station
config_station = station.creer_config_station()
print(f"\n🔧 Configuration de la station: {config_station}")
# mesure defaut et configurer seuil
mesure_defaut = station.obtenir_mesure_ou_defaut()
print(f"\n📊 Mesure par défaut: {mesure_defaut}")
seuils_configures = station.configurer_seuils(temp_min=0.0, temp_max=35.0)
print(f"\n📈 Seuils configurés: {seuils_configures}")

# Exemple d'analyse de données brutes
donnees_brutes = """
# Données météo
# Mesures de la station
Température: 18.5°C
Humidité: 65%
Pression: 1013 hPa
Alerte vent fort !
# Fin des mesures
"""

stats_analyse = station.analyser_donnees_brutes(donnees_brutes)
print(f"\n📊 Statistiques d'analyse des données brutes: {stats_analyse}")