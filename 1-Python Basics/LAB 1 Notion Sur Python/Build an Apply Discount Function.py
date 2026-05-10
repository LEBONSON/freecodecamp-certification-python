# ============================================
# BUILD AN APPLY DISCOUNT FUNCTION
# ============================================
# 
# ÉNONCÉ :
# Dans ce laboratoire, vous allez écrire une fonction qui calcule le prix final
# d'un article après application d'un pourcentage de réduction.
#
# Exemple : Si le prix d'un article est 50 et qu'une réduction de 20 est appliquée,
# le montant de la réduction est 10 et le prix final est 40.
#
# OBJECTIF : Répondre aux critères utilisateur ci-dessous pour compléter le laboratoire.
#
# CRITÈRES UTILISATEUR :
# - Vous devez définir une fonction nommée apply_discount.
# - La fonction apply_discount doit prendre exactement deux paramètres : price et discount.
# - Si price n'est pas un nombre (int ou float), la fonction doit retourner la chaîne
#   "The price should be a number".
# - Si discount n'est pas un nombre (int ou float), la fonction doit retourner la chaîne
#   "The discount should be a number".
# - Si price est inférieur ou égal à 0, la fonction doit retourner la chaîne
#   "The price should be greater than 0".
# - Si discount est inférieur à 0 ou supérieur à 100, la fonction doit retourner la chaîne
#   "The discount should be between 0 and 100".
# - Si les deux entrées sont valides, la fonction doit calculer la réduction en pourcentage du prix.
# - La fonction doit retourner le prix final après application de la réduction.
#
# ============================================

def apply_discount(price, discount):
    # Vérification du type du prix
    if type(price) not in (int, float):
        return "The price should be a number"
    
    # Vérification du type de la réduction
    if type(discount) not in (int, float):
        return "The discount should be a number"
    
    # Vérification que le prix est supérieur à 0
    if price <= 0:
        return "The price should be greater than 0"
    
    # Vérification que la réduction est comprise entre 0 et 100
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100"
    
    # Calcul du prix final : prix - (prix * réduction / 100)
    return price - (price * discount / 100)


# ============================================
# EXEMPLES DE TEST (décommentez pour tester)
# ============================================
# print(apply_discount(100, 20))    # 80.0
# print(apply_discount(200, 50))    # 100.0
# print(apply_discount(50, 0))      # 50.0
# print(apply_discount(50, 100))    # 0.0
# print(apply_discount(74.5, 20.0)) # 59.6
# print(apply_discount("100", 20))  # "The price should be a number"
# print(apply_discount(100, "20"))  # "The discount should be a number"
# print(apply_discount(-50, 20))    # "The price should be greater than 0"
# print(apply_discount(100, -10))   # "The discount should be between 0 and 100"
# print(apply_discount(100, 150))   # "The discount should be between 0 and 100"