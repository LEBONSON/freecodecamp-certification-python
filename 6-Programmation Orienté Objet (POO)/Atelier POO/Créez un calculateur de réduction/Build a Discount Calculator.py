# ============================================
# DISCOUNT ENGINE - MOTEUR DE RÉDUCTION
# ============================================
# 
# ÉNONCÉ :
# Dans cet atelier, vous allez créer un système de gestion de réductions
# utilisant le pattern Strategy (Patron de conception Stratégie).
# Le système permet d'appliquer différentes stratégies de réduction
# et de choisir la meilleure offre pour un utilisateur donné.
#
# OBJECTIF : Créer les classes suivantes avec leurs fonctionnalités :
#
# 1. Une classe Product représentant un produit
# 2. Une classe abstraite DiscountStrategy définissant le contrat
# 3. Des stratégies concrètes de réduction :
#    - PercentageDiscount (réduction en pourcentage)
#    - FixedAmountDiscount (réduction d'un montant fixe)
#    - PremiumUserDiscount (réduction spéciale pour utilisateurs premium)
# 4. Une classe DiscountEngine qui applique la meilleure réduction
#
# PATTERN STRATEGY :
# - Permet de définir une famille d'algorithmes interchangeables
# - Facilite l'ajout de nouvelles stratégies sans modifier le code existant
# - Applique le principe Open/Closed (ouvert à l'extension, fermé à la modification)
#
# ============================================

from abc import ABC, abstractmethod

# ------------------------------------------
# 1. CLASSE PRODUCT
# ------------------------------------------
# Représente un produit avec son nom et son prix
# ==========================================

class Product:
    """
    Classe représentant un produit disponible à l'achat.
    
    Attributs:
    name (str): Nom du produit
    price (float): Prix du produit en dollars
    """
    
    def __init__(self, name: str, price: float) -> None:
        """
        Constructeur de la classe Product.
        
        Paramètres:
        name (str): Nom du produit
        price (float): Prix du produit
        """
        self.name = name      # Nom du produit
        self.price = price    # Prix du produit

    def __str__(self) -> str:
        """
        Représentation string du produit.
        
        Retourne:
        str: Format "Nom - $prix"
        """
        return f'{self.name} - ${self.price}'


# ------------------------------------------
# 2. CLASSE ABSTRAITE DISCOUNTSTRATEGY
# ------------------------------------------
# Définit le contrat pour toutes les stratégies de réduction
# ==========================================

class DiscountStrategy(ABC):
    """
    Classe abstraite définissant l'interface pour les stratégies de réduction.
    
    Méthodes abstraites:
    is_applicable: Vérifie si la stratégie peut être appliquée
    apply_discount: Calcule le prix après réduction
    """
    
    @abstractmethod
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        """
        Vérifie si la stratégie de réduction est applicable.
        
        Paramètres:
        product (Product): Le produit à évaluer
        user_tier (str): Niveau de l'utilisateur (ex: 'premium', 'standard')
        
        Retourne:
        bool: True si la réduction s'applique, False sinon
        """
        pass

    @abstractmethod
    def apply_discount(self, product: Product) -> float:
        """
        Applique la réduction au produit.
        
        Paramètres:
        product (Product): Le produit à réduire
        
        Retourne:
        float: Le prix après application de la réduction
        """
        pass


# ------------------------------------------
# 3. STRATÉGIE : PERCENTAGEDISCOUNT
# ------------------------------------------
# Réduction en pourcentage (ex: -10%, -20%)
# ==========================================

class PercentageDiscount(DiscountStrategy):
    """
    Stratégie de réduction en pourcentage.
    
    Attributs:
    percent (int): Pourcentage de réduction (ex: 10 pour 10%)
    
    Règle d'application:
    La réduction s'applique si le pourcentage ne dépasse pas 70%
    (limite maximale de réduction autorisée)
    """
    
    def __init__(self, percent: int) -> None:
        """
        Constructeur de PercentageDiscount.
        
        Paramètres:
        percent (int): Pourcentage de réduction (0 à 100)
        """
        self.percent = percent

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        """
        Vérifie si la réduction en pourcentage est applicable.
        
        Règle: Le pourcentage ne doit pas dépasser 70%
        (évite les réductions trop importantes)
        
        Paramètres:
        product (Product): Le produit (non utilisé dans cette règle)
        user_tier (str): Niveau utilisateur (non utilisé dans cette règle)
        
        Retourne:
        bool: True si percent ≤ 70, False sinon
        """
        return self.percent <= 70

    def apply_discount(self, product: Product) -> float:
        """
        Applique la réduction en pourcentage.
        
        Formule: prix_final = prix × (1 - pourcentage/100)
        Exemple: prix=100, percent=10 → 100 × 0.9 = 90
        
        Paramètres:
        product (Product): Le produit à réduire
        
        Retourne:
        float: Prix après réduction en pourcentage
        """
        return product.price * (1 - self.percent / 100)


# ------------------------------------------
# 4. STRATÉGIE : FIXEDAMOUNTDISCOUNT
# ------------------------------------------
# Réduction d'un montant fixe (ex: -5$, -10$)
# ==========================================

class FixedAmountDiscount(DiscountStrategy):
    """
    Stratégie de réduction d'un montant fixe.
    
    Attributs:
    amount (int): Montant à déduire (en dollars)
    
    Règle d'application:
    Le prix après réduction de 10% doit être supérieur au montant
    Condition: prix × 0.9 > amount
    (Garantit que le prix final reste raisonnable)
    """
    
    def __init__(self, amount: int) -> None:
        """
        Constructeur de FixedAmountDiscount.
        
        Paramètres:
        amount (int): Montant à déduire du prix
        """
        self.amount = amount

    def is_applicable(self, product: Product, user_tier: str) -> bool:
        """
        Vérifie si la réduction d'un montant fixe est applicable.
        
        Règle: Le prix après 10% de réduction doit être supérieur au montant
        Évite d'appliquer une réduction trop agressive
        
        Formule: product.price × 0.9 > amount
        
        Paramètres:
        product (Product): Le produit à évaluer
        user_tier (str): Niveau utilisateur (non utilisé)
        
        Retourne:
        bool: True si condition vérifiée, False sinon
        """
        return product.price * 0.9 > self.amount

    def apply_discount(self, product: Product) -> float:
        """
        Applique la réduction d'un montant fixe.
        
        Formule: prix_final = prix - montant
        
        Paramètres:
        product (Product): Le produit à réduire
        
        Retourne:
        float: Prix après déduction du montant fixe
        """
        return product.price - self.amount


# ------------------------------------------
# 5. STRATÉGIE : PREMIUMUSERDISCOUNT
# ------------------------------------------
# Réduction spéciale pour les utilisateurs premium
# ==========================================

class PremiumUserDiscount(DiscountStrategy):
    """
    Stratégie de réduction pour utilisateurs premium.
    
    Règle d'application:
    S'applique uniquement si l'utilisateur est 'premium'
    (insensible à la casse)
    
    Réduction: Prix × 0.8 (20% de réduction)
    """
    
    def is_applicable(self, product: Product, user_tier: str) -> bool:
        """
        Vérifie si l'utilisateur a droit à la réduction premium.
        
        Règle: user_tier.lower() == 'premium'
        
        Paramètres:
        product (Product): Le produit (non utilisé)
        user_tier (str): Niveau de l'utilisateur
        
        Retourne:
        bool: True si l'utilisateur est premium, False sinon
        """
        return user_tier.lower() == 'premium'

    def apply_discount(self, product: Product) -> float:
        """
        Applique la réduction premium.
        
        Formule: prix_final = prix × 0.8 (20% de réduction)
        
        Paramètres:
        product (Product): Le produit à réduire
        
        Retourne:
        float: Prix après réduction premium
        """
        return product.price * 0.8


# ------------------------------------------
# 6. CLASSE DISCOUNTENGINE
# ------------------------------------------
# Moteur qui calcule la meilleure réduction parmi plusieurs stratégies
# ==========================================

class DiscountEngine:
    """
    Moteur de calcul des réductions.
    Évalue toutes les stratégies applicables et retourne le meilleur prix.
    
    Attributs:
    strategies (list[DiscountStrategy]): Liste des stratégies à appliquer
    
    Principe:
    - Teste chaque stratégie avec is_applicable()
    - Calcule le prix réduit pour les stratégies applicables
    - Retourne le prix le plus bas
    """
    
    def __init__(self, strategies: list[DiscountStrategy]) -> None:
        """
        Constructeur de DiscountEngine.
        
        Paramètres:
        strategies (list[DiscountStrategy]): Liste des stratégies à utiliser
        """
        self.strategies = strategies

    def calculate_best_price(self, product: Product, user_tier: str) -> float:
        """
        Calcule le meilleur prix pour un produit et un utilisateur donnés.
        
        Algorithme:
        1. Initialiser la liste des prix avec le prix original
        2. Pour chaque stratégie :
           a. Vérifier si la stratégie s'applique (is_applicable)
           b. Si oui, calculer le prix réduit (apply_discount)
           c. Ajouter ce prix à la liste
        3. Retourner le prix minimum de la liste
        
        Paramètres:
        product (Product): Le produit à évaluer
        user_tier (str): Niveau de l'utilisateur
        
        Retourne:
        float: Le meilleur prix possible après réduction
        """
        # Commencer avec le prix original
        prices = [product.price]
        
        # Tester chaque stratégie
        for strategy in self.strategies:
            if strategy.is_applicable(product, user_tier):
                discounted = strategy.apply_discount(product)
                prices.append(discounted)
        
        # Retourner le prix le plus bas
        return min(prices)


# ============================================
# POINT D'ENTRÉE PRINCIPAL
# ============================================

if __name__ == '__main__':
    # Création d'un produit
    product = Product('Wireless Mouse', 50.0)
    
    # Niveau de l'utilisateur
    user_tier = 'Premium'
    
    # Configuration des stratégies de réduction
    strategies = [
        PercentageDiscount(10),   # 10% de réduction = 45.00$
        FixedAmountDiscount(5),   # 5$ de réduction = 45.00$
        PremiumUserDiscount()     # 20% de réduction = 40.00$ (meilleur prix)
    ]
    
    # Création du moteur de réduction
    engine = DiscountEngine(strategies)
    
    # Calcul du meilleur prix
    best_price = engine.calculate_best_price(product, user_tier)
    
    # Affichage du résultat final
    print(f"Best price for {product.name} for {user_tier} user: ${best_price:.2f}")
    # Sortie: "Best price for Wireless Mouse for Premium user: $40.00"


# ============================================
# TESTS SUPPLÉMENTAIRES
# ============================================

def run_additional_tests():
    """
    Fonction de test pour valider les différentes stratégies.
    """
    print("\n" + "="*50)
    print("TESTS SUPPLÉMENTAIRES")
    print("="*50)
    
    # Test 1 : Utilisateur standard
    print("\n1. Utilisateur standard avec toutes les réductions")
    product_std = Product('Keyboard', 100.0)
    user_std = 'Standard'
    engine_std = DiscountEngine([
        PercentageDiscount(10),
        FixedAmountDiscount(5),
        PremiumUserDiscount()
    ])
    best = engine_std.calculate_best_price(product_std, user_std)
    print(f"   Produit: {product_std}")
    print(f"   Utilisateur: {user_std}")
    print(f"   Meilleur prix: ${best:.2f}")
    print(f"   (Original: $100, -10% = $90, -$5 = $95, Premium: non applicable) → $90")
    
    # Test 2 : Réduction en pourcentage élevée (non applicable)
    print("\n2. Réduction en pourcentage excessive (75%)")
    product_high = Product('Expensive Item', 200.0)
    engine_high = DiscountEngine([PercentageDiscount(75)])
    best = engine_high.calculate_best_price(product_high, 'Standard')
    print(f"   Produit: {product_high}")
    print(f"   Réduction 75% demandée mais limitée à 70% max → non applicable")
    print(f"   Meilleur prix: ${best:.2f} (prix original)")
    
    # Test 3 : Montant fixe trop élevé
    print("\n3. Montant fixe trop élevé (non applicable)")
    product_small = Product('Small Item', 30.0)
    engine_fixed = DiscountEngine([FixedAmountDiscount(28)])
    # Condition: 30 × 0.9 = 27 > 28? NON → non applicable
    best = engine_fixed.calculate_best_price(product_small, 'Standard')
    print(f"   Produit: {product_small}")
    print(f"   Condition: 30 × 0.9 = 27 > 28? False → réduction non applicable")
    print(f"   Meilleur prix: ${best:.2f}")
    
    # Test 4 : Comparaison des différentes stratégies
    print("\n4. Comparaison complète des stratégies")
    product_comp = Product('Monitor', 200.0)
    user_comp = 'Premium'
    engines = {
        'Original': DiscountEngine([]),
        '10% réduction': DiscountEngine([PercentageDiscount(10)]),
        '20$ réduction': DiscountEngine([FixedAmountDiscount(20)]),
        'Premium (20%)': DiscountEngine([PremiumUserDiscount()]),
        'Toutes stratégies': DiscountEngine([
            PercentageDiscount(10),
            FixedAmountDiscount(20),
            PremiumUserDiscount()
        ])
    }
    for name, eng in engines.items():
        price = eng.calculate_best_price(product_comp, user_comp)
        print(f"   {name:20} → ${price:.2f}")
    
    # Test 5 : Produits avec différents prix
    print("\n5. Test avec plusieurs produits")
    products = [
        Product('Item A', 25.0),
        Product('Item B', 50.0),
        Product('Item C', 100.0),
        Product('Item D', 200.0)
    ]
    user_tiers = ['Standard', 'Premium']
    
    print("\n   Meilleur prix pour chaque produit et niveau utilisateur:")
    for product_item in products:
        for tier in user_tiers:
            engine_all = DiscountEngine([
                PercentageDiscount(10),
                FixedAmountDiscount(5),
                PremiumUserDiscount()
            ])
            best = engine_all.calculate_best_price(product_item, tier)
            print(f"   {product_item.name:10} | {tier:10} → ${best:.2f}")
    
    # Test 6 : Stratégies personnalisées
    print("\n6. Stratégies personnalisées")
    product_custom = Product('Gaming Mouse', 80.0)
    
    print(f"   Produit: {product_custom}")
    print(f"   Prix original: ${product_custom.price:.2f}")
    
    # Différentes combinaisons
    combos = [
        ("10% réduction", [PercentageDiscount(10)]),
        ("15$ réduction", [FixedAmountDiscount(15)]),
        ("Premium + 10%", [PremiumUserDiscount(), PercentageDiscount(10)]),
        ("Premium + 15$", [PremiumUserDiscount(), FixedAmountDiscount(15)]),
        ("Tout combiné", [PercentageDiscount(10), FixedAmountDiscount(15), PremiumUserDiscount()])
    ]
    
    for name, strat_list in combos:
        engine_custom = DiscountEngine(strat_list)
        best = engine_custom.calculate_best_price(product_custom, 'Premium')
        print(f"   {name:20} → ${best:.2f}")


# Décommentez pour exécuter les tests supplémentaires
# run_additional_tests()


# ============================================
# DIAGRAMME DE LA RELATION DES CLASSES
# ============================================
#
#                    ┌─────────────────┐
#                    │   <<ABC>>       │
#                    │ DiscountStrategy│
#                    ├─────────────────┤
#                    │ +is_applicable()│
#                    │ +apply_discount()│
#                    └────────┬────────┘
#                             │
#         ┌───────────────────┼───────────────────┐
#         │                   │                   │
#         ▼                   ▼                   ▼
# ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
# │PercentageDiscount│ │FixedAmountDiscount│ │PremiumUserDiscount│
# ├─────────────────┤ ├─────────────────┤ ├─────────────────┤
# │ -percent: int   │ │ -amount: int   │ │                 │
# ├─────────────────┤ ├─────────────────┤ ├─────────────────┤
# │ +is_applicable()│ │ +is_applicable()│ │ +is_applicable()│
# │ +apply_discount()│ │ +apply_discount()│ │ +apply_discount()│
# └─────────────────┘ └─────────────────┘ └─────────────────┘
#
#                    ┌─────────────────┐
#                    │ DiscountEngine  │
#                    ├─────────────────┤
#                    │ -strategies     │
#                    ├─────────────────┤
#                    │ +calculate_best │
#                    │ _price()        │
#                    └─────────────────┘
#
#                    ┌─────────────────┐
#                    │    Product      │
#                    ├─────────────────┤
#                    │ -name: str      │
#                    │ -price: float   │
#                    ├─────────────────┤
#                    │ +__str__()      │
#                    └─────────────────┘
#
# ============================================
# RÉSUMÉ DE L'ARCHITECTURE
# ============================================
#
# 1. Product : Modèle de données simple
#    - Contient les informations du produit (nom, prix)
#    - Méthode __str__ pour l'affichage
#
# 2. DiscountStrategy (Pattern Strategy) :
#    - Interface abstraite définissant le contrat
#    - Deux méthodes : is_applicable + apply_discount
#    - Hérite de ABC pour être abstraite
#
# 3. Stratégies concrètes :
#    - PercentageDiscount : réduction en pourcentage (max 70%)
#    - FixedAmountDiscount : réduction d'un montant fixe (max 10% du prix)
#    - PremiumUserDiscount : réduction spéciale premium (20%)
#
# 4. DiscountEngine (Context) :
#    - Agrège les stratégies dans une liste
#    - Calcule le meilleur prix en essayant toutes les stratégies
#    - Applique le principe Open/Closed
#
# AVANTAGES DU PATTERN STRATEGY :
# - Évite les longues chaînes if/elif/else
# - Facilite l'ajout de nouvelles stratégies sans modifier le moteur
# - Rend le code plus testable et maintenable
# - Permet de composer différentes stratégies dynamiquement
# - Sépare la logique de calcul de la logique d'application
#
# ============================================