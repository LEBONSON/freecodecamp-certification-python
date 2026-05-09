# ============================================
# CRÉER UN GESTIONNAIRE DE CONFIGURATION UTILISATEUR
# ============================================
# 
# ÉNONCÉ :
# Dans ce laboratoire, vous créerez un gestionnaire de configuration utilisateur
# qui permet aux utilisateurs de gérer leurs paramètres tels que le thème,
# la langue et les notifications. Vous implémenterez des fonctions pour ajouter,
# mettre à jour, supprimer et afficher les paramètres utilisateur.
#
# OBJECTIF : Remplissez les user stories ci-dessous et obtenez tous les tests
# à réussir pour terminer le laboratoire.
#
# HISTOIRES D'UTILISATEURS :
#
# 1. Vous devez définir une fonction nommée add_setting avec deux paramètres
#    représentant un dictionnaire de paramètres et un tuple contenant une paire clé-valeur
#
# 2. add_setting devrait :
#    - Convertir la clé et la valeur en minuscules.
#    - Si le paramètre de clé existe, retourner "Setting '[key]' already exists! Cannot add a new setting with this name."
#    - Si le paramètre clé n'existe pas, ajouter la paire clé-valeur au dictionnaire
#      et retourner "Setting '[key]' added with value '[value]' successfully!"
#    - Les messages retournés doivent avoir la clé et la valeur en minuscules.
#
# 3. Vous devez définir une fonction nommée update_setting avec deux paramètres
#    représentant un dictionnaire de paramètres et un tuple contenant une paire clé-valeur.
#
# 4. update_setting devrait :
#    - Convertir la clé et la valeur en minuscules.
#    - Si le paramètre clé existe, mettre à jour sa valeur et retourner
#      "Setting '[key]' updated to '[value]' successfully!"
#    - Si le paramètre de clé n'existe pas, retourner
#      "Setting '[key]' does not exist! Cannot update a non-existing setting."
#    - Les messages retournés doivent avoir la clé et la valeur en minuscules.
#
# 5. Vous devez définir une fonction nommée delete_setting avec deux paramètres
#    représentant un dictionnaire de paramètres et une clé.
#
# 6. delete_setting devrait :
#    - Convertir la clé passée en minuscules.
#    - Si le paramètre clé existe, supprimer la paire clé-valeur et retourner
#      "Setting '[key]' deleted successfully!"
#    - Si le paramètre de clé n'existe pas, retourner "Setting not found!"
#    - Les messages retournés doivent avoir la clé en minuscules.
#
# 7. Vous devez définir une fonction nommée view_settings avec un paramètre
#    représentant un dictionnaire de paramètres.
#
# 8. view_settings devrait :
#    - Retourner "No settings available." si le dictionnaire est vide.
#    - Si le dictionnaire contient des paramètres, retourner une chaîne affichant
#      les paramètres. La chaîne doit commencer par "Current User Settings:"
#      suivi des paires clé-valeur, chacune sur une nouvelle ligne et avec la clé
#      en majuscule (première lettre en majuscule).
#
# 9. Pour tester le code, vous devez créer un dictionnaire nommé test_settings
#    pour stocker quelques préférences de configuration utilisateur.
#
# ============================================

# ------------------------------------------
# 1. FONCTION add_setting
# ------------------------------------------
# Ajoute un nouveau paramètre de configuration
# ==========================================

def add_setting(setting_dict, setting_tuple):
    """
    Ajoute un nouveau paramètre de configuration.
    
    Paramètres:
    setting_dict (dict): Dictionnaire des paramètres existants
    setting_tuple (tuple): Tuple contenant (clé, valeur) du nouveau paramètre
    
    Retourne:
    str: Message de succès ou d'erreur
    
    Règles:
    - Convertit la clé et la valeur en minuscules
    - Vérifie si la clé existe déjà
    - Si la clé n'existe pas, l'ajoute au dictionnaire
    """
    
    # Extraire la clé et la valeur du tuple
    key, value = setting_tuple
    
    # Convertir la clé et la valeur en minuscules (normalisation)
    key = key.lower()
    value = value.lower()
    
    # Vérifier si la clé existe déjà dans le dictionnaire
    if key in setting_dict:
        # Cas d'erreur : la clé existe déjà
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        # Cas de succès : ajouter la nouvelle paire clé-valeur
        setting_dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"


# ------------------------------------------
# 2. FONCTION update_setting
# ------------------------------------------
# Met à jour un paramètre de configuration existant
# ==========================================

def update_setting(setting_dict, setting_tuple):
    """
    Met à jour un paramètre de configuration existant.
    
    Paramètres:
    setting_dict (dict): Dictionnaire des paramètres existants
    setting_tuple (tuple): Tuple contenant (clé, valeur) du paramètre à mettre à jour
    
    Retourne:
    str: Message de succès ou d'erreur
    
    Règles:
    - Convertit la clé et la valeur en minuscules
    - Vérifie si la clé existe
    - Si la clé existe, met à jour sa valeur
    """
    
    # Extraire la clé et la valeur du tuple
    key, value = setting_tuple
    
    # Convertir la clé et la valeur en minuscules (normalisation)
    key = key.lower()
    value = value.lower()
    
    # Vérifier si la clé existe dans le dictionnaire
    if key in setting_dict:
        # Cas de succès : mettre à jour la valeur existante
        setting_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        # Cas d'erreur : la clé n'existe pas
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


# ------------------------------------------
# 3. FONCTION delete_setting
# ------------------------------------------
# Supprime un paramètre de configuration
# ==========================================

def delete_setting(setting_dict, key):
    """
    Supprime un paramètre de configuration.
    
    Paramètres:
    setting_dict (dict): Dictionnaire des paramètres existants
    key (str): Clé du paramètre à supprimer
    
    Retourne:
    str: Message de succès ou d'erreur
    
    Règles:
    - Convertit la clé en minuscules
    - Vérifie si la clé existe
    - Si la clé existe, la supprime du dictionnaire
    """
    
    # Convertir la clé en minuscules (normalisation)
    key = key.lower()
    
    # Vérifier si la clé existe dans le dictionnaire
    if key in setting_dict:
        # Cas de succès : supprimer la clé
        del setting_dict[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        # Cas d'erreur : la clé n'existe pas
        return "Setting not found!"


# ------------------------------------------
# 4. FONCTION view_settings
# ------------------------------------------
# Affiche tous les paramètres de configuration
# ==========================================

def view_settings(setting_dict):
    """
    Affiche tous les paramètres de configuration.
    
    Paramètres:
    setting_dict (dict): Dictionnaire des paramètres à afficher
    
    Retourne:
    str: Affichage formaté des paramètres ou message si vide
    
    Règles:
    - Si le dictionnaire est vide, retourne "No settings available."
    - Sinon, retourne "Current User Settings:" suivi de chaque paramètre
    - Chaque paramètre est sur une nouvelle ligne
    - La clé a sa première lettre en majuscule (capitalize)
    """
    
    # Vérifier si le dictionnaire est vide
    if not setting_dict:
        return "No settings available."
    
    # Initialiser la chaîne de résultat avec l'en-tête
    result = "Current User Settings:\n"
    
    # Parcourir toutes les paires clé-valeur du dictionnaire
    for key, value in setting_dict.items():
        # Ajouter chaque paramètre formaté
        # .capitalize() met la première lettre en majuscule
        result = result + f"{key.capitalize()}: {value}\n"
    
    # Retourner la chaîne complète
    return result


# ------------------------------------------
# 5. TESTS ET EXEMPLES
# ------------------------------------------
# Création du dictionnaire de test
# ==========================================

# Créer un dictionnaire vide pour les tests
test_settings = {}

# Ajouter des paramètres de configuration initiaux
add_setting(test_settings, ('theme', 'light'))        # Ajoute theme: light
add_setting(test_settings, ('language', 'english'))   # Ajoute language: english
add_setting(test_settings, ('notifications', 'enabled'))  # Ajoute notifications: enabled


# ==========================================
# EXEMPLES D'UTILISATION SUPPLÉMENTAIRES
# ==========================================

# Exemple 1: Afficher tous les paramètres
# print(view_settings(test_settings))
# Résultat attendu:
# Current User Settings:
# Theme: light
# Language: english
# Notifications: enabled

# Exemple 2: Ajouter un paramètre qui existe déjà
# print(add_setting(test_settings, ('theme', 'dark')))
# Résultat: Setting 'theme' already exists! Cannot add a new setting with this name.

# Exemple 3: Mettre à jour un paramètre existant
# print(update_setting(test_settings, ('theme', 'dark')))
# Résultat: Setting 'theme' updated to 'dark' successfully!

# Exemple 4: Mettre à jour un paramètre qui n'existe pas
# print(update_setting(test_settings, ('volume', 'high')))
# Résultat: Setting 'volume' does not exist! Cannot update a non-existing setting.

# Exemple 5: Supprimer un paramètre existant
# print(delete_setting(test_settings, 'language'))
# Résultat: Setting 'language' deleted successfully!

# Exemple 6: Supprimer un paramètre qui n'existe pas
# print(delete_setting(test_settings, 'volume'))
# Résultat: Setting not found!

# Exemple 7: Afficher après modifications
# print(view_settings(test_settings))


# ==========================================
# TESTS DE VALIDATION
# ==========================================

# Test de conversion en minuscules automatique
print("\n--- Test de conversion en minuscules ---")
test_dict = {}
print(add_setting(test_dict, ('THEME', 'LIGHT')))  # Devient 'theme', 'light'
print(f"Dictionnaire après ajout: {test_dict}")    # {'theme': 'light'}

# Test de mise à jour avec casse différente
print(update_setting(test_dict, ('THEME', 'DARK')))  # Trouve 'theme', met à jour
print(f"Dictionnaire après mise à jour: {test_dict}") # {'theme': 'dark'}

# Test de suppression avec casse différente
print(delete_setting(test_dict, 'THEME'))  # Trouve 'theme', supprime
print(f"Dictionnaire après suppression: {test_dict}") # {}


# ==========================================
# RÉSUMÉ DE LA LOGIQUE :
# 1. add_setting : ajoute une nouvelle paire clé-valeur (clé unique)
# 2. update_setting : modifie une valeur existante
# 3. delete_setting : supprime une paire clé-valeur existante
# 4. view_settings : affiche toutes les paires formatées
# 5. Normalisation : toutes les clés sont stockées en minuscules
# 6. Les clés sont affichées avec la première lettre en majuscule
# ==========================================