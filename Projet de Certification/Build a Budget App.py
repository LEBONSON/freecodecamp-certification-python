# ============================================
# CRÉEZ UNE APPLICATION BUDGÉTAIRE
# ============================================
# 
# ÉNONCÉ :
# Dans ce laboratoire, vous créerez une application budgétaire simple qui suit
# les dépenses dans différentes catégories et peut afficher le pourcentage
# relatif des dépenses sur un graphique.
#
# OBJECTIF : Remplissez les user stories ci-dessous et obtenez tous les tests
# à réussir pour terminer le laboratoire.
#
# HISTOIRES D'UTILISATEURS :
#
# 1. Vous devriez avoir une classe Category qui accepte un nom comme argument.
#
# 2. La classe Category doit avoir un attribut d'instance ledger qui est une liste
#    et contient la liste des transactions.
#
# 3. La classe Category doit avoir les méthodes suivantes :
#    - deposit : ajoute un dépôt au ledger
#    - withdraw : retire de l'argent si les fonds sont suffisants
#    - get_balance : calcule le solde actuel
#    - transfer : transfère de l'argent vers une autre catégorie
#    - check_funds : vérifie si les fonds sont suffisants
#
# 4. Quand un objet Category est imprimé, il doit :
#    - Afficher une ligne de titre de 30 caractères avec le nom centré entre *
#    - Lister chaque entrée du ledger avec description (23 caractères max) et montant
#    - Afficher une dernière ligne "Total: [balance]"
#
# 5. Vous devriez avoir une fonction create_spend_chart(categories) qui renvoie
#    un graphique à barres des pourcentages de dépenses par catégorie.
#
# ============================================

class Category:
    """
    Classe représentant une catégorie budgétaire.
    
    Attributs:
    name (str): Nom de la catégorie
    ledger (list): Liste des transactions (dépôts, retraits, transferts)
    """
    
    # ------------------------------------------
    # 1. MÉTHODE CONSTRUCTEUR __init__
    # ------------------------------------------
    
    def __init__(self, name):
        """
        Constructeur de la classe Category.
        
        Paramètres:
        name (str): Nom de la catégorie (ex: 'Food', 'Clothing')
        
        Initialise:
        - name : nom de la catégorie
        - ledger : liste vide pour stocker les transactions
        """
        self.name = name      # Nom de la catégorie
        self.ledger = []      # Liste des transactions (dépôts, retraits)
    
    # ------------------------------------------
    # 2. MÉTHODE deposit
    # ------------------------------------------
    
    def deposit(self, amount, description=""):
        """
        Ajoute un dépôt au ledger.
        
        Paramètres:
        amount (float): Montant à déposer
        description (str): Description optionnelle du dépôt (défaut: "")
        
        Ajoute au ledger: {'amount': amount, 'description': description}
        """
        # Ajouter la transaction de dépôt au ledger
        self.ledger.append({"amount": amount, "description": description})
    
    # ------------------------------------------
    # 3. MÉTHODE withdraw
    # ------------------------------------------
    
    def withdraw(self, amount, description=""):
        """
        Retire de l'argent si les fonds sont suffisants.
        
        Paramètres:
        amount (float): Montant à retirer
        description (str): Description optionnelle du retrait (défaut: "")
        
        Retourne:
        bool: True si le retrait a réussi, False sinon
        
        Note: Le montant est stocké comme nombre négatif dans le ledger
        """
        # Vérifier si les fonds sont suffisants
        if self.check_funds(amount):
            # Ajouter le retrait (montant négatif) au ledger
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False
    
    # ------------------------------------------
    # 4. MÉTHODE get_balance
    # ------------------------------------------
    
    def get_balance(self):
        """
        Calcule le solde actuel de la catégorie.
        
        Retourne:
        float: Somme de tous les montants dans le ledger
        """
        # Additionner tous les montants (positifs et négatifs)
        return sum(item["amount"] for item in self.ledger)
    
    # ------------------------------------------
    # 5. MÉTHODE transfer
    # ------------------------------------------
    
    def transfer(self, amount, category):
        """
        Transfère de l'argent vers une autre catégorie.
        
        Paramètres:
        amount (float): Montant à transférer
        category (Category): Catégorie de destination
        
        Retourne:
        bool: True si le transfert a réussi, False sinon
        
        Le transfert effectue deux opérations :
        1. Retrait de la catégorie source avec description "Transfer to [Destination]"
        2. Dépôt dans la catégorie destination avec description "Transfer from [Source]"
        """
        # Vérifier si les fonds sont suffisants
        if self.check_funds(amount):
            # Retirer de la catégorie actuelle (source)
            self.withdraw(amount, f"Transfer to {category.name}")
            
            # Déposer dans la catégorie de destination
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    # ------------------------------------------
    # 6. MÉTHODE check_funds
    # ------------------------------------------
    
    def check_funds(self, amount):
        """
        Vérifie si les fonds sont suffisants pour une opération.
        
        Paramètres:
        amount (float): Montant à vérifier
        
        Retourne:
        bool: True si amount <= solde, False sinon
        
        Cette méthode est utilisée par withdraw et transfer
        """
        return amount <= self.get_balance()
    
    # ------------------------------------------
    # 7. MÉTHODE get_withdrawals (utilitaire)
    # ------------------------------------------
    
    def get_withdrawals(self):
        """
        Calcule le total des retraits pour cette catégorie.
        
        Retourne:
        float: Somme de tous les retraits (valeurs positives)
        
        Note: Cette méthode est utilisée pour le graphique des dépenses
        """
        # Additionner les montants négatifs (retraits) et inverser le signe
        return sum(-item["amount"] for item in self.ledger if item["amount"] < 0)
    
    # ------------------------------------------
    # 8. MÉTHODE __str__
    # ------------------------------------------
    
    def __str__(self):
        """
        Représentation string de la catégorie pour l'affichage.
        
        Format:
        - Ligne de titre : 30 caractères avec le nom centré entre *
        - Chaque transaction : description (23 caractères max) alignée à gauche,
          montant (7 caractères max, 2 décimales) aligné à droite
        - Ligne de total : "Total: [balance]" avec 2 décimales
        
        Retourne:
        str: Représentation formatée de la catégorie
        """
        # 1. Ligne de titre (30 caractères, nom centré entre *)
        # Exemple: "*************Food*************"
        title = f"{self.name:*^30}\n"
        
        # 2. Construction des lignes de transaction
        entries = ""
        for item in self.ledger:
            # Description : maximum 23 caractères
            description = item["description"][:23]
            
            # Montant : formaté avec 2 décimales, 7 caractères de large
            amount = f"{item['amount']:.2f}"
            
            # Ajouter la ligne formatée
            # description: alignée à gauche sur 23 caractères
            # amount: alignée à droite sur 7 caractères
            entries += f"{description:<23}{amount:>7}\n"
        
        # 3. Ligne de total
        total = f"Total: {self.get_balance():.2f}"
        
        # Retourner la chaîne complète
        return title + entries + total


# ============================================
# FONCTION create_spend_chart
# ============================================
# Crée un graphique à barres des pourcentages de dépenses
# ============================================

def create_spend_chart(categories):
    """
    Crée un graphique à barres montrant le pourcentage dépensé par catégorie.
    
    Paramètres:
    categories (list): Liste d'objets Category
    
    Retourne:
    str: Graphique à barres formaté avec les pourcentages de dépenses
    
    Le graphique affiche :
    - Titre "Percentage spent by category"
    - Axe Y de 100 à 0 par pas de 10
    - Barres avec 'o' pour chaque pourcentage (arrondi à la dizaine inférieure)
    - Ligne horizontale sous les barres
    - Noms des catégories écrits verticalement
    """
    
    # ------------------------------------------
    # 1. CALCUL DES POURCENTAGES
    # ------------------------------------------
    
    # Récupérer le total des retraits pour chaque catégorie
    withdrawals = [category.get_withdrawals() for category in categories]
    
    # Calculer le total général des dépenses
    total_spent = sum(withdrawals)
    
    # Calculer le pourcentage pour chaque catégorie
    # Éviter la division par zéro si total_spent == 0
    if total_spent == 0:
        percentages = [0] * len(categories)
    else:
        # Pourcentage = (dépenses_catégorie / total) * 100
        # Puis arrondir à la dizaine inférieure
        # Exemple: 43% devient 40, 67% devient 60
        percentages = [int((w / total_spent) * 100) // 10 * 10 for w in withdrawals]
    
    # ------------------------------------------
    # 2. CONSTRUCTION DU GRAPHIQUE
    # ------------------------------------------
    
    # Titre du graphique
    chart = "Percentage spent by category\n"
    
    # Axe Y : de 100 à 0 par pas de 10
    for i in range(100, -1, -10):
        # Afficher la valeur de l'axe Y (alignée à droite sur 3 caractères)
        chart += f"{i:>3}|"
        
        # Pour chaque catégorie, afficher 'o' si le pourcentage >= valeur actuelle
        for percentage in percentages:
            if percentage >= i:
                chart += " o "  # Barre avec espacements
            else:
                chart += "   "  # Espace vide
        chart += " \n"  # Espace supplémentaire après la dernière barre
    
    # ------------------------------------------
    # 3. LIGNE HORIZONTALE
    # ------------------------------------------
    
    # Ligne horizontale sous les barres
    # 4 espaces initiaux + 3 tirets par catégorie + 1 tiret final
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # ------------------------------------------
    # 4. NOMS DES CATÉGORIES VERTICALEMENT
    # ------------------------------------------
    
    # Trouver la longueur maximale des noms de catégories
    max_name_length = max(len(category.name) for category in categories)
    
    # Afficher les lettres verticalement
    for i in range(max_name_length):
        # Indentation de 5 espaces
        chart += "     "
        
        # Pour chaque catégorie, afficher la lettre si elle existe
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "  # Lettre + 2 espaces
            else:
                chart += "   "  # Espaces vides
        
        # Ajouter un retour à la ligne sauf pour la dernière ligne
        if i < max_name_length - 1:
            chart += "\n"
    
    # Retourner le graphique (sans retour à la ligne final)
    return chart


# ============================================
# EXEMPLES D'UTILISATION
# ============================================

# Création des catégories
food = Category('Food')
clothing = Category('Clothing')
auto = Category('Auto')

# Dépôts initiaux
food.deposit(1000, 'initial deposit')
clothing.deposit(500, 'initial deposit')
auto.deposit(300, 'initial deposit')

# Retraits
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing.withdraw(50.00, 'jacket')
auto.withdraw(30.00, 'gas')

# Transfert
food.transfer(50, clothing)

# Affichage d'une catégorie
print(food)
# Résultat attendu :
# *************Food*************
# initial deposit        1000.00
# groceries               -10.15
# restaurant and more foo -15.89
# Transfer to Clothing    -50.00
# Total: 923.96

# Création du graphique des dépenses
print(create_spend_chart([food, clothing, auto]))
# Résultat attendu :
# Percentage spent by category
# 100|          
#  90|          
#  80|          
#  70|          
#  60| o        
#  50| o        
#  40| o        
#  30| o        
#  20| o  o     
#  10| o  o  o  
#   0| o  o  o  
#     ----------
#      F  C  A  
#      o  l  u  
#      o  o  t  
#      d  t  o  
#         h     
#         i     
#         n     
#         g


# ============================================
# TESTS DE VALIDATION
# ============================================

# Test des dépôts et retraits
print("\n--- Test des dépôts et retraits ---")
test_cat = Category('Test')
test_cat.deposit(100, 'test deposit')
test_cat.withdraw(30, 'test withdrawal')
print(f"Solde après opérations: {test_cat.get_balance()}")  # Devrait être 70

# Test de check_funds
print(f"Fonds suffisants pour 50? {test_cat.check_funds(50)}")  # True
print(f"Fonds suffisants pour 100? {test_cat.check_funds(100)}")  # False

# Test de transfert insuffisant
print(f"Transfert de 200 (insuffisant): {test_cat.transfer(200, food)}")  # False

# Test de la fonction __str__
print("\n--- Test de __str__ ---")
print(test_cat)

# Test du graphique avec une seule catégorie
print("\n--- Test du graphique avec une catégorie ---")
single_category = Category('Food')
single_category.withdraw(100, 'groceries')
print(create_spend_chart([single_category]))

# Test du graphique avec catégorie sans dépenses
print("\n--- Test sans dépenses ---")
no_spend = Category('NoSpend')
print(create_spend_chart([no_spend]))


# ============================================
# RÉSUMÉ DE LA LOGIQUE :
# 1. Category : gère une catégorie budgétaire
#    - ledger : liste des transactions
#    - deposit : ajoute un montant positif
#    - withdraw : ajoute un montant négatif (si fonds suffisants)
#    - transfer : combine withdraw et deposit entre catégories
#    - check_funds : validation des fonds avant opération
#
# 2. create_spend_chart : génère un graphique
#    - Calcule les pourcentages basés sur les retraits uniquement
#    - Arrondit à la dizaine inférieure
#    - Utilise 'o' pour les barres
#    - Affiche les noms verticalement
# ============================================