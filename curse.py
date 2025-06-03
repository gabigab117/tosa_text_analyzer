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
        
        # Classification simple
        if humidite_actuelle < seuil_bas:
            niveau = 1                           # int
            description = "Sec"                  # str
            ecart_seuil_bas = seuil_bas - humidite_actuelle  # int: manque pour atteindre seuil_bas
            ecart_info = f" Manque {ecart_seuil_bas} pour atteindre le seuil bas de {seuil_bas}."  # str

        elif humidite_actuelle < seuil_haut:
            niveau = 2                           # int
            description = "Normal"               # str
            ecart_seuil_haut = seuil_haut - humidite_actuelle  # int: manque pour atteindre seuil_haut
            ecart_info = f" Manque {ecart_seuil_haut} pour atteindre le seuil haut de {seuil_haut}."  # str
        else:
            niveau = 3                           # int
            description = "Humide"               # str
            ecart_seuil_haut = humidite_actuelle - seuil_haut  # int: dépasse le seuil_haut
            ecart_info = f" Dépasse de {ecart_seuil_haut} le seuil haut de {seuil_haut}."  # str

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

class StationMeteo:
    def __init__(self):
        self.mesures = []                # list[dict]
        self.config = {}                 # dict
        self.villes_observees = set()    # set
        self.derniere_mesure = None      # None
    
    def creer_config_station(self, nom, altitude, latitude, longitude, active=True):
        """Création d'une configuration avec un dictionnaire"""
        # Dictionnaire avec différents types de valeurs
        
        # Ajout d'éléments un par un
        self.config["nom"] = nom  # str
        self.config["altitude"] = altitude  # int
        self.config["latitude"] = latitude  # float
        self.config["longitude"] = longitude  # float
        self.config["active"] = active  # bool

        # Ou création directe
        self.config = {
            "nom": nom,             # str
            "altitude": altitude,   # int
            "latitude": latitude,   # float
            "longitude": longitude,  # float
            "active": active,       # bool
            "capteurs": ["temperature", "humidite", "pression"]  # list
        }
        
        # Accès aux valeurs
        _ = self.config["nom"]          # str
        _ = self.config["active"]         # bool
        _ = len(self.config["capteurs"])  # int

        return self.config                  # dict
    
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
    
    @staticmethod
    def analyser_donnees_brutes(donnees_brutes):
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
# Exemple de création de mesure
mesure_paris = Mesure(18.5, 65, 1013, "Paris", False)
print(mesure_paris.analyser_humidite())
print(mesure_paris.analyser_temperature())
print(mesure_paris.analyser_ville())
print(mesure_paris.analyser_conditions_meteo())
# Exemple de création de configuration de station
config_station = station.creer_config_station(
    nom="Station-Paris",
    altitude=35,
    latitude=48.8566,
    longitude=2.3522
)
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

# Exemple de manipulation de dictionnaire pour voir les différentes méthodes associées aux dictionnaires
config_station = station.creer_config_station(
    nom="Station-Paris",
    altitude=35,
    latitude=48.8566,
    longitude=2.3522
)

nom = config_station.get("nom")  # Accès avec get
altitude = config_station.get("altitude", 0)  # Valeur par défaut si clé absente
print("nom" in config_station) # bool: Vérifie si la clé "nom" existe
# keys, values, items
print(config_station.keys())  # Obtenir les clés
print(config_station.values())  # Obtenir les valeurs
print(config_station.items())  # Obtenir les paires clé-valeur

# update
config_station.update({"autre_information": "Informations supplémentaires"})  # Mise à jour avec un dictionnaire
print(config_station)

# setdefault
config_station.setdefault("version", "1.0")  # Définit une valeur par défaut si la clé n'existe pas

# suppression
print(config_station.pop("altitude", 0)) # Suppression de la clé "altitude" et retourne sa valeur, 0 si absente
print(config_station.popitem())  # Suppression de la dernière paire clé-valeur insérée


print("---\nManipulation des sets\n---")
station = StationMeteo()
station.villes_observees.add("Paris")        # set: {"Paris"}
station.villes_observees.add("Lyon")         # set: {"Paris", "Lyon"}  
station.villes_observees.add("Paris")        # set: {"Paris", "Lyon"} (pas de doublon)
station.villes_observees.add("Berlin")       # set: {"Paris", "Lyon", "Berlin"}

# Test d'appartenance
print("Paris" in station.villes_observees)  # bool: True

# Conversion tuple → set pour éliminer doublons
villes_tuple = ("Madrid", "Tokyo", "Madrid")  # tuple avec doublon
villes_depuis_tuple = set(villes_tuple)       # set: {"Madrid", "Tokyo"} (doublons éliminés)

# Conversion liste → set
villes_liste = ["Sydney", "Londres", "Sydney"]  # list avec doublons
villes_depuis_liste = set(villes_liste)         # set: {"Sydney", "Londres"} (doublons éliminés)

# Conversion set → tuple pour immutabilité
villes_tuple_final = tuple(station.villes_observees)    # tuple: ("Paris", "Lyon", "Berlin") immutable

# Frozenset : set immutable
villes_fixes = frozenset(["New York", "Rome"])  # frozenset: immutable

# Opérations sur sets
villes_france = {"Paris", "Lyon", "Marseille"}                  # set
communes = station.villes_observees & villes_france               # set: {"Paris", "Lyon"} (intersection)
toutes = station.villes_observees | villes_france                 # set: union

# Suppressions
station.villes_observees.discard("Tokyo")                         # Supprime si présent, sinon rien
ville_supprimee = station.villes_observees.pop()                  # str: supprime et retourne aléatoirement

# isdisjoint
print(station.villes_observees.isdisjoint(villes_france))  # bool: False (vérifie s'il n'y a pas d'éléments communs)