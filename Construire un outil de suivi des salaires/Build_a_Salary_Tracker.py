# ============================================
# BUILD AN EMPLOYEE CLASS
# ============================================
# 
# ÉNONCÉ :
# Dans ce laboratoire, vous allez créer une classe Employee qui gère
# les employés avec leurs noms, niveaux et salaires.
#
# OBJECTIF : Répondre aux critères utilisateur ci-dessous pour compléter le laboratoire.
#
# CRITÈRES UTILISATEUR (reconstitués d'après le code) :
# - Vous devez avoir une classe nommée Employee.
# - La classe doit avoir un dictionnaire de classe _base_salaries contenant
#   les salaires de base pour chaque niveau : 'trainee', 'junior', 'mid-level', 'senior'
# - La méthode __init__ doit prendre name et level comme paramètres
# - La méthode __str__ doit retourner le format '{name}: {level}'
# - La méthode __repr__ doit retourner le format Employee('{name}', '{level}')
# - La propriété name doit :
#   • être une chaîne de caractères (sinon TypeError)
#   • afficher "'name' updated to '{self.name}'." lors de la modification
# - La propriété level doit :
#   • être une chaîne de caractères (sinon TypeError)
#   • être une valeur valide dans _base_salaries (sinon ValueError)
#   • ne pas être identique au niveau actuel (sinon ValueError)
#   • ne pas permettre un changement vers un niveau inférieur (sinon ValueError)
#   • afficher "'{self.name}' promoted to '{new_level}'." lors de la modification
#   • mettre à jour le salaire avec la valeur de base du nouveau niveau
# - La propriété salary doit :
#   • être un nombre (int ou float) (sinon TypeError)
#   • être supérieure ou égale au salaire minimum du niveau (sinon ValueError)
#   • afficher f'Salary updated to ${self.salary}.' lors de la modification
#
# ============================================

class Employee:
    """
    Classe représentant un employé avec son nom, son niveau et son salaire.
    
    Attributs de classe:
    _base_salaries (dict): Dictionnaire des salaires de base par niveau
    
    Attributs d'instance:
    _name (str): Nom de l'employé (privé)
    _level (str): Niveau de l'employé (privé)
    _salary (int/float): Salaire de l'employé (privé)
    """
    
    # ------------------------------------------
    # 1. ATTRIBUTS DE CLASSE
    # ------------------------------------------
    # Dictionnaire des salaires de base pour chaque niveau
    _base_salaries = {
        'trainee': 1000,    # Stagiaire : 1000€
        'junior': 2000,     # Junior : 2000€
        'mid-level': 3000,  # Intermédiaire : 3000€
        'senior': 4000,     # Senior : 4000€
    }

    # ------------------------------------------
    # 2. MÉTHODES MAGIQUES (__init__, __str__, __repr__)
    # ------------------------------------------
    
    def __init__(self, name, level):
        """
        Constructeur de la classe Employee.
        
        Paramètres:
        name (str): Nom de l'employé
        level (str): Niveau de l'employé (trainee, junior, mid-level, senior)
        """
        # Initialisation directe des attributs privés pour éviter
        # les déclenchements multiples des setters
        self._name = name
        self._level = level
        # Le salaire est initialisé avec la valeur de base du niveau
        self._salary = Employee._base_salaries[level]

    def __str__(self):
        """
        Représentation string de l'employé pour l'utilisateur.
        
        Retourne:
        str: Format '{name}: {level}'
        """
        return f'{self.name}: {self.level}'

    def __repr__(self):
        """
        Représentation string de l'employé pour le développeur.
        
        Retourne:
        str: Format "Employee('{name}', '{level}')"
        """
        return f"Employee('{self.name}', '{self.level}')"

    # ------------------------------------------
    # 3. PROPRIÉTÉ name (GETTER + SETTER)
    # ------------------------------------------
    
    @property
    def name(self):
        """
        Getter pour l'attribut name.
        
        Retourne:
        str: Le nom de l'employé
        """
        return self._name

    @name.setter
    def name(self, new_name):
        """
        Setter pour l'attribut name avec validation.
        
        Paramètres:
        new_name (str): Nouveau nom de l'employé
        
        Lève:
        TypeError: Si new_name n'est pas une chaîne de caractères
        """
        # Validation : le nom doit être une chaîne de caractères
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")
        
        # Mise à jour du nom
        self._name = new_name
        
        # Message de confirmation
        print(f"'name' updated to '{self.name}'.")

    # ------------------------------------------
    # 4. PROPRIÉTÉ level (GETTER + SETTER)
    # ------------------------------------------
    
    @property
    def level(self):
        """
        Getter pour l'attribut level.
        
        Retourne:
        str: Le niveau de l'employé
        """
        return self._level

    @level.setter
    def level(self, new_level):
        """
        Setter pour l'attribut level avec validations multiples.
        
        Paramètres:
        new_level (str): Nouveau niveau de l'employé
        
        Lève:
        TypeError: Si new_level n'est pas une chaîne de caractères
        ValueError: Si new_level n'existe pas dans _base_salaries
        ValueError: Si new_level est identique au niveau actuel
        ValueError: Si le nouveau niveau est inférieur au niveau actuel
        """
        # Validation 1 : le niveau doit être une chaîne de caractères
        if not isinstance(new_level, str):
            raise TypeError("'level' must be a string.")
        
        # Validation 2 : le niveau doit exister dans le dictionnaire
        if new_level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")
        
        # Validation 3 : on ne peut pas passer au même niveau
        if hasattr(self, '_level') and new_level == self.level:
            raise ValueError(f"'{self.level}' is already the selected level.")
        
        # Validation 4 : on ne peut pas passer à un niveau inférieur
        # (un employé ne peut pas être rétrogradé)
        if hasattr(self, '_level') and Employee._base_salaries[new_level] < Employee._base_salaries[self.level]:
            raise ValueError("Cannot change to lower level.")
        
        # Message de promotion
        print(f"'{self.name}' promoted to '{new_level}'.")
        
        # Mise à jour du salaire avec le salaire de base du nouveau niveau
        self.salary = Employee._base_salaries[new_level]
        
        # Mise à jour du niveau
        self._level = new_level

    # ------------------------------------------
    # 5. PROPRIÉTÉ salary (GETTER + SETTER)
    # ------------------------------------------
    
    @property
    def salary(self):
        """
        Getter pour l'attribut salary.
        
        Retourne:
        int/float: Le salaire de l'employé
        """
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        """
        Setter pour l'attribut salary avec validation.
        
        Paramètres:
        new_salary (int/float): Nouveau salaire de l'employé
        
        Lève:
        TypeError: Si new_salary n'est pas un nombre
        ValueError: Si le salaire est inférieur au minimum du niveau
        """
        # Validation 1 : le salaire doit être un nombre (int ou float)
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")
        
        # Validation 2 : le salaire doit être supérieur ou égal au minimum
        if hasattr(self, '_level') and new_salary < Employee._base_salaries[self.level]:
            raise ValueError(f'Salary must be higher than minimum salary ${Employee._base_salaries[self.level]}.')
        
        # Mise à jour du salaire
        self._salary = new_salary
        
        # Message de confirmation
        print(f'Salary updated to ${self.salary}.')


# ============================================
# EXEMPLES D'UTILISATION
# ============================================

# Création d'un employé stagiaire
charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)                    # Charlie Brown: trainee
print(f'Base salary: ${charlie_brown.salary}')  # Base salary: $1000

# Promotion du stagiaire au niveau junior
charlie_brown.level = 'junior'
# Sortie : 'Charlie Brown' promoted to 'junior'.
#         Salary updated to $2000.

# ============================================
# TESTS SUPPLÉMENTAIRES (décommentez pour tester)
# ============================================

# Test de changement de nom
# charlie_brown.name = "Chuck Brown"
# Sortie : 'name' updated to 'Chuck Brown'.

# Test de validation du nom (erreur)
# charlie_brown.name = 123
# Sortie : TypeError: 'name' must be a string.

# Test de niveau invalide
# charlie_brown.level = 'expert'
# Sortie : ValueError: Invalid value 'expert' for 'level' attribute.

# Test de rétrogradation (erreur)
# charlie_brown.level = 'trainee'
# Sortie : ValueError: Cannot change to lower level.

# Test de salaire trop bas (erreur)
# charlie_brown.salary = 1500
# Sortie : ValueError: Salary must be higher than minimum salary $2000.

# ============================================
# RÉSUMÉ DE LA LOGIQUE :
# 1. Classe Employee avec attributs name, level, salary
# 2. Validation complète via des propriétés (getters/setters)
# 3. Salaires de base définis par niveau
# 4. Règles métier :
#    - Pas de rétrogradation
#    - Salaire ≥ minimum du niveau
#    - Niveau doit exister dans la liste prédéfinie
# 5. Messages de confirmation pour chaque modification
# ============================================