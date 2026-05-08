# ============================================
# BUILD A GAME CHARACTER STATS TRACKER
# ============================================
# 
# ÉNONCÉ :
# Dans ce laboratoire, vous allez construire un système de suivi des statistiques
# d'un personnage de jeu. Le programme permet de créer un personnage avec des
# attributs spécifiques, de mettre à jour ces attributs et de récupérer les
# statistiques actuelles du personnage.
#
# OBJECTIF : Répondre aux critères utilisateur ci-dessous pour compléter le laboratoire.
#
# CRITÈRES UTILISATEUR :
#
# 1. Créer une classe nommée GameCharacter qui représente un personnage de jeu
#    et gère les statistiques du personnage.
#
# 2. Lors de l'instanciation, un nouvel objet GameCharacter doit avoir les attributs suivants :
#    - _name : défini avec la chaîne donnée au moment de l'instanciation
#    - _health : défini à 100
#    - _mana : défini à 50
#    - _level : défini à 1
#
# 3. Créer une propriété name en lecture seule pour accéder au nom du personnage.
#
# 4. Pour la propriété health :
#    - Définir un getter qui retourne la santé actuelle
#    - Définir un setter qui empêche la santé d'être inférieure à 0
#    - Le setter doit limiter la santé à un maximum de 100
#
# 5. Pour la propriété mana :
#    - Définir un getter qui retourne le mana actuel
#    - Définir un setter qui empêche le mana d'être inférieur à 0
#    - Le setter doit limiter le mana à un maximum de 50
#
# 6. Créer un getter pour level qui retourne le niveau actuel du personnage.
#
# 7. Définir une méthode nommée level_up qui :
#    - Augmente le niveau du personnage de 1
#    - Réinitialise la santé à 100 et le mana à 50 (via les setters)
#    - Affiche un message : "<name> leveled up to <level>!"
#
# 8. Définir une méthode __str__ qui retourne une chaîne formatée incluant :
#    - Le nom du personnage
#    - Le niveau du personnage
#    - La santé actuelle
#    - Le mana actuel
#
# EXEMPLE D'UTILISATION :
# hero = GameCharacter('Kratos')
# print(hero)
# hero.health -= 30
# hero.mana -= 10
# print(hero)
# hero.level_up()
# print(hero)
#
# ============================================

class GameCharacter:
    """
    Classe représentant un personnage de jeu avec ses statistiques.
    
    Attributs privés:
    _name (str): Nom du personnage (lecture seule)
    _health (int): Points de vie du personnage (0-100)
    _mana (int): Points de mana du personnage (0-50)
    _level (int): Niveau du personnage (augmente avec level_up)

    """
    
    # ------------------------------------------
    # 1. MÉTHODE CONSTRUCTEUR __init__
    # ------------------------------------------
    # Initialise un nouveau personnage avec ses statistiques de base
    
    def __init__(self, name):
        """
        Constructeur de la classe GameCharacter.
        
        Paramètres:
        name (str): Nom du personnage
        
        Initialise:
        - _name avec le nom donné
        - _health à 100 (santé maximale)
        - _mana à 50 (mana maximal)
        - _level à 1 (début du jeu)

        """
        self._name = name      # Nom du personnage (privé, lecture seule)
        self._health = 100     # Santé initiale : 100 points
        self._mana = 50        # Mana initial : 50 points
        self._level = 1        # Niveau initial : 1
    
    # ------------------------------------------
    # 2. PROPRIÉTÉ name (GETTER uniquement - READ ONLY)
    # ------------------------------------------
    # Permet un accès en lecture seule au nom du personnage
    """
        Getter pour l'attribut name.
        Retourne:
        str: Le nom du personnage (lecture seule, pas de setter)
        """
    @property
    def name(self):

        return self._name
    
    # ------------------------------------------
    # 3. PROPRIÉTÉ health (GETTER + SETTER avec validation)
    # ------------------------------------------
    # Gère les points de vie avec des limites (0 minimum, 100 maximum)
    """
        Getter pour l'attribut health.
        
        Retourne:
        int: La santé actuelle du personnage

        """

    @property
    def health(self):
        
        return self._health
    
    @health.setter
    def health(self, value):
        """
        Setter pour l'attribut health avec validation des limites.
        
        Règles de validation:
        - Si value < 0     → health = 0 (limite minimale)
        - Si value > 100   → health = 100 (limite maximale)
        - Sinon            → health = value (valeur normale)
        
        Paramètres:
        value (int): Nouvelle valeur de santé

        """
        # Éviter que la santé tombe en dessous de 0
        if value < 0:
            self._health = 0
        
        # Éviter que la santé dépasse 100
        elif value > 100:
            self._health = 100
        
        # Valeur dans les limites acceptables
        else:
            self._health = value
    
    # ------------------------------------------
    # 4. PROPRIÉTÉ mana (GETTER + SETTER avec validation)
    # ------------------------------------------
    # Gère les points de mana avec des limites (0 minimum, 50 maximum)
    """
        Getter pour l'attribut mana.
        
        Retourne:
        int: Le mana actuel du personnage

        """

    @property
    def mana(self):
        
        return self._mana
    
    @mana.setter
    def mana(self, value):
        """
        Setter pour l'attribut mana avec validation des limites.
        
        Règles de validation:
        - Si value < 0     → mana = 0 (limite minimale)
        - Si value > 50    → mana = 50 (limite maximale)
        - Sinon            → mana = value (valeur normale)
        
        Paramètres:
        value (int): Nouvelle valeur de mana

        """
        # Éviter que le mana tombe en dessous de 0
        if value < 0:
            self._mana = 0
        
        # Éviter que le mana dépasse 50
        elif value > 50:
            self._mana = 50
        
        # Valeur dans les limites acceptables
        else:
            self._mana = value
    
    # ------------------------------------------
    # 5. PROPRIÉTÉ level (GETTER uniquement)
    # ------------------------------------------
    # Permet d'accéder au niveau actuel du personnage
    
    """
        Getter pour l'attribut level.
        
        Retourne:
        int: Le niveau actuel du personnage

        """
    @property
    def level(self):
        
        return self._level
    
    # ------------------------------------------
    # 6. MÉTHODE level_up
    # ------------------------------------------
    # Augmente le niveau et restaure les statistiques
    
    """
        Fait monter le personnage d'un niveau.
        
        Effets:
        - Augmente _level de 1
        - Restaure la santé à 100 (via le setter health)
        - Restaure le mana à 50 (via le setter mana)
        - Affiche un message de promotion
        
        Le message utilise les propriétés name et level pour
        afficher les valeurs actuelles après l'augmentation.

        """


    def level_up(self):
        
        # Augmenter le niveau de 1
        self._level += 1
        
        # Restaurer la santé à son maximum (100)
        # Utilisation du setter health (avec validation)
        self.health = 100
        
        # Restaurer le mana à son maximum (50)
        # Utilisation du setter mana (avec validation)
        self.mana = 50
        
        # Afficher le message de niveau supérieur
        # Note: self.level retourne le NOUVEAU niveau (après incrémentation)
        print(f"{self.name} leveled up to {self.level}!")
    
    # ------------------------------------------
    # 7. MÉTHODE __str__
    # ------------------------------------------
    # Représentation string du personnage pour l'affichage
    
    """
        Représentation string du personnage pour print().
        
        Retourne une chaîne formatée avec toutes les statistiques :
        - Name : nom du personnage
        - Level : niveau actuel
        - Health : points de vie actuels
        - Mana : points de mana actuels
        
        Retourne:
        str: Format multi-lignes des statistiques du personnage

        """
        
    def __str__(self):
        
        return f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}"


# ============================================
# EXEMPLES D'UTILISATION
# ============================================

# Création d'un nouveau personnage
hero = GameCharacter('Kratos')  # Crée un personnage nommé Kratos
print(hero)  # Affiche les statistiques du personnage
# Sortie attendue :
# Name: Kratos
# Level: 1
# Health: 100
# Mana: 50

# Modification des statistiques
hero.health -= 30  # Diminue la santé de 30 (devient 70)
hero.mana -= 10    # Diminue le mana de 10 (devient 40)
print(hero)  # Affiche les statistiques mises à jour
# Sortie attendue :
# Name: Kratos
# Level: 1
# Health: 70
# Mana: 40

# Montée de niveau
hero.level_up()  # Le personnage monte au niveau 2
# Sortie : Kratos leveled up to 2!
print(hero)  # Affiche les statistiques après la montée de niveau
# Sortie attendue :
# Name: Kratos
# Level: 2
# Health: 100
# Mana: 50


# ============================================
# TESTS SUPPLÉMENTAIRES
# ============================================

# Test des limites de santé
print("\n--- Tests des limites de santé ---")
test_char = GameCharacter("Test")
print(f"Santé initiale : {test_char.health}")
test_char.health = -50  # Tentative de mettre une santé négative
print(f"After health = -50 → {test_char.health} (doit être 0)")
test_char.health = 200  # Tentative de dépasser 100
print(f"After health = 200 → {test_char.health} (doit être 100)")
test_char.health = 75   # Valeur normale
print(f"After health = 75 → {test_char.health} (doit être 75)")

# Test des limites de mana
print("\n--- Tests des limites de mana ---")
test_char.mana = -30    # Tentative de mettre un mana négatif
print(f"After mana = -30 → {test_char.mana} (doit être 0)")
test_char.mana = 100    # Tentative de dépasser 50
print(f"After mana = 100 → {test_char.mana} (doit être 50)")
test_char.mana = 25     # Valeur normale
print(f"After mana = 25 → {test_char.mana} (doit être 25)")

# Test des niveaux multiples
print("\n--- Tests de montée de niveaux ---")
multi_char = GameCharacter("Multi")
for i in range(5):
    print(f"Niveau {multi_char.level} : Health={multi_char.health}, Mana={multi_char.mana}")
    multi_char.level_up()

# ============================================
# RÉSUMÉ DE LA LOGIQUE :
# 1. Attributs privés avec underscore (_name, _health, _mana, _level)
# 2. Propriétés avec décorateurs @property pour un accès contrôlé
# 3. Setters avec validation pour éviter les valeurs invalides
# 4. Méthode level_up qui incrémente et restaure les stats
# 5. Méthode __str__ pour un affichage propre et formaté
# ============================================