# ============================================
# DEBUG AN ISBN VALIDATOR
# ============================================
# 
# ÉNONCÉ :
# L'ISBN (International Standard Book Number) est un identifiant unique
# attribué aux livres commerciaux. Il peut être composé de 10 ou 13 chiffres,
# et le dernier chiffre est un chiffre de contrôle calculé à partir des autres.
#
# Dans ce laboratoire, vous allez corriger le code existant d'un validateur ISBN.
#
# OBJECTIF : Remplir les user stories et faire passer tous les tests.
#
# RÈGLES DE VALIDATION :
# - ISBN-10 : 10 caractères, le dernier peut être 0-9 ou X
# - ISBN-13 : 13 chiffres, le dernier est 0-9
# - Le code ISBN ne doit pas contenir de tirets
# - Format d'entrée : "ISBN,longueur" (ex: "1530051126,10")
#
# ============================================

def validate_isbn(isbn, length):
    """
    Valide un code ISBN en vérifiant sa longueur et son chiffre de contrôle.
    
    Paramètres:
    isbn (str): Le code ISBN à valider (sans tirets)
    length (int): Longueur attendue (10 ou 13)
    
    Comportement:
    - Vérifie que la longueur correspond
    - Extrait les chiffres principaux et le chiffre de contrôle
    - Calcule le chiffre de contrôle attendu
    - Compare et affiche le résultat
    """
    
    # Vérifier que la longueur de l'ISBN correspond à la longueur spécifiée
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return
    
    # Extraire les chiffres principaux (tous sauf le dernier)
    # Pour ISBN-10: 9 premiers chiffres
    # Pour ISBN-13: 12 premiers chiffres
    main_digits = isbn[0:length-1]
    
    # Extraire le chiffre de contrôle donné (dernier caractère)
    given_check_digit = isbn[length-1]
    
    # Convertir les chiffres principaux en entiers
    try:
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        # Si un caractère non numérique est trouvé (sauf 'X' qui sera traité plus tard)
        print('Invalid character was found.')
        return
    
    # Calculer le chiffre de contrôle attendu selon la longueur
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:  # length == 13
        expected_check_digit = calculate_check_digit_13(main_digits_list)
    
    # Comparer le chiffre de contrôle donné avec celui calculé
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(main_digits_list):
    """
    Calcule le chiffre de contrôle pour un ISBN-10.
    
    Algorithme:
    1. Multiplier chacun des 9 premiers chiffres par son poids (10 à 2)
    2. Somme des résultats
    3. Trouver le reste de la division par 11
    4. Soustraire ce reste de 11
    5. Si résultat = 11 → chiffre = '0'
    6. Si résultat = 10 → chiffre = 'X'
    7. Sinon → chiffre = résultat (1-9)
    
    Paramètres:
    main_digits_list (list): Liste des 9 premiers chiffres
    
    Retourne:
    str: Le chiffre de contrôle attendu ('0'-'9' ou 'X')
    """
    digits_sum = 0
    
    # Multiplier chaque chiffre par son poids (10 à 2)
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    
    # Calcul du chiffre de contrôle
    result = 11 - (digits_sum % 11)
    
    # Conversion selon les règles ISBN-10
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    
    return expected_check_digit


def calculate_check_digit_13(main_digits_list):
    """
    Calcule le chiffre de contrôle pour un ISBN-13.
    
    Algorithme:
    1. Multiplier les chiffres par 1 et 3 alternativement (commençant par 1)
    2. Somme des résultats
    3. Trouver le reste de la division par 10
    4. Soustraire ce reste de 10
    5. Si résultat = 10 → chiffre = '0'
    6. Sinon → chiffre = résultat (1-9)
    
    Paramètres:
    main_digits_list (list): Liste des 12 premiers chiffres
    
    Retourne:
    str: Le chiffre de contrôle attendu ('0'-'9')
    """
    digits_sum = 0
    
    # Multiplier les chiffres par 1 et 3 alternativement
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:  # Position paire (0,2,4...) → poids 1
            digits_sum += digit * 1
        else:               # Position impaire (1,3,5...) → poids 3
            digits_sum += digit * 3
    
    # Calcul du chiffre de contrôle
    result = 10 - (digits_sum % 10)
    
    # Conversion selon les règles ISBN-13
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    
    return expected_check_digit


def main():
    """
    Fonction principale qui gère l'entrée utilisateur et orchestre la validation.
    
    Étapes:
    1. Demander à l'utilisateur de saisir l'ISBN et la longueur
    2. Séparer les valeurs par la virgule
    3. Valider le format d'entrée
    4. Valider la longueur (10 ou 13)
    5. Appeler validate_isbn pour la validation
    """
    
    # Demander à l'utilisateur de saisir l'ISBN et la longueur
    user_input = input('Enter ISBN and length: ')
    
    try:
        # Séparer les valeurs par la virgule
        values = user_input.split(',')
        
        # Vérifier qu'il y a exactement deux valeurs (ISBN et longueur)
        if len(values) != 2:
            print('Enter comma-separated values.')
            return
        
        # Extraire l'ISBN et la longueur
        isbn = values[0]
        length = int(values[1])  # Peut lever ValueError si non numérique
        
        # Vérifier que la longueur est 10 ou 13
        if length == 10 or length == 13:
            validate_isbn(isbn, length)
        else:
            print('Length should be 10 or 13.')
            
    except ValueError:
        # Gérer les erreurs de conversion de la longueur en nombre
        print('Length must be a number.')


# ============================================
# POINT D'ENTRÉE
# ============================================
# Note: La ligne suivante est commentée pour permettre aux tests de s'exécuter
# Décommentez-la pour tester manuellement le programme

# main()


# ============================================
# EXPLICATION DES CORRECTIONS APPORTÉES
# ============================================
#
# 1. IndentationError - Correction du retrait des fonctions
# 2. IndexError - Gestion des cas où split() ne retourne pas assez d'éléments
# 3. ValueError - Gestion des entrées non numériques pour la longueur
# 4. Off-by-one error - Correction dans l'extraction des chiffres
#    - main_digits = isbn[0:length-1] (était length-2)
#    - given_check_digit = isbn[length-1] (était length-2)
# 5. TypeError - Gestion correcte de la conversion des chiffres
# 6. Validation des caractères - Gestion du ValueError dans la conversion
#
# ============================================


# ============================================
# TESTS MANUELS (décommentez pour tester)
# ============================================

def run_tests():
    """
    Fonction de test manuel pour vérifier les différents cas.
    """
    print("="*50)
    print("TESTS DU VALIDATEUR ISBN")
    print("="*50)
    
    # Cas 1: ISBN-10 valide
    print("\n1. ISBN-10 valide (1530051126,10)")
    print("   Attendu: Valid ISBN Code.")
    print("   Résultat: ", end="")
    validate_isbn("1530051126", 10)
    
    # Cas 2: ISBN-13 valide
    print("\n2. ISBN-13 valide (9781530051120,13)")
    print("   Attendu: Valid ISBN Code.")
    print("   Résultat: ", end="")
    validate_isbn("9781530051120", 13)
    
    # Cas 3: ISBN-10 invalide (mauvais chiffre de contrôle)
    print("\n3. ISBN-10 invalide (1530051125,10)")
    print("   Attendu: Invalid ISBN Code.")
    print("   Résultat: ", end="")
    validate_isbn("1530051125", 10)
    
    # Cas 4: Mauvaise longueur (ISBN-13 avec longueur 10)
    print("\n4. ISBN-13 avec longueur 10 (9781530051120,10)")
    print("   Attendu: ISBN-10 code should be 10 digits long.")
    print("   Résultat: ", end="")
    validate_isbn("9781530051120", 10)
    
    # Cas 5: Mauvaise longueur (ISBN-10 avec longueur 13)
    print("\n5. ISBN-10 avec longueur 13 (1530051126,13)")
    print("   Attendu: ISBN-13 code should be 13 digits long.")
    print("   Résultat: ", end="")
    validate_isbn("1530051126", 13)
    
    # Cas 6: Caractères non numériques
    print("\n6. Caractères non numériques (15-0051126,10)")
    print("   Attendu: Invalid character was found.")
    print("   Résultat: ", end="")
    validate_isbn("15-0051126", 10)
    
    # Cas 7: Longueur invalide (9)
    print("\n7. Longueur invalide 9 (1530051126,9)")
    print("   Attendu: Length should be 10 or 13.")
    print("   Résultat direct dans le test simulateur")
    
    # Cas 8: Longueur non numérique
    print("\n8. Longueur non numérique (1530051125,A)")
    print("   Attendu: Length must be a number.")
    print("   Résultat direct dans le test simulateur")
    
    # Cas 9: Format non séparé par virgule
    print("\n9. Format non séparé par virgule (1530051125)")
    print("   Attendu: Enter comma-separated values.")
    print("   Résultat direct dans le test simulateur")
    
    # Cas 10: ISBN-10 valide avec X
    print("\n10. ISBN-10 valide avec X (080442957X,10)")
    print("    Attendu: Valid ISBN Code.")
    print("    Résultat: ", end="")
    validate_isbn("080442957X", 10)
    
    # Cas 11: ISBN-13 valide (9781947172104)
    print("\n11. ISBN-13 valide (9781947172104,13)")
    print("    Attendu: Valid ISBN Code.")
    print("    Résultat: ", end="")
    validate_isbn("9781947172104", 13)


# Décommentez pour exécuter les tests manuels
# run_tests()


# ============================================
# EXEMPLE DE SORTIE ATTENDUE
# ============================================
#
# Enter ISBN and length: 1530051126,10
# Valid ISBN Code.
#
# Enter ISBN and length: 9781530051120,13
# Valid ISBN Code.
#
# Enter ISBN and length: 1530051125,10
# Invalid ISBN Code.
#
# Enter ISBN and length: 9781530051120,10
# ISBN-10 code should be 10 digits long.
#
# Enter ISBN and length: 1530051126,13
# ISBN-13 code should be 13 digits long.
#
# Enter ISBN and length: 15-0051126,10
# Invalid character was found.
#
# Enter ISBN and length: 1530051126,9
# Length should be 10 or 13.
#
# Enter ISBN and length: 1530051125,A
# Length must be a number.
#
# Enter ISBN and length: 1530051125
# Enter comma-separated values.
#
# ============================================
# RÉSUMÉ DES CORRECTIONS EFFECTUÉES
# ============================================
#
# 1. Indentation : Tout le code a été correctement indenté
# 2. validate_isbn :
#    - Correction de l'extraction : isbn[0:length-1] (était length-2)
#    - Correction du check digit : isbn[length-1] (était length-2)
# 3. main() :
#    - Gestion du IndexError avec vérification de len(values) != 2
#    - Gestion du ValueError avec try/except
# 4. Gestion des caractères non numériques dans try/except
# 5. Commentaire de l'appel main() pour les tests
#
# ============================================