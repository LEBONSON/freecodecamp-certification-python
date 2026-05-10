# ============================================
# BUILD A NUMBER PATTERN GENERATOR
# ============================================
# 
# ÉNONCÉ :
# Dans ce laboratoire, vous allez pratiquer les bases de Python en construisant
# une petite application qui crée un motif de nombres.
#
# OBJECTIF : Remplissez les user stories ci-dessous et obtenez tous les tests
# à réussir pour terminer le laboratoire.
#
# HISTOIRES D'UTILISATEURS :
#
# 1. Vous devez définir une fonction nommée number_pattern qui prend un seul
#    paramètre n (représentant un entier positif).
#
# 2. number_pattern doit utiliser une boucle for.
#
# 3. number_pattern(n) doit retourner une chaîne avec tous les entiers
#    de 1 à n (inclus) séparés par un espace.
#    Exemple : number_pattern(4) doit retourner la chaîne "1 2 3 4".
#
# 4. Si l'argument passé à la fonction n'est pas un entier,
#    la fonction doit retourner "Argument must be an integer value."
#
# 5. Si l'argument passé à la fonction est inférieur à 1,
#    la fonction doit retourner "Argument must be an integer greater than 0."
#
# ============================================

def number_pattern(n):
    """
    Génère un motif de nombres de 1 à n séparés par des espaces.
    
    Paramètres:
    n (int): Un entier positif représentant la limite supérieure
    
    Retourne:
    str: Une chaîne contenant les nombres de 1 à n séparés par des espaces
         ou un message d'erreur si l'entrée est invalide
    """
    
    # Vérifier si l'argument est un entier
    if not isinstance(n, int):
        return "Argument must be an integer value."
    
    # Vérifier si l'argument est supérieur à 0
    if n < 1:
        return "Argument must be an integer greater than 0."
    
    # Construire le motif de nombres en utilisant une boucle for
    result = []
    for i in range(1, n + 1):
        result.append(str(i))
    
    # Joindre les nombres avec des espaces
    return " ".join(result)


# ============================================
# EXEMPLES D'UTILISATION
# ============================================
#
# number_pattern(4)   → "1 2 3 4"
# number_pattern(12)  → "1 2 3 4 5 6 7 8 9 10 11 12"
# number_pattern(1)   → "1"
# number_pattern(0)   → "Argument must be an integer greater than 0."
# number_pattern(-5)  → "Argument must be an integer greater than 0."
# number_pattern("5") → "Argument must be an integer value."
# number_pattern(4.5) → "Argument must be an integer value."
#
# ============================================