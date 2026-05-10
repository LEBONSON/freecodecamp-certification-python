# ============================================
# PIN EXTRACTOR - EXTRACTEUR DE CODES SECRETS
# ============================================
# 
# ÉNONCÉ :
# Dans cet atelier, vous allez créer un extracteur de codes secrets à partir
# de poèmes. Chaque poème contient un code caché basé sur la longueur des mots
# à des positions spécifiques.
#
# OBJECTIF :
# Extraire un code secret de chaque poème en suivant une règle spécifique :
# Pour chaque ligne du poème (indexée à partir de 0), prenez le mot à la position
# correspondant à l'index de la ligne. Ajoutez la longueur de ce mot au code.
# Si la ligne n'a pas assez de mots, ajoutez '0'.
#
# RÈGLE D'EXTRACTION :
# - Pour la ligne 0 → prendre le mot à l'index 0 (premier mot)
# - Pour la ligne 1 → prendre le mot à l'index 1 (deuxième mot)
# - Pour la ligne 2 → prendre le mot à l'index 2 (troisième mot)
# - etc.
# - Ajouter la longueur de ce mot au code secret
# - Si la ligne a moins de mots que l'index, ajouter '0'
#
# EXEMPLE :
# Poème :
# "Stars and the moon"     (ligne 0) → mot[0]='Stars' → longueur=5
# "shine in the sky"       (ligne 1) → mot[1]='in'    → longueur=2
# "white and"              (ligne 2) → pas de mot[2]  → '0'
# "until the end"          (ligne 3) → pas de mot[3]  → '0'
# Code secret obtenu : "5200"
#
# ============================================

def pin_extractor(poems):
    """
    Extrait un code secret de chaque poème dans une liste.
    
    Paramètres:
    poems (list): Liste de chaînes de caractères, chaque chaîne est un poème
                  contenant des lignes séparées par des retours à la ligne (\n)
    
    Retourne:
    list: Liste de chaînes de caractères, chaque chaîne est le code secret
          extrait du poème correspondant
    
    Algorithme:
    1. Pour chaque poème dans la liste :
       a. Initialiser un code secret vide
       b. Diviser le poème en lignes (en utilisant '\n')
       c. Pour chaque ligne avec son index (0, 1, 2, ...) :
          - Diviser la ligne en mots (en utilisant les espaces)
          - Si le nombre de mots est supérieur à l'index de ligne :
            - Prendre le mot à la position index
            - Compter sa longueur
            - Ajouter cette longueur (convertie en chaîne) au code
          - Sinon (pas assez de mots) :
            - Ajouter '0' au code
       d. Ajouter le code à la liste des résultats
    
    3. Retourner la liste des codes secrets
    """
    
    # Liste pour stocker les codes secrets de chaque poème
    secret_codes = []
    
    # Parcourir chaque poème dans la liste d'entrée
    for poem in poems:
        # Code secret pour ce poème (initialement vide)
        secret_code = ''
        
        # Diviser le poème en lignes séparées par le caractère newline
        lines = poem.split('\n')
        
        # Parcourir chaque ligne avec son index (enumerate donne index, ligne)
        for line_index, line in enumerate(lines):
            # Diviser la ligne en mots (séparés par des espaces)
            words = line.split()
            
            # Vérifier si la ligne a assez de mots
            # Si le nombre de mots est supérieur à l'index de la ligne
            if len(words) > line_index:
                # Prendre le mot à la position line_index
                # Compter sa longueur (nombre de caractères)
                # Convertir en chaîne et ajouter au code secret
                secret_code += str(len(words[line_index]))
            else:
                # Pas assez de mots : ajouter '0'
                secret_code += '0'
        
        # Ajouter le code de ce poème à la liste des résultats
        secret_codes.append(secret_code)
    
    # Retourner tous les codes secrets extraits
    return secret_codes


# ============================================
# POÈMES DE TEST
# ============================================

# Poème 1 : Un poème classique sur les étoiles
poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

# Poème 2 : Un poème sur la nature
poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'

# Poème 3 : Un court poème sur un dragon
poem3 = 'There\nonce\nwas\na\ndragon'


# ============================================
# EXÉCUTION DE LA FONCTION
# ============================================

# Appeler pin_extractor avec une liste contenant les trois poèmes
# et afficher les codes secrets extraits
print(pin_extractor([poem, poem2, poem3]))


# ============================================
# ANALYSE DÉTAILLÉE DES RÉSULTATS
# ============================================

# Résultat attendu : ['5200', '3345', '50000']
#
# Analyse du poème 1 :
# Ligne 0: "Stars and the moon"     → mots = ['Stars','and','the','moon']
#          → mot à l'index 0 = 'Stars' → longueur = 5
# Ligne 1: "shine in the sky"       → mots = ['shine','in','the','sky']
#          → mot à l'index 1 = 'in' → longueur = 2
# Ligne 2: "white and"              → mots = ['white','and']
#          → pas de mot à l'index 2 → '0'
# Ligne 3: "until the end of the night" → mots = ['until','the','end','of','the','night']
#          → pas de mot à l'index 3 → '0'
# Code : "5" + "2" + "0" + "0" = "5200"
#
# Analyse du poème 2 :
# Ligne 0: "The grass is green"     → mots = ['The','grass','is','green']
#          → mot à l'index 0 = 'The' → longueur = 3
# Ligne 1: "here and there"         → mots = ['here','and','there']
#          → mot à l'index 1 = 'and' → longueur = 3
# Ligne 2: "hoping for rain"        → mots = ['hoping','for','rain']
#          → mot à l'index 2 = 'rain' → longueur = 4
# Ligne 3: "before it turns yellow" → mots = ['before','it','turns','yellow']
#          → mot à l'index 3 = 'turns' → longueur = 5
# Code : "3" + "3" + "4" + "5" = "3345"
#
# Analyse du poème 3 :
# Ligne 0: "There"  → mots = ['There'] → mot à l'index 0 = 'There' → longueur = 5
# Ligne 1: "once"   → mots = ['once'] → pas de mot à l'index 1 → '0'
# Ligne 2: "was"    → mots = ['was']  → pas de mot à l'index 2 → '0'
# Ligne 3: "a"      → mots = ['a']    → pas de mot à l'index 3 → '0'
# Ligne 4: "dragon" → mots = ['dragon'] → pas de mot à l'index 4 → '0'
# Code : "5" + "0" + "0" + "0" + "0" = "50000"


# ============================================
# RÉSUMÉ DE LA FONCTION PIN_EXTRACTOR
# ============================================
#
# pin_extractor(poems) :
# │
# ├─ Entrée : liste de poèmes (chaînes de caractères)
# │
# ├─ Pour chaque poème :
# │  │
# │  ├─ Diviser en lignes (split('\n'))
# │  │
# │  ├─ Pour chaque ligne avec son index (enumerate) :
# │  │  │
# │  │  ├─ Diviser la ligne en mots (split())
# │  │  │
# │  │  ├─ Si nombre de mots > index :
# │  │  │  └─ Ajouter la longueur du mot à l'index
# │  │  │
# │  │  └─ Sinon :
# │  │     └─ Ajouter '0'
# │  │
# │  └─ Ajouter le code à la liste des résultats
# │
# └─ Retourner la liste des codes
#
# ============================================