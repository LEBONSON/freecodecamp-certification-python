# ============================================
# CRÉER UNE INTERFACE DE JOUEUR
# ============================================
# 
# ÉNONCÉ :
# Dans ce laboratoire, vous allez créer une interface de joueur en utilisant
# les classes abstraites. Le système permet de définir différents types de
# joueurs (Pion, etc.) avec leurs propres capacités de mouvement.
#
# OBJECTIF : Remplissez les user stories ci-dessous et obtenez tous les tests
# à réussir pour terminer le laboratoire.
#
# HISTOIRES D'UTILISATEURS :
#
# 1. Vous devez définir une classe abstraite nommée Player qui hérite de abc.ABC
#
# 2. La classe Player doit avoir une méthode __init__ qui définit :
#    - moves : liste vide
#    - position : (0, 0)
#    - path : liste contenant la position initiale
#
# 3. La classe Player doit avoir une méthode make_move qui :
#    - Utilise random.choice pour obtenir un mouvement aléatoire
#    - Ajoute le mouvement à la position actuelle
#    - Ajoute la nouvelle position au chemin
#    - Retourne la nouvelle position
#
# 4. La classe Player doit avoir une méthode abstraite level_up
#
# 5. Vous devez définir une classe Pawn qui hérite de Player
#
# 6. La classe Pawn doit définir ses mouvements de base :
#    - haut (0, 1), bas (0, -1), gauche (-1, 0), droite (1, 0)
#
# 7. La méthode level_up de Pawn doit ajouter les mouvements diagonaux
#
# ============================================

import abc
import random


class Player(abc.ABC):
    """
    Classe abstraite représentant un joueur générique.
    
    Attributs:
    moves (list): Liste des mouvements possibles
    position (tuple): Position actuelle (x, y)
    path (list): Historique des positions empruntées
    
    Méthodes:
    make_move(): Effectue un mouvement aléatoire
    level_up(): Méthode abstraite à implémenter (augmente les capacités)
    """
    
    def __init__(self):
        """
        Constructeur de la classe Player.
        
        Initialise:
        - moves : liste vide (sera remplie par les classes filles)
        - position : (0, 0) origine du plateau
        - path : liste contenant la position de départ
        """
        self.moves = []               # Liste des mouvements possibles
        self.position = (0, 0)        # Position actuelle (x, y)
        self.path = [self.position]   # Historique des positions
    
    def make_move(self):
        """
        Effectue un mouvement aléatoire parmi les mouvements possibles.
        
        Algorithme:
        1. Choisir un mouvement aléatoire dans self.moves
        2. Calculer la nouvelle position x, y
        3. Mettre à jour position
        4. Ajouter la nouvelle position au chemin
        5. Retourner la nouvelle position
        
        Retourne:
        tuple: Nouvelle position (x, y) après le mouvement
        """
        # 1. Choisir un mouvement aléatoire
        move = random.choice(self.moves)
        
        # 2. Calculer les nouvelles coordonnées
        new_x = self.position[0] + move[0]  # Ajouter dx à x
        new_y = self.position[1] + move[1]  # Ajouter dy à y
        new_position = (new_x, new_y)
        
        # 3. Mettre à jour la position actuelle
        self.position = new_position
        
        # 4. Ajouter au chemin
        self.path.append(self.position)
        
        # 5. Retourner la nouvelle position
        return self.position
    
    @abc.abstractmethod
    def level_up(self):
        """
        Méthode abstraite pour augmenter le niveau du joueur.
        
        Chaque classe concrète doit implémenter cette méthode pour
        ajouter de nouvelles capacités (mouvements supplémentaires).
        
        Note: Cette méthode doit être implémentée dans les classes filles
        """
        pass


class Pawn(Player):
    """
    Classe représentant un Pion (type de joueur de base).
    
    Hérite de Player et implémente les mouvements spécifiques au pion.
    
    Mouvements de base:
    - Haut : (0, 1)     → déplacement vers le haut
    - Bas : (0, -1)     → déplacement vers le bas
    - Gauche : (-1, 0)  → déplacement vers la gauche
    - Droite : (1, 0)   → déplacement vers la droite
    
    Mouvements supplémentaires (niveau supérieur):
    - Diagonale haut-droite : (1, 1)
    - Diagonale haut-gauche : (-1, 1)
    - Diagonale bas-droite : (1, -1)
    - Diagonale bas-gauche : (-1, -1)
    """
    
    def __init__(self):
        """
        Constructeur de la classe Pawn.
        
        Appelle le constructeur parent avec super() puis
        définit les mouvements de base du pion.
        """
        # Appeler le constructeur de la classe parent (Player)
        super().__init__()
        
        # Définir les mouvements de base du pion
        # Chaque tuple représente (dx, dy) pour se déplacer
        self.moves = [
            (0, 1),   # Haut : y + 1
            (0, -1),  # Bas : y - 1
            (-1, 0),  # Gauche : x - 1
            (1, 0)    # Droite : x + 1
        ]
    
    def level_up(self):
        """
        Augmente le niveau du pion en ajoutant des mouvements diagonaux.
        
        Cette méthode concrète implémente la méthode abstraite level_up
        de la classe Player.
        
        Mouvements diagonaux ajoutés:
        - (1, 1)   : diagonale haut-droite (x+1, y+1)
        - (1, -1)  : diagonale bas-droite (x+1, y-1)
        - (-1, 1)  : diagonale haut-gauche (x-1, y+1)
        - (-1, -1) : diagonale bas-gauche (x-1, y-1)
        """
        # Mouvements diagonaux à ajouter
        diagonal_moves = [
            (1, 1),   # Diagonale haut-droite
            (1, -1),  # Diagonale bas-droite
            (-1, 1),  # Diagonale haut-gauche
            (-1, -1)  # Diagonale bas-gauche
        ]
        
        # Ajouter les mouvements diagonaux à la liste existante
        self.moves.extend(diagonal_moves)


# ============================================
# EXEMPLES D'UTILISATION
# ============================================

# Créer un pion
print("=== EXEMPLE D'UTILISATION ===")
pawn = Pawn()
print(f"Pion créé - Position initiale: {pawn.position}")
print(f"Mouvements de base: {pawn.moves}")

# Effectuer quelques mouvements aléatoires
print("\n--- Mouvements du pion ---")
for i in range(5):
    new_pos = pawn.make_move()
    print(f"Mouvement {i+1}: {new_pos}")

print(f"\nChemin parcouru: {pawn.path}")

# Niveau supérieur - ajout des mouvements diagonaux
print("\n--- Montée de niveau ---")
pawn.level_up()
print(f"Mouvements après level_up: {pawn.moves}")

# Effectuer des mouvements avec les diagonales
for i in range(5):
    new_pos = pawn.make_move()
    print(f"Mouvement après level_up {i+1}: {new_pos}")


# ============================================
# TESTS SUPPLÉMENTAIRES
# ============================================

print("\n\n=== TESTS DE VALIDATION ===\n")

# Test 1 : Vérification de l'abstraction
print("Test 1 : Vérification de la classe abstraite")
try:
    player = Player()  # Devrait lever une erreur car abstraite
    print("  ❌ Player n'est pas abstraite")
except TypeError as e:
    print(f"  ✓ Player est bien abstraite: {e}")

# Test 2 : Vérification de l'instanciation de Pawn
print("\nTest 2 : Instanciation de Pawn")
pawn_test = Pawn()
print(f"  ✓ Pawn instancié avec succès")
print(f"  Position initiale: {pawn_test.position}")
print(f"  Path initial: {pawn_test.path}")

# Test 3 : Vérification des mouvements
print("\nTest 3 : Vérification des mouvements")
pawn_test = Pawn()
initial_pos = pawn_test.position
print(f"  Position avant mouvement: {initial_pos}")
new_pos = pawn_test.make_move()
print(f"  Position après mouvement: {new_pos}")
print(f"  Un mouvement a été effectué")

# Test 4 : Vérification que les mouvements sont limités
print("\nTest 4 : Vérification des limites de mouvement")
pawn_test = Pawn()
possible_moves = pawn_test.moves
print(f"  Mouvements de base: {possible_moves}")
print(f"  Nombre de mouvements: {len(possible_moves)}")
for i in range(10):
    move = pawn_test.make_move()
    print(f"  Position {i+1}: {move}")

# Test 5 : Vérification du level_up
print("\nTest 5 : Vérification de level_up")
pawn_test = Pawn()
initial_moves = pawn_test.moves.copy()
print(f"  Mouvements avant level_up ({len(initial_moves)}): {initial_moves}")
pawn_test.level_up()
print(f"  Mouvements après level_up ({len(pawn_test.moves)}): {pawn_test.moves}")
print(f"  ✓ Mouvements ajoutés: {len(pawn_test.moves) - len(initial_moves)}")

# Test 6 : Vérification des coordonnées
print("\nTest 6 : Vérification des types de coordonnées")
pawn_test = Pawn()
pawn_test.make_move()
print(f"  Position: {pawn_test.position}")
print(f"  Type de position: {type(pawn_test.position)}")
print(f"  Type de x: {type(pawn_test.position[0])}")
print(f"  Type de y: {type(pawn_test.position[1])}")

# Test 7 : Vérification des mouvements après level_up
print("\nTest 7 : Mouvements avec diagonales")
pawn_test = Pawn()
pawn_test.level_up()
print("  Mouvements possibles après niveau supérieur:")
for i, move in enumerate(pawn_test.moves, 1):
    print(f"    {i}: {move}")

# Test 8 : Simulation de jeu
print("\nTest 8 : Simulation de jeu")
pawn_game = Pawn()
print(f"Début du jeu: {pawn_game.position}")
for step in range(10):
    pos = pawn_game.make_move()
    print(f"Étape {step+1}: {pos}")
print(f"\nChemin complet ({len(pawn_game.path)} positions): {pawn_game.path}")

# Test 9 : Level up après plusieurs mouvements
print("\nTest 9 : Level up après mouvements")
pawn_game = Pawn()
for i in range(3):
    pawn_game.make_move()
print(f"Position avant level_up: {pawn_game.position}")
pawn_game.level_up()
for i in range(3):
    pawn_game.make_move()
print(f"Position après level_up: {pawn_game.position}")
print(f"Mouvements totaux: {len(pawn_game.path) - 1}")


# ============================================
# EXEMPLE DE SORTIE
# ============================================
#
# === EXEMPLE D'UTILISATION ===
# Pion créé - Position initiale: (0, 0)
# Mouvements de base: [(0, 1), (0, -1), (-1, 0), (1, 0)]
#
# --- Mouvements du pion ---
# Mouvement 1: (1, 0)
# Mouvement 2: (0, 1)
# Mouvement 3: (0, -1)
# Mouvement 4: (1, 0)
# Mouvement 5: (0, 1)
#
# Chemin parcouru: [(0, 0), (1, 0), (1, 1), (1, 0), (2, 0), (2, 1)]
#
# --- Montée de niveau ---
# Mouvements après level_up: [(0, 1), (0, -1), (-1, 0), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
#
# Mouvement après level_up 1: (2, 2)
# Mouvement après level_up 2: (1, 1)
# Mouvement après level_up 3: (2, 2)
# Mouvement après level_up 4: (3, 2)
# Mouvement après level_up 5: (4, 2)


# ============================================
# DIAGRAMME DE CLASSES
# ============================================
#
#                    ┌─────────────┐
#                    │   abc.ABC   │
#                    └──────┬──────┘
#                           │
#                    ┌──────▼──────┐
#                    │   Player    │ (abstract)
#                    ├─────────────┤
#                    │ -moves: list│
#                    │ -position   │
#                    │ -path: list │
#                    ├─────────────┤
#                    │ +__init__() │
#                    │ +make_move()│
#                    │ +level_up() │ (abstract)
#                    └──────┬──────┘
#                           │
#                    ┌──────▼──────┐
#                    │    Pawn     │
#                    ├─────────────┤
#                    │ +__init__() │
#                    │ +level_up() │
#                    └─────────────┘
#
# ============================================
# RÉSUMÉ DE L'ARCHITECTURE
# ============================================
#
# 1. Player (Classe abstraite) :
#    - Définit l'interface commune pour tous les joueurs
#    - Implémente la logique de mouvement (make_move)
#    - Déclare la méthode abstraite level_up
#    - Utilise abc.ABC pour l'abstraction
#
# 2. Pawn (Classe concrète) :
#    - Hérite de Player
#    - Implémente __init__ avec des mouvements de base
#    - Implémente level_up en ajoutant des diagonales
#    - Est instanciable (contrairement à Player)
#
# AVANTAGES DE L'ABSTRACTION :
# - Force les classes filles à implémenter level_up
# - Évite l'instanciation directe de Player
# - Permet d'ajouter facilement de nouveaux types de joueurs
#
# MOUVEMENTS POSSIBLES :
# - Pion niveau 1 : 4 directions cardinales
# - Pion niveau 2 : 4 directions cardinales + 4 diagonales (8 directions)
#
# ============================================