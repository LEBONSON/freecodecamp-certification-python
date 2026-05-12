# =======================================================
# ATELIER : CATALOGUE MULTIMÉDIA
# =======================================================
# Objectif : Créer un système de gestion de films et séries TV
# avec validation, héritage, exceptions personnalisées et affichage.
# =======================================================

# -------------------------------------------------------
# ÉTAPE 30-31 : Exception personnalisée
# -------------------------------------------------------
# Il fallait créer une classe d'exception spécifique pour
# gérer proprement les erreurs liées aux médias.
# Elle doit mémoriser l'objet problématique.
class MediaError(Exception):
    """Custom exception for media-related errors."""
    def __init__(self, message, obj):
        super().__init__(message)   # Appel au constructeur parent pour stocker le message
        self.obj = obj              # Stocke l'objet à l'origine de l'erreur

# -------------------------------------------------------
# ÉTAPES 1 À 7 : Classe Movie avec validations
# -------------------------------------------------------
# Il fallait définir une classe Movie avec :
# - Une méthode __init__ avec title, year, director, duration
# - Des validations pour chaque attribut (non vide, année>=1895, durée>0)
# - Une méthode __str__ pour l'affichage
# - Une docstring à la fin (étape 27)
class Movie:
    """Parent class representing a movie."""
    
    def __init__(self, title, year, director, duration):
        # Étape 4 : Validation du titre (non vide)
        if not title.strip():
            raise ValueError('Title cannot be empty')
        # Étape 5 : Validation de l'année (>=1895)
        if year < 1895:
            raise ValueError('Year must be 1895 or later')
        # Étape 6 : Validation du réalisateur (non vide)
        if not director.strip():
            raise ValueError('Director cannot be empty')
        # Étape 7 : Validation de la durée (>0)
        if duration <= 0:
            raise ValueError('Duration must be positive')
        
        # Étape 1 : Attribution des attributs
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration

    # Étape 2 : Méthode __str__ pour affichage lisible
    def __str__(self):
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'

# -------------------------------------------------------
# ÉTAPES 16 À 22 : Classe TVSeries (héritage)
# -------------------------------------------------------
# Il fallait créer une sous-classe de Movie avec :
# - Des attributs supplémentaires : seasons, total_episodes
# - Validation de ces nouveaux attributs
# - Surcharge de __str__ pour un format adapté
# - Appel au constructeur parent via super()
class TVSeries(Movie):
    """Child class representing an entire TV series."""

    def __init__(self, title, year, director, duration, seasons, total_episodes):
        # Étape 18 : Appel du constructeur parent via super()
        super().__init__(title, year, director, duration)

        # Étape 19 : Validations spécifiques
        if seasons < 1:
            raise ValueError('Seasons must be 1 or greater')
        if total_episodes < 1:
            raise ValueError('Total episodes must be 1 or greater')
        
        self.seasons = seasons
        self.total_episodes = total_episodes

    # Étape 22 : Surcharge de __str__ avec le format demandé
    def __str__(self):
        return f'{self.title} ({self.year}) - {self.seasons} seasons, {self.total_episodes} episodes, {self.duration} min avg, {self.director}'

# -------------------------------------------------------
# ÉTAPES 10 À 14, 29-32, 37-42 : MediaCatalogue
# -------------------------------------------------------
# Il fallait une classe pour gérer une collection d'éléments média avec :
# - Méthode add avec validation de type
# - Méthodes get_movies et get_tv_series pour filtrer
# - Méthode __str__ affichant séparément films et séries
class MediaCatalogue:
    """A catalogue that can store different types of media items."""

    def __init__(self):
        self.items = []          # Étape 10 : Liste pour stocker les éléments

    # Étape 29 & 32 : Validation du type avant ajout
    def add(self, media_item):
        # Étape 29 : Utilisation de isinstance pour accepter Movie et ses sous-classes
        # Étape 32 : Remplacement de TypeError par MediaError personnalisée
        if not isinstance(media_item, Movie):
            raise MediaError('Only Movie or TVSeries instances can be added', media_item)
        self.items.append(media_item)

    # Étape 37 : Filtre pour n'obtenir que les films (classe parent exacte)
    def get_movies(self):
        # Utilisation de type(item) is Movie pour exclure les sous-classes (TVSeries)
        return [item for item in self.items if type(item) is Movie]

    # Étape 38 : Filtre pour obtenir uniquement les séries TV
    def get_tv_series(self):
        # isinstance fonctionne ici car on veut TVSeries ET ses sous-classes
        return [item for item in self.items if isinstance(item, TVSeries)]
    
    # Étapes 11-14, 39-42 : Méthode __str__ pour affichage structuré
    def __str__(self):
        # Étape 11 : Cas particulier si catalogue vide
        if not self.items:
            return 'Media Catalogue (empty)'
        
        # Étape 39 : Récupération des listes filtrées
        movies = self.get_movies()
        series = self.get_tv_series()

        # Étape 12 : En-tête avec nombre total d'articles
        result = f'Media Catalogue ({len(self.items)} items):\n\n'
        
        # Étape 40-42 : Affichage des films
        if movies:
            result += '=== MOVIES ===\n'
            for i, movie in enumerate(movies, 1):
                result += f'{i}. {movie}\n'
        
        # Étape 42 : Affichage des séries TV
        if series:
            result += "=== TV SERIES ===\n"
            for i, tv_series in enumerate(series, start=1):
                result += f"{i}. {tv_series}\n"
        return result

# -------------------------------------------------------
# ÉTAPES 14, 15, 20, 23, 35 : Utilisation du catalogue
# -------------------------------------------------------
# Il fallait instancier des films, des séries, les ajouter
# au catalogue, et gérer les exceptions.
catalogue = MediaCatalogue()

try:
    # Étape 3 & 14 : Création de movie1
    movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
    catalogue.add(movie1)
    
    # Étape 15 : Création de movie2
    movie2 = Movie('Inception', 2010, 'Christopher Nolan', 148)
    catalogue.add(movie2)

    # Étape 20 & 23 : Création et ajout de séries TV
    series1 = TVSeries('Scrubs', 2001, 'Bill Lawrence', 24, 9, 182)
    catalogue.add(series1)
    series2 = TVSeries('Breaking Bad', 2008, 'Vince Gilligan', 47, 5, 62)
    catalogue.add(series2)

    # Affichage du catalogue (déclenche __str__)
    print(catalogue)

# Gestion des exceptions selon les étapes 8, 35
except ValueError as e:
    print(f'Validation Error: {e}')
except MediaError as e:
    print(f'Media Error: {e}')
    print(f'Unable to add {e.obj}: {type(e.obj)}')