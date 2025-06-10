import re


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

    def classifier_conditions_avancees(self):
        """Classification avancée avec opérateurs chainés et intervalles"""
        temp = self.temperature
        humidite = self.humidite
        pression = self.pression
        
        # Opérateurs chainés pour les intervalles
        temperature_froide = 0 <= temp < 10          # bool
        temperature_temperee = 10 <= temp <= 25      # bool
        temperature_chaude = temp > 25               # bool
        
        # Intervalles combinés
        confort_optimal = 15 <= temp <= 25 and 40 <= humidite <= 70  # bool
        risque_orage = pression < 1000 and humidite > 85             # bool
        
        # Score avec comparaisons multiples
        score_confort = (
            (1 if 18 <= temp <= 22 else 0) +
            (1 if 45 <= humidite <= 65 else 0) +
            (1 if 1013 <= pression <= 1020 else 0)
        )  # int: score de 0 à 3
        
        return {
            "temperature_froide": temperature_froide,
            "temperature_temperee": temperature_temperee,
            "temperature_chaude": temperature_chaude,
            "confort_optimal": confort_optimal,
            "risque_orage": risque_orage,
            "score_confort": score_confort
        }

    def analyser_conditions_logiques(self):
        """Démonstration des lois de De Morgan et transformations logiques"""
        temp = self.temperature
        humidite = self.humidite
        pluvieux = self.pluvieux
        
        # Conditions de base
        temp_normale = 15 <= temp <= 25
        humidite_normale = 40 <= humidite <= 70
        
        # Loi 1: not (A and B) ≡ (not A) or (not B)
        conditions_defavorables_v1 = not (temp_normale and humidite_normale)
        conditions_defavorables_v2 = (not temp_normale) or (not humidite_normale)
        
        # Loi 2: not (A or B) ≡ (not A) and (not B)
        pas_alerte_v1 = not (temp > 35 or humidite > 90)
        pas_alerte_v2 = (temp <= 35) and (humidite <= 90)
        
        # Simplification pratique
        alerte_complexe = not (not pluvieux and not (temp > 30 or humidite < 20))
        alerte_finale = pluvieux or temp > 30 or humidite < 20

        return {
            "equivalence_loi1": conditions_defavorables_v1 == conditions_defavorables_v2,
            "equivalence_loi2": pas_alerte_v1 == pas_alerte_v2,
            "simplification_reussie": alerte_complexe == alerte_finale
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
        """
        Analyse des données brutes et retourne un résumé avec détection de patterns.
        
        Cette méthode statique est conçue comme un utilitaire de traitement :
        elle reçoit des données textuelles brutes et produit un rapport d'analyse
        sans avoir besoin d'accéder aux données de l'instance.
        
        Args:
            donnees_brutes (str): Texte contenant des données météorologiques
            
        Returns:
            dict: Rapport d'analyse avec statistiques et données extraites
        """
        if not donnees_brutes:
            return dict()

        # Division en lignes individuelles
        lignes = donnees_brutes.splitlines()  # list: sépare les lignes

        # Nettoyage des lignes
        lignes_nettoyees = [ligne.strip() for ligne in lignes]  # list: nettoyage des espaces
        lignes_valides = [ligne for ligne in lignes_nettoyees if ligne]  # list: filtre les lignes non vides

        # Détection de patterns avec différentes méthodes
        commentaires = [ligne for ligne in lignes_valides if ligne.startswith("#")]  # list: commentaires
        mesures_temperature = [ligne for ligne in lignes_valides if "Température" in ligne and ligne.endswith("°C")]  # list: températures
        alertes = [ligne for ligne in lignes_valides if "!" in ligne]  # list: alertes

        # Statistiques d'analyse
        stats = {
            "total_lignes": len(lignes_valides),      # int: nombre total de lignes valides
            "lignes_commentaires": len(commentaires), # int: nombre de commentaires
            "lignes_temp": len(mesures_temperature),  # int: lignes de température
            "lignes_alertes": len(alertes),           # int: lignes d'alertes
            "commentaires": commentaires,             # list: commentaires extraits
            "temperatures": mesures_temperature,      # list: mesures de température
            "alertes": alertes                        # list: alertes détectées
        }
        return stats                                  # dict
    
    # StationMeteo
    def configurer_station_interactive(self):
        """Configuration interactive de la station avec validation des entrées"""
        print("=== Configuration de la station météorologique ===")
        
        # Saisie et validation du nom
        while True:
            nom = input("Nom de la station : ").strip()  # str: saisie utilisateur
            if nom and len(nom) >= 3:                    # Validation: non vide et longueur minimale
                break
            print("Le nom doit contenir au moins 3 caractères.")
        
        # Saisie de l'altitude avec gestion d'erreurs
        while True:
            try:
                altitude_str = input("Altitude (en mètres) : ")  # str: saisie brute
                altitude = int(altitude_str)                     # int: conversion
                if altitude >= 0:                                # Validation: altitude positive
                    break
                print("L'altitude doit être positive.")
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")
        
        # Choix du type de station
        print("\nType de station :")
        print("1. Urbaine")
        print("2. Rurale") 
        print("3. Côtière")
        
        types_station = {"1": "urbaine", "2": "rurale", "3": "cotiere"}  # dict: mapping choix
        
        while True:
            choix = input("Votre choix (1, 2 ou 3) : ").strip()  # str: choix utilisateur
            if choix in types_station:
                type_station = types_station[choix]               # str: type validé
                break
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
        
        # Stockage de la configuration
        self.config = {
            "nom": nom,                              # str
            "altitude": altitude,                    # int
            "type": type_station,                    # str
            "active": True                           # bool
        }
        
        return self.config                           # dict
    
    # StationMeteo
    @staticmethod
    def extraire_donnees_avec_regex(texte_donnees):
        """Extrait des données météorologiques avec des expressions régulières"""
        if not texte_donnees:
            return dict()
        
        # Patterns pour différents types de données
        patterns = {
            # Températures : "18.5°C" ou "Température: 18.5°C"
            "temperatures": re.findall(r"(?:Température:\s*)?(-?\d+(?:\.\d+)?)°C", texte_donnees),  # list
            
            # Humidité : "65%" ou "Humidité: 65%"
            "humidites": re.findall(r"(?:Humidité:\s*)?(\d+)%", texte_donnees),  # list
            
            # Pressions : "1013 hPa" ou "Pression: 1013 hPa"
            "pressions": re.findall(r"(?:Pression:\s*)?(\d+)\s*hPa", texte_donnees),  # list
            
            # Dates au format DD/MM/YYYY
            "dates": re.findall(r"(\d{2}/\d{2}/\d{4})", texte_donnees),  # list
            
            # Heures au format HH:MM
            "heures": re.findall(r"(\d{2}:\d{2})", texte_donnees),  # list
        }
        
        # Conversion des types pour les valeurs numériques
        donnees_extraites = {
            "temperatures": [float(temp) for temp in patterns["temperatures"]],  # list[float]
            "humidites": [int(hum) for hum in patterns["humidites"]],            # list[int]
            "pressions": [int(press) for press in patterns["pressions"]],        # list[int]
            "dates": patterns["dates"],                                          # list[str]
            "heures": patterns["heures"],                                        # list[str]
            "total_mesures": len(patterns["temperatures"])                       # int
        }
        
        return donnees_extraites                     # dict
    
    # StationMeteo
    def generer_rapport_station(self):
        """Génère un rapport formaté de la station avec différentes techniques de formatage"""
        if not self.config:
            return "Station non configurée"
        
        # Template avec .format()
        template_titre = "=== Rapport de la station {nom} ===".format(nom=self.config["nom"])  # str
        
        # Informations de base avec f-strings et formatage numérique
        nom_station = self.config["nom"]             # str
        altitude = self.config["altitude"]           # int
        type_station = self.config["type"]           # str
        
        info_base = f"Station: {nom_station} (Type: {type_station}, Altitude: {altitude:,} m)"  # str
        
        # Formatage conditionnel
        status_mesures = f"Nombre de mesures: {len(self.mesures)}" if self.mesures else "Aucune mesure"  # str
        
        # Exemples de formatage f-string avancé
        from datetime import datetime
        maintenant = datetime.now()
        
        # Formatage de date/heure avec zéros de tête
        horodatage = f"Généré le {maintenant.day:02d}/{maintenant.month:02d}/{maintenant.year} à {maintenant.hour:02d}:{maintenant.minute:02d}"  # str
        
        # Formatage avec pourcentage et précision
        if self.mesures:
            objectif_mesures = 50  # Objectif de 50 mesures par jour
            pourcentage_activite = (len(self.mesures) / objectif_mesures) * 100
            activite = f"Objectif atteint: {pourcentage_activite:6.1f}%"  # str: largeur 6, 1 décimale
        else:
            activite = "Objectif atteint: N/A"       # str
        
        # Formatage avec alignement et padding
        status_format = f"Status: {self.config.get('active', False):>10}"  # str: alignement droite sur 10 caractères
        
        # Assembly final du rapport avec join()
        lignes_rapport = [template_titre, "=" * 40, info_base, status_mesures, horodatage, activite, status_format]  # list
        
        return "\n".join(lignes_rapport)             # str: assemblage avec sauts de ligne

    # StationMeteo
    def valider_coherence_donnees(self, donnees_mesures):
        """Valide la cohérence d'un lot de mesures avec expressions booléennes"""
        if not donnees_mesures:
            return {"toutes_valides": True, "details": "Aucune donnée"}
        
        # Vérifications avec all()
        toutes_temperatures_valides = all(-50 <= m["temp"] <= 60 for m in donnees_mesures)  # bool
        toutes_humidites_valides = all(0 <= m["humidite"] <= 100 for m in donnees_mesures)  # bool
        
        # Vérifications avec any()
        au_moins_une_pluie = any(m["pluvieux"] for m in donnees_mesures)  # bool
        temperature_elevee = any(m["temp"] > 30 for m in donnees_mesures)  # bool
        
        # Combinaison all() + logique
        coherence_pluie = all(not m["pluvieux"] or m["humidite"] > 60 for m in donnees_mesures)  # bool
        
        return {
            "toutes_valides": all([toutes_temperatures_valides, toutes_humidites_valides, coherence_pluie]),
            "details": {
                "temperatures": toutes_temperatures_valides,
                "humidites": toutes_humidites_valides,
                "presence_pluie": au_moins_une_pluie,
                "temperature_elevee": temperature_elevee
            }
        }

    # StationMeteo  
    def analyser_tendances_optimise(self, donnees_nouvelles):
        """Analyse optimisée des tendances avec l'opérateur walrus"""
        if not donnees_nouvelles:
            return {}
        
        # Walrus dans une condition
        if (nb_mesures := len(donnees_nouvelles)) >= 5:
            tendances = {"echantillon_suffisant": True, "taille": nb_mesures}
            
            # Calcul de moyenne avec walrus
            if (temp_moyenne := sum(m["temp"] for m in donnees_nouvelles) / nb_mesures) > 25:
                tendances["periode_chaude"] = True
                tendances["temperature_moyenne"] = temp_moyenne
        else:
            tendances = {"echantillon_suffisant": False, "taille": nb_mesures}
        
        # Walrus dans une compréhension
        temperatures_ajustees = [
            temp_ajustee
            for mesure in donnees_nouvelles
            if (temp_ajustee := mesure["temp"] + 0.5) > 20
        ]
        
        tendances["temperatures_ajustees"] = temperatures_ajustees
        return tendances

    # StationMeteo
    @staticmethod
    def analyser_avec_operateurs_ternaires(donnees_mesures):
        """Utilisation des opérateurs ternaires et gestion de la précédence"""
        if not donnees_mesures:
            return {}
        
        analyses = []
        for mesure in donnees_mesures:
            temp = mesure["temp"]
            humidite = mesure["humidite"]
            
            # Opérateurs ternaires
            classification = "Chaud" if temp > 25 else "Froid"
            confort = "Excellent" if 18 <= temp <= 22 and 45 <= humidite <= 65 else "Moyen"
            
            # Précédence des opérateurs
            # and a une précédence plus élevée que or
            condition_precedence = temp > 30 or humidite > 80 and mesure["pluvieux"]
            # Équivaut à: temp > 30 or (humidite > 80 and mesure["pluvieux"])
            
            # Avec parenthèses pour changer l'ordre
            condition_modifiee = (temp > 30 or humidite > 80) and mesure["pluvieux"]
            
            # Score avec précédence contrôlée
            score = (3 if temp > 35 else 1) * (2 if humidite > 80 else 1)
            
            analyses.append({
                "ville": mesure["ville"],
                "classification": classification,
                "confort": confort,
                "precedence_demo": condition_precedence != condition_modifiee,
                "score": score
            })
        
        return {"analyses": analyses}

# Exemple d'utilisation
donnees_test = [
    {"temp": 28, "humidite": 75, "ville": "Paris", "pluvieux": True},
    {"temp": 15, "humidite": 45, "ville": "Lyon", "pluvieux": False},
    {"temp": 35, "humidite": 85, "ville": "Marseille", "pluvieux": False}
]

analyse = StationMeteo.analyser_avec_operateurs_ternaires(donnees_test)
for a in analyse["analyses"]:
    print(f"{a['ville']}: {a['classification']} (Score: {a['score']})")
