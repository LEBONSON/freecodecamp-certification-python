# ============================================
# BUILD AN RPG CHARACTER
# ============================================
# 
# ÉNONCÉ :
# Dans ce laboratoire, vous allez pratiquer les bases de Python en construisant
# une petite application qui crée un personnage pour une aventure RPG.
#
# OBJECTIF : Répondre aux critères utilisateur ci-dessous pour compléter le laboratoire.
#
# CRITÈRES UTILISATEUR :
# - Vous devez avoir une fonction nommée create_character.
# - La fonction doit accepter, dans l'ordre : un nom de personnage, suivi de trois statistiques :
#   force (strength), intelligence (intelligence) et charisme (charisma).
# - Le nom du personnage doit être validé :
#   • Si le nom n'est pas une chaîne de caractères → "The character name should be a string"
#   • Si le nom est une chaîne vide → "The character should have a name"
#   • Si le nom contient plus de 10 caractères → "The character name is too long"
#   • Si le nom contient des espaces → "The character name should not contain spaces"
# - Les statistiques doivent aussi être validées :
#   • Si une ou plusieurs stats ne sont pas des entiers → "All stats should be integers"
#   • Si une ou plusieurs stats sont inférieures à 1 → "All stats should be no less than 1"
#   • Si une ou plusieurs stats sont supérieures à 4 → "All stats should be no more than 4"
#   • Si la somme de toutes les stats est différente de 7 → "The character should start with 7 points"
# - Si toutes les valeurs passent la validation, la fonction doit retourner une chaîne avec quatre lignes :
#   • La première ligne contient le nom du personnage
#   • Les lignes 2-4 commencent par l'abréviation de la statistique (STR, INT ou CHA),
#     puis un espace, puis un nombre de points pleins (●) égal à la valeur de la statistique,
#     et un nombre de points vides (○) pour atteindre 10.
#
# EXEMPLE : create_character('ren', 4, 2, 1) doit retourner :
# ren
# STR ●●●●○○○○○○
# INT ●●○○○○○○○○
# CHA ●○○○○○○○○○
#
# NOTE : str et int sont des mots réservés en Python et ne doivent pas être utilisés
# comme noms de variables.
#
# ============================================

full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    """
    Crée un personnage RPG avec ses statistiques.
    
    Paramètres:
    name (str): Le nom du personnage
    strength (int): Force (1-4)
    intelligence (int): Intelligence (1-4)
    charisma (int): Charisme (1-4)
    
    Retourne:
    str: Le personnage formaté ou un message d'erreur
    """
    
    # ------------------------------------------
    # 1. VALIDATION DU NOM (name)
    # ------------------------------------------
    
    # Vérifie si le nom n'est pas une chaîne de caractères
    if type(name) != str:
        return "The character name should be a string"
    
    # Vérifie si le nom est une chaîne vide
    if name == "":
        return "The character should have a name"
    
    # Vérifie si le nom contient plus de 10 caractères
    if len(name) > 10:
        return "The character name is too long"
    
    # Vérifie si le nom contient des espaces
    if " " in name:
        return "The character name should not contain spaces"
    
    # ------------------------------------------
    # 2. VALIDATION DES STATISTIQUES
    # ------------------------------------------
    
    # Vérifie si toutes les stats sont des entiers
    if type(strength) != int or type(intelligence) != int or type(charisma) != int:
        return "All stats should be integers"
    
    # Vérifie si les stats sont au minimum 1
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    
    # Vérifie si les stats sont au maximum 4
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    
    # Vérifie si la somme des stats est égale à 7
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"
    
    # ------------------------------------------
    # 3. CONSTRUCTION DE LA SORTIE
    # ------------------------------------------
    
    # Fonction auxiliaire pour créer une ligne de statistiques
    def format_stat(stat_value):
        # stat_value : nombre de points pleins (1-4)
        # full_dot * stat_value : répète le point plein
        # empty_dot * (10 - stat_value) : complète avec des points vides jusqu'à 10
        return full_dot * stat_value + empty_dot * (10 - stat_value)
    
    # Construction des lignes
    result = name + "\n"                    # Ligne 1 : nom du personnage
    result += "STR " + format_stat(strength) + "\n"      # Ligne 2 : Force
    result += "INT " + format_stat(intelligence) + "\n"  # Ligne 3 : Intelligence
    result += "CHA " + format_stat(charisma)              # Ligne 4 : Charisme
    
    return result


# ============================================
# EXEMPLES DE TEST (décommentez pour tester)
# ============================================
# print(create_character('ren', 4, 2, 1))
# # Sortie attendue :
# # ren
# # STR ●●●●○○○○○○
# # INT ●●○○○○○○○○
# # CHA ●○○○○○○○○○
#
# print(create_character('gandalf', 2, 3, 2))
# # Sortie :
# # gandalf
# # STR ●●○○○○○○○○
# # INT ●●●○○○○○○○
# # CHA ●●○○○○○○○○
#
# # Tests des cas d'erreur :
# print(create_character(123, 4, 2, 1))    # "The character name should be a string"
# print(create_character('', 4, 2, 1))     # "The character should have a name"
# print(create_character('verylongname', 4, 2, 1))  # "The character name is too long"
# print(create_character('ren hero', 4, 2, 1))      # "The character name should not contain spaces"
# print(create_character('ren', 4.5, 2, 1))         # "All stats should be integers"
# print(create_character('ren', 0, 2, 1))           # "All stats should be no less than 1"
# print(create_character('ren', 5, 2, 1))           # "All stats should be no more than 4"
# print(create_character('ren', 4, 2, 2))           # "The character should start with 7 points" (4+2+2=8)

# ============================================
# RÉSUMÉ DE LA LOGIQUE :
# 1. Valider le nom (string, non vide, max 10 caractères, sans espaces)
# 2. Valider les stats (entiers, entre 1 et 4, somme = 7)
# 3. Formater la sortie avec ● et ○
# ============================================