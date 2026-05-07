# ============================================
# TRAVEL WEATHER PLANNER
# ============================================
# Ce programme détermine s'il est possible de se déplacer
# en fonction de la distance, de la météo et des moyens de transport disponibles
# ============================================

# ---------------------------
# 1. DÉCLARATION DES VARIABLES
# ---------------------------
# distance_mi : nombre représentant la distance à parcourir en miles
distance_mi = 5  # Exemple : 5 miles

# is_raining : booléen indiquant s'il pleut actuellement
is_raining = False  # Exemple : il ne pleut pas

# has_bike : booléen indiquant si l'utilisateur possède un vélo
has_bike = True  # Exemple : l'utilisateur a un vélo

# has_car : booléen indiquant si l'utilisateur possède une voiture
has_car = False  # Exemple : l'utilisateur n'a pas de voiture

# has_ride_share_app : booléen indiquant si l'utilisateur a une app de VTC
has_ride_share_app = False  # Exemple : pas d'application de VTC

# ------------------------------------------
# 2. LOGIQUE CONDITIONNELLE - PAR ORDRE CROISSANT
# ------------------------------------------

# Vérification si la distance est une valeur "falsy" (0, None, chaîne vide, etc.)
if not distance_mi:
    # Si la distance est nulle ou invalide, le déplacement est impossible
    print(False)

# Cas 1 : Distance inférieure ou égale à 1 mile
elif distance_mi <= 1:
    # Pour les très courtes distances, seul le temps importe
    # True seulement s'il ne pleut pas (marche possible)
    if not is_raining:
        print(True)  # Déplacement possible
    else:
        print(False)  # Trop de pluie pour marcher

# Cas 2 : Distance comprise entre 1 mile (exclu) et 6 miles (inclus)
elif distance_mi <= 6:
    # Pour les distances moyennes, on peut utiliser le vélo
    # True seulement si : possède un vélo ET qu'il ne pleut pas
    if has_bike and not is_raining:
        print(True)  # Déplacement possible à vélo
    else:
        print(False)  # Pas de vélo ou mauvaise météo

# Cas 3 : Distance supérieure à 6 miles
else:  # distance_mi > 6 miles
    # Pour les longues distances, on a besoin d'un véhicule motorisé
    # True si : possède une voiture OU a une application de VTC
    if has_car or has_ride_share_app:
        print(True)  # Déplacement possible en voiture ou VTC
    else:
        print(False)  # Pas de moyen de transport adapté

# ============================================
# RÉSUMÉ DE LA LOGIQUE :
# - ≤ 1 mile : marche (si pas de pluie)
# - 1-6 miles : vélo (si vélo ET pas de pluie)
# - > 6 miles : voiture ou VTC (si voiture OU app VTC)
# - Distance nulle ou falsy : impossible
# ============================================