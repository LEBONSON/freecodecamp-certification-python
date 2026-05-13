# ============================================
# BUILD A MEDICAL DATA VALIDATOR
# ============================================
# 
# ÉNONCÉ :
# Dans cet atelier, vous allez créer un validateur de données médicales.
# Le système vérifie l'intégrité et le format des dossiers patients
# stockés dans une liste de dictionnaires.
#
# OBJECTIF : Créer les fonctions suivantes :
#
# 1. find_invalid_records : Vérifie chaque champ d'un dossier patient
# 2. validate : Valide l'ensemble des dossiers médicaux
#
# RÈGLES DE VALIDATION :
# - patient_id : chaîne commençant par 'p' suivie de chiffres (ex: 'P1001')
# - age : entier ≥ 18
# - gender : 'male' ou 'female' (insensible à la casse)
# - diagnosis : chaîne de caractères ou None
# - medications : liste de chaînes de caractères
# - last_visit_id : chaîne commençant par 'v' suivie de chiffres (ex: 'V2301')
#
# ============================================

import re

# ============================================
# DONNÉES DE TEST
# ============================================

medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]


# ============================================
# FONCTION find_invalid_records
# ============================================

def find_invalid_records(
    patient_id, age, gender, diagnosis, medications, last_visit_id
):
    """
    Vérifie chaque champ d'un dossier patient selon les règles de validation.
    
    Paramètres:
    patient_id (str): Identifiant du patient
    age (int): Âge du patient
    gender (str): Genre du patient
    diagnosis (str): Diagnostic médical
    medications (list): Liste des médicaments
    last_visit_id (str): Identifiant de la dernière visite
    
    Retourne:
    list: Liste des clés invalides
    
    Règles de validation:
    - patient_id: chaîne commençant par 'p' suivie de chiffres (p\d+)
    - age: entier >= 18
    - gender: 'male' ou 'female' (insensible à la casse)
    - diagnosis: chaîne de caractères ou None
    - medications: liste de chaînes de caractères
    - last_visit_id: chaîne commençant par 'v' suivie de chiffres (v\d+)
    """
    
    # Dictionnaire des contraintes de validation
    constraints = {
        # patient_id : doit être une chaîne correspondant au pattern 'p' + chiffres
        'patient_id': isinstance(patient_id, str)
        and re.fullmatch('p\d+', patient_id, re.IGNORECASE),
        
        # age : doit être un entier >= 18 (patient adulte)
        'age': isinstance(age, int) and age >= 18,
        
        # gender : doit être 'male' ou 'female' (insensible à la casse)
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),
        
        # diagnosis : doit être une chaîne ou None (diagnostic optionnel)
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
        
        # medications : doit être une liste de chaînes de caractères
        'medications': isinstance(medications, list)
        and all([isinstance(i, str) for i in medications]),
        
        # last_visit_id : doit être une chaîne correspondant au pattern 'v' + chiffres
        'last_visit_id': isinstance(last_visit_id, str)
        and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE)
    }
    
    # Retourner la liste des clés dont la validation a échoué
    return [key for key, value in constraints.items() if not value]


# ============================================
# FONCTION validate
# ============================================

def validate(data):
    """
    Valide l'ensemble des dossiers médicaux.
    
    Paramètres:
    data (list/tuple): Liste ou tuple contenant les dictionnaires de dossiers
    
    Retourne:
    bool: True si tous les dossiers sont valides, False sinon
    
    Étapes de validation:
    1. Vérifier que data est une liste ou un tuple
    2. Vérifier que chaque élément est un dictionnaire
    3. Vérifier que chaque dictionnaire contient toutes les clés requises
    4. Vérifier les valeurs de chaque champ avec find_invalid_records
    5. Afficher les erreurs et retourner False si des erreurs sont trouvées
    """
    
    # ==========================================
    # ÉTAPE 1 : Vérification du type de la structure de données
    # ==========================================
    
    # Vérifier si data est une séquence (liste ou tuple)
    is_sequence = isinstance(data, (list, tuple))
    
    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False
    
    # ==========================================
    # ÉTAPE 2 : Initialisation des variables
    # ==========================================
    
    # Drapeau pour indiquer si des erreurs ont été trouvées
    is_invalid = False
    
    # Ensemble des clés requises dans chaque dictionnaire
    key_set = set(
        ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
    )
    
    # ==========================================
    # ÉTAPE 3 : Parcours de chaque enregistrement
    # ==========================================
    
    # Parcourir chaque dictionnaire avec son index
    for index, dictionary in enumerate(data):
        
        # --- Vérification 1 : Chaque élément doit être un dictionnaire ---
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True
            continue  # Passer à l'élément suivant
        
        # --- Vérification 2 : Les clés du dictionnaire doivent correspondre ---
        if set(dictionary.keys()) != key_set:
            print(
                f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
            )
            is_invalid = True
            continue  # Passer à l'élément suivant
        
        # --- Vérification 3 : Valider les valeurs de chaque champ ---
        # Appeler find_invalid_records avec les valeurs du dictionnaire
        invalid_records = find_invalid_records(**dictionary)
        
        # Parcourir chaque clé invalide pour afficher l'erreur
        for key in invalid_records:
            print(f"Unexpected format '{key}: {dictionary[key]}' at position {index}.")
            is_invalid = True
    
    # ==========================================
    # ÉTAPE 4 : Résultat final
    # ==========================================
    
    # Si des erreurs ont été trouvées, retourner False
    if is_invalid:
        return False
    
    # Sinon, tout est valide
    print('Valid format.')
    return True


# ============================================
# EXÉCUTION DU VALIDATEUR
# ============================================

# Appeler la fonction validate avec les dossiers médicaux de test
validate(medical_records)


# ============================================
# TESTS SUPPLÉMENTAIRES
# ============================================

print("\n" + "="*50)
print("TESTS SUPPLÉMENTAIRES")
print("="*50)

# Test 1 : Données valides
print("\n--- Test 1: Données valides ---")
valid_data = [
    {
        'patient_id': 'p1001',
        'age': 25,
        'gender': 'male',
        'diagnosis': 'Cold',
        'medications': ['Paracetamol'],
        'last_visit_id': 'v1001'
    }
]
validate(valid_data)

# Test 2 : Format invalide (tuple au lieu de liste)
print("\n--- Test 2: Format invalide (tuple) ---")
invalid_format = (
    {
        'patient_id': 'p1001',
        'age': 25,
        'gender': 'male',
        'diagnosis': 'Cold',
        'medications': ['Paracetamol'],
        'last_visit_id': 'v1001'
    }
)
validate(invalid_format)  # tuple fonctionne aussi (c'est une séquence)

# Test 3 : Données avec patient_id invalide
print("\n--- Test 3: patient_id invalide ---")
invalid_patient_id = [
    {
        'patient_id': 'PATIENT1001',  # Ne commence pas par 'p'
        'age': 25,
        'gender': 'male',
        'diagnosis': 'Cold',
        'medications': ['Paracetamol'],
        'last_visit_id': 'v1001'
    }
]
validate(invalid_patient_id)

# Test 4 : Âge invalide (mineur)
print("\n--- Test 4: Âge invalide (< 18) ---")
invalid_age = [
    {
        'patient_id': 'p1001',
        'age': 15,  # < 18
        'gender': 'male',
        'diagnosis': 'Cold',
        'medications': ['Paracetamol'],
        'last_visit_id': 'v1001'
    }
]
validate(invalid_age)

# Test 5 : Genre invalide
print("\n--- Test 5: Genre invalide ---")
invalid_gender = [
    {
        'patient_id': 'p1001',
        'age': 25,
        'gender': 'other',  # Ni 'male' ni 'female'
        'diagnosis': 'Cold',
        'medications': ['Paracetamol'],
        'last_visit_id': 'v1001'
    }
]
validate(invalid_gender)

# Test 6 : Médicaments invalides (liste de non-chaînes)
print("\n--- Test 6: Médicaments invalides ---")
invalid_medications = [
    {
        'patient_id': 'p1001',
        'age': 25,
        'gender': 'male',
        'diagnosis': 'Cold',
        'medications': [123, 456],  # Nombres au lieu de chaînes
        'last_visit_id': 'v1001'
    }
]
validate(invalid_medications)

# Test 7 : last_visit_id invalide
print("\n--- Test 7: last_visit_id invalide ---")
invalid_visit = [
    {
        'patient_id': 'p1001',
        'age': 25,
        'gender': 'male',
        'diagnosis': 'Cold',
        'medications': ['Paracetamol'],
        'last_visit_id': 'VISIT1001'  # Ne commence pas par 'v'
    }
]
validate(invalid_visit)

# Test 8 : Dossier avec clé manquante
print("\n--- Test 8: Clé manquante ---")
missing_key = [
    {
        'patient_id': 'p1001',
        'age': 25,
        'gender': 'male',
        'diagnosis': 'Cold',
        'medications': ['Paracetamol']
        # last_visit_id est manquant
    }
]
validate(missing_key)

# Test 9 : Dossier avec clé supplémentaire
print("\n--- Test 9: Clé supplémentaire ---")
extra_key = [
    {
        'patient_id': 'p1001',
        'age': 25,
        'gender': 'male',
        'diagnosis': 'Cold',
        'medications': ['Paracetamol'],
        'last_visit_id': 'v1001',
        'extra_field': 'not allowed'  # Clé non autorisée
    }
]
validate(extra_key)

# Test 10 : Données avec plusieurs erreurs
print("\n--- Test 10: Multiples erreurs ---")
multiple_errors = [
    {
        'patient_id': 'INVALID',
        'age': 15,
        'gender': 'unknown',
        'diagnosis': 'Cold',
        'medications': ['Paracetamol', 123],
        'last_visit_id': 'INVALID'
    }
]
validate(multiple_errors)

# Test 11 : Médicaments vides (liste vide est valide)
print("\n--- Test 11: Médicaments vides ---")
empty_meds = [
    {
        'patient_id': 'p1001',
        'age': 25,
        'gender': 'male',
        'diagnosis': 'Cold',
        'medications': [],  # Liste vide = valide
        'last_visit_id': 'v1001'
    }
]
validate(empty_meds)

# Test 12 : Diagnosis None (valide)
print("\n--- Test 12: Diagnosis None ---")
none_diagnosis = [
    {
        'patient_id': 'p1001',
        'age': 25,
        'gender': 'male',
        'diagnosis': None,  # None est autorisé
        'medications': ['Paracetamol'],
        'last_visit_id': 'v1001'
    }
]
validate(none_diagnosis)


# ============================================
# EXPLICATION DÉTAILLÉE
# ============================================

print("\n" + "="*50)
print("EXPLICATION DÉTAILLÉE")
print("="*50)

print("""
1. find_invalid_records(data):
   ----------------------------
   - Reçoit 6 paramètres correspondant aux champs d'un dossier
   - Crée un dictionnaire 'constraints' avec 6 conditions
   - Chaque condition combine isinstance() et une règle spécifique
   - Retourne une liste des clés dont la condition est False

2. validate(data):
   --------------
   - Vérifie que data est une liste ou un tuple
   - Initialise is_invalid = False
   - Définit l'ensemble des clés requises
   
   Pour chaque dictionnaire dans data:
   - Vérifie que c'est un dict
   - Vérifie que les clés correspondent exactement
   - Appelle find_invalid_records(**dictionary)
   - Pour chaque clé invalide, affiche l'erreur
   
   - Si is_invalid est True, retourne False
   - Sinon, affiche 'Valid format.' et retourne True

3. Expressions régulières utilisées:
   ---------------------------------
   - 'p\d+' : p suivi d'un ou plusieurs chiffres
   - 'v\d+' : v suivi d'un ou plusieurs chiffres
   - re.IGNORECASE : ignore la casse (P ou p, V ou v)
   - re.fullmatch() : vérifie que toute la chaîne correspond

4. Types de validations:
   ---------------------
   - patient_id: str + pattern regex
   - age: int + >= 18
   - gender: str + valeur dans ('male', 'female')
   - diagnosis: str ou None
   - medications: list + tous les éléments sont str
   - last_visit_id: str + pattern regex
""")


# ============================================
# RÉSUMÉ DE L'ATELIER
# ============================================
#
# 1. find_invalid_records :
#    - Valide chaque champ individuellement
#    - Retourne la liste des champs invalides
#    - Utilise isinstance() et re.fullmatch()
#
# 2. validate :
#    - Valide la structure globale des données
#    - Vérifie le format (liste/tuple)
#    - Vérifie le type de chaque élément (dict)
#    - Vérifie la présence de toutes les clés
#    - Affiche les erreurs spécifiques
#    - Retourne un booléen et imprime un message
#
# 3. Cas de validation :
#    - patient_id : pattern 'p' + chiffres (ex: 'P1001')
#    - age : entier >= 18
#    - gender : 'male' ou 'female'
#    - diagnosis : str ou None
#    - medications : liste de str
#    - last_visit_id : pattern 'v' + chiffres (ex: 'V2301')
#
# ============================================
