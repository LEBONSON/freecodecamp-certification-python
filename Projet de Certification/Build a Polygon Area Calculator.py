# ============================================
# CONSTRUIRE UNE CALCULATRICE DE ZONE POLYGONALE
# ============================================
# 
# ÉNONCÉ :
# Dans ce projet, vous utiliserez la programmation orientée objet pour créer
# une classe Rectangle et une classe Square. La classe Square doit être une
# sous-classe de Rectangle et hériter de ses méthodes et attributs.
#
# OBJECTIF : Remplissez les user stories ci-dessous et obtenez tous les tests
# à réussir pour terminer le laboratoire.
#
# HISTOIRES D'UTILISATEURS :
#
# 1. Vous devriez créer une classe Rectangle.
#    - Initialisée avec width et height
#    - Méthodes : set_width, set_height, get_area, get_perimeter,
#                 get_diagonal, get_picture, get_amount_inside
#    - Représentation string : "Rectangle(width=5, height=10)"
#
# 2. Vous devriez créer une classe Square qui sous-classe Rectangle.
#    - Initialisée avec un seul côté (side)
#    - Méthodes : set_width, set_height, set_side
#    - Représentation string : "Square(side=9)"
#
# ============================================

class Rectangle:
    """
    Classe représentant un rectangle avec ses dimensions et méthodes.
    
    Attributs:
    width (int/float): Largeur du rectangle
    height (int/float): Hauteur du rectangle
    """
    
    # ------------------------------------------
    # 1. MÉTHODE CONSTRUCTEUR __init__
    # ------------------------------------------
    
    def __init__(self, width, height):
        """
        Constructeur de la classe Rectangle.
        
        Paramètres:
        width (int/float): Largeur du rectangle
        height (int/float): Hauteur du rectangle
        """
        self.width = width    # Largeur du rectangle
        self.height = height  # Hauteur du rectangle
    
    # ------------------------------------------
    # 2. MÉTHODES DE MODIFICATION DES DIMENSIONS
    # ------------------------------------------
    
    def set_width(self, width):
        """
        Définit la largeur du rectangle.
        
        Paramètres:
        width (int/float): Nouvelle largeur
        """
        self.width = width
    
    def set_height(self, height):
        """
        Définit la hauteur du rectangle.
        
        Paramètres:
        height (int/float): Nouvelle hauteur
        """
        self.height = height
    
    # ------------------------------------------
    # 3. MÉTHODES DE CALCUL GÉOMÉTRIQUE
    # ------------------------------------------
    
    def get_area(self):
        """
        Calcule l'aire du rectangle.
        
        Formule: largeur × hauteur
        
        Retourne:
        int/float: Aire du rectangle
        """
        return self.width * self.height
    
    def get_perimeter(self):
        """
        Calcule le périmètre du rectangle.
        
        Formule: 2 × (largeur + hauteur)
        
        Retourne:
        int/float: Périmètre du rectangle
        """
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        """
        Calcule la diagonale du rectangle (théorème de Pythagore).
        
        Formule: √(largeur² + hauteur²)
        
        Retourne:
        float: Longueur de la diagonale
        """
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    # ------------------------------------------
    # 4. MÉTHODE get_picture
    # ------------------------------------------
    
    def get_picture(self):
        """
        Génère une représentation graphique du rectangle avec des *.
        
        Règles:
        - Si largeur > 50 ou hauteur > 50 → "Too big for picture."
        - Sinon, retourne une chaîne avec height lignes de width * chacun
        - Chaque ligne se termine par un retour à la ligne (\n)
        
        Retourne:
        str: Représentation graphique ou message d'erreur
        """
        # Vérifier les limites (dimensions > 50 interdites)
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        # Construire l'image ligne par ligne
        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture
    
    # ------------------------------------------
    # 5. MÉTHODE get_amount_inside
    # ------------------------------------------
    
    def get_amount_inside(self, shape):
        """
        Calcule combien de fois une forme peut entrer dans ce rectangle.
        
        Paramètres:
        shape (Rectangle/Square): La forme à insérer
        
        Retourne:
        int: Nombre de fois que la forme peut tenir sans rotation
        
        Principe:
        - Compter combien de largeurs de shape tiennent dans self.width
        - Compter combien de hauteurs de shape tiennent dans self.height
        - Multiplier les deux nombres
        """
        # Nombre de fois que la largeur de shape tient dans celle du rectangle
        width_fit = self.width // shape.width
        
        # Nombre de fois que la hauteur de shape tient dans celle du rectangle
        height_fit = self.height // shape.height
        
        # Retourner le nombre total de formes pouvant tenir
        return width_fit * height_fit
    
    # ------------------------------------------
    # 6. MÉTHODE __str__
    # ------------------------------------------
    
    def __str__(self):
        """
        Représentation string du rectangle.
        
        Retourne:
        str: Format "Rectangle(width=X, height=Y)"
        """
        return f"Rectangle(width={self.width}, height={self.height})"


# ============================================
# CLASSE SQUARE (SOUS-CLASSE DE RECTANGLE)
# ============================================

class Square(Rectangle):
    """
    Classe représentant un carré (sous-classe de Rectangle).
    
    Un carré a une largeur égale à sa hauteur.
    
    Attributs:
    side (int/float): Longueur du côté du carré
    """
    
    # ------------------------------------------
    # 1. MÉTHODE CONSTRUCTEUR __init__
    # ------------------------------------------
    
    def __init__(self, side):
        """
        Constructeur de la classe Square.
        
        Paramètres:
        side (int/float): Longueur du côté du carré
        
        Note: Appelle le constructeur de Rectangle avec side pour largeur et hauteur
        """
        # Appeler le constructeur de la classe parent (Rectangle)
        # Un carré a la même largeur et hauteur
        super().__init__(side, side)
    
    # ------------------------------------------
    # 2. MÉTHODES SURCHARGEES
    # ------------------------------------------
    
    def set_width(self, width):
        """
        Définit la largeur du carré (et la hauteur automatiquement).
        
        Paramètres:
        width (int/float): Nouvelle largeur (deviendra aussi la hauteur)
        
        Note: Surcharge de la méthode de Rectangle pour maintenir la forme carrée
        """
        self.width = width   # Définir la largeur
        self.height = width  # La hauteur devient identique à la largeur
    
    def set_height(self, height):
        """
        Définit la hauteur du carré (et la largeur automatiquement).
        
        Paramètres:
        height (int/float): Nouvelle hauteur (deviendra aussi la largeur)
        
        Note: Surcharge de la méthode de Rectangle pour maintenir la forme carrée
        """
        self.width = height  # La largeur devient identique à la hauteur
        self.height = height # Définir la hauteur
    
    # ------------------------------------------
    # 3. MÉTHODE SPÉCIFIQUE À SQUARE
    # ------------------------------------------
    
    def set_side(self, side):
        """
        Définit la longueur du côté du carré.
        
        Paramètres:
        side (int/float): Longueur du côté
        
        Note: Cette méthode est spécifique aux carrés
        """
        self.width = side   # Largeur = côté
        self.height = side  # Hauteur = côté
    
    # ------------------------------------------
    # 4. MÉTHODE __str__
    # ------------------------------------------
    
    def __str__(self):
        """
        Représentation string du carré.
        
        Retourne:
        str: Format "Square(side=X)"
        """
        return f"Square(side={self.width})"


# ============================================
# EXEMPLES D'UTILISATION
# ============================================

# Exemple 1 : Utilisation de Rectangle
print("--- EXEMPLE RECTANGLE ---")
rect = Rectangle(10, 5)
print(f"Aire: {rect.get_area()}")           # 50
rect.set_height(3)
print(f"Périmètre: {rect.get_perimeter()}")  # 26
print(f"Représentation: {rect}")             # Rectangle(width=10, height=3)
print(rect.get_picture())
# Sortie:
# **********
# **********
# **********

# Exemple 2 : Utilisation de Square
print("\n--- EXEMPLE CARRÉ ---")
sq = Square(9)
print(f"Aire: {sq.get_area()}")              # 81
sq.set_side(4)
print(f"Diagonale: {sq.get_diagonal()}")     # 5.656854249492381
print(f"Représentation: {sq}")               # Square(side=4)
print(sq.get_picture())
# Sortie:
# ****
# ****
# ****
# ****

# Exemple 3 : Combien de formes peuvent tenir
print("\n--- EXEMPLE get_amount_inside ---")
rect.set_height(8)
rect.set_width(16)
print(f"Nombre de carrés (côté 4) dans rectangle 16x8: {rect.get_amount_inside(sq)}")  # 8


# ============================================
# TESTS DE VALIDATION SUPPLÉMENTAIRES
# ============================================

print("\n--- TESTS SUPPLÉMENTAIRES ---")

# Test 1 : Vérification de l'héritage
sq2 = Square(5)
print(f"sq2 est-il une instance de Square? {isinstance(sq2, Square)}")      # True
print(f"sq2 est-il une instance de Rectangle? {isinstance(sq2, Rectangle)}") # True

# Test 2 : Modification par set_width sur un carré
sq2.set_width(7)
print(f"Après set_width(7) sur carré: {sq2}")  # Square(side=7)

# Test 3 : Modification par set_height sur un carré
sq2.set_height(3)
print(f"Après set_height(3) sur carré: {sq2}")  # Square(side=3)

# Test 4 : Test des limites pour get_picture
big_rect = Rectangle(100, 10)
print(f"Grand rectangle: {big_rect.get_picture()}")  # Too big for picture.

big_square = Square(60)
print(f"Grand carré: {big_square.get_picture()}")    # Too big for picture.

# Test 5 : Calculs géométriques
rect2 = Rectangle(3, 6)
print(f"Rectangle 3x6 - Aire: {rect2.get_area()}")        # 18
print(f"Rectangle 3x6 - Périmètre: {rect2.get_perimeter()}")  # 18
print(f"Rectangle 3x6 - Diagonale: {rect2.get_diagonal()}")   # 6.708203932499369

sq3 = Square(5)
print(f"Carré 5x5 - Aire: {sq3.get_area()}")             # 25
print(f"Carré 5x5 - Périmètre: {sq3.get_perimeter()}")   # 20
print(f"Carré 5x5 - Diagonale: {sq3.get_diagonal()}")    # 7.0710678118654755

# Test 6 : get_amount_inside avec différents cas
rect3 = Rectangle(15, 10)
sq4 = Square(5)
print(f"Rectangle 15x10 contient combien de carrés 5x5? {rect3.get_amount_inside(sq4)}")  # 6

rect4 = Rectangle(4, 8)
rect5 = Rectangle(3, 6)
print(f"Rectangle 4x8 contient rectangle 3x6? {rect4.get_amount_inside(rect5)}")  # 1

rect6 = Rectangle(2, 3)
rect7 = Rectangle(3, 6)
print(f"Rectangle 2x3 contient rectangle 3x6? {rect6.get_amount_inside(rect7)}")  # 0

# Test 7 : Vérification que set_side fonctionne correctement
sq5 = Square(10)
print(f"Avant set_side(6): {sq5}")   # Square(side=10)
sq5.set_side(6)
print(f"Après set_side(6): {sq5}")   # Square(side=6)
print(f"Aire après changement: {sq5.get_area()}")  # 36

# Test 8 : Chaînage des méthodes (héritage)
sq6 = Square(8)
print(f"get_diagonal hérité: {sq6.get_diagonal()}")  # 11.313708498984761
print(f"get_perimeter hérité: {sq6.get_perimeter()}")  # 32


# ============================================
# RÉSUMÉ DE LA LOGIQUE :
# 
# RECTANGLE :
# - Attributs : width, height
# - set_width, set_height : modifient les dimensions
# - get_area, get_perimeter, get_diagonal : calculs géométriques
# - get_picture : affichage graphique avec *
# - get_amount_inside : calcul de combien de formes tiennent
# - __str__ : affichage formaté
#
# SQUARE (sous-classe de Rectangle) :
# - Hérite de toutes les méthodes de Rectangle
# - Constructeur avec un seul paramètre (side)
# - set_width, set_height surchargées pour maintenir côté égal
# - set_side : méthode spécifique pour définir le côté
# - __str__ : affichage spécifique "Square(side=X)"
# - Les méthodes get_area, get_perimeter, etc. fonctionnent automatiquement
# ============================================