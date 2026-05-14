# ============================================
# BUILD AN EMAIL SYSTEM
# ============================================
# 
# ÉNONCÉ :
# Dans cet atelier, vous allez créer un système d'email simple qui permet
# aux utilisateurs d'envoyer, recevoir, lire et supprimer des emails.
#
# OBJECTIF : Créer les classes suivantes avec leurs fonctionnalités :
#
# CLASSE Email :
# - Attributs : sender, receiver, subject, body, timestamp, read
# - Méthode mark_as_read() : marque l'email comme lu
# - Méthode display_full_email() : affiche l'email complet et le marque comme lu
# - Méthode __str__() : affiche un résumé de l'email
#
# CLASSE Inbox :
# - Attributs : emails (liste)
# - Méthode receive_email() : ajoute un email à la boîte de réception
# - Méthode list_emails() : affiche tous les emails avec des numéros
# - Méthode read_email() : affiche un email spécifique par son numéro
# - Méthode delete_email() : supprime un email spécifique par son numéro
#
# CLASSE User :
# - Attributs : name, inbox
# - Méthode send_email() : crée et envoie un email à un autre utilisateur
# - Méthode check_inbox() : affiche la boîte de réception de l'utilisateur
# - Méthode read_email() : lit un email spécifique par son numéro
# - Méthode delete_email() : supprime un email spécifique par son numéro
#
# ============================================

import datetime

# ============================================
# CLASSE EMAIL
# ============================================
# Représente un email individuel avec ses métadonnées
# ============================================

class Email:
    """
    Classe représentant un email avec expéditeur, destinataire, contenu et état.
    
    Attributs:
    sender (User): L'utilisateur qui envoie l'email
    receiver (User): L'utilisateur qui reçoit l'email
    subject (str): L'objet de l'email
    body (str): Le corps du message
    timestamp (datetime): Date et heure d'envoi
    read (bool): Statut de lecture de l'email (False par défaut)
    """
    
    def __init__(self, sender, receiver, subject, body):
        """
        Constructeur de la classe Email.
        
        Paramètres:
        sender (User): Expéditeur de l'email
        receiver (User): Destinataire de l'email
        subject (str): Objet de l'email
        body (str): Corps du message
        """
        self.sender = sender          # Expéditeur (objet User)
        self.receiver = receiver      # Destinataire (objet User)
        self.subject = subject        # Objet de l'email
        self.body = body              # Corps du message
        self.timestamp = datetime.datetime.now()  # Horodatage automatique
        self.read = False             # Statut de lecture (non lu par défaut)

    def mark_as_read(self):
        """
        Marque l'email comme lu.
        
        Modifie l'attribut read de False à True.
        """
        self.read = True

    def display_full_email(self):
        """
        Affiche l'email complet dans un format structuré.
        
        Marque automatiquement l'email comme lu lors de l'affichage.
        """
        # Marquer l'email comme lu
        self.mark_as_read()
        
        # Affichage formaté de l'email
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        # Formatage de la date : YYYY-MM-DD HH:MM
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    def __str__(self):
        """
        Représentation string simplifiée de l'email.
        
        Retourne:
        str: Format "[Read/Unread] From: expéditeur | Subject: objet | Time: horaire"
        """
        # Déterminer le statut de lecture
        status = 'Read' if self.read else 'Unread'
        
        # Retourner le résumé formaté
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


# ============================================
# CLASSE INBOX
# ============================================
# Gère la boîte de réception d'un utilisateur
# ============================================

class Inbox:
    """
    Classe représentant la boîte de réception d'un utilisateur.
    
    Attributs:
    emails (list): Liste des emails reçus
    """
    
    def __init__(self):
        """
        Constructeur de la classe Inbox.
        
        Initialise une liste vide pour stocker les emails.
        """
        self.emails = []  # Liste des emails dans la boîte de réception

    def receive_email(self, email):
        """
        Reçoit un email et l'ajoute à la boîte de réception.
        
        Paramètres:
        email (Email): L'email à ajouter
        """
        self.emails.append(email)

    def list_emails(self):
        """
        Affiche tous les emails de la boîte de réception avec leurs numéros.
        
        Si la boîte est vide, affiche un message approprié.
        """
        # Vérifier si la boîte de réception est vide
        if not self.emails:
            print('Your inbox is empty.\n')
            return
        
        # Afficher la liste des emails numérotés
        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')

    def read_email(self, index):
        """
        Lit un email spécifique par son numéro (1-indexé).
        
        Paramètres:
        index (int): Numéro de l'email dans la liste (1, 2, 3...)
        
        Gère les erreurs : boîte vide ou numéro invalide.
        """
        # Vérifier si la boîte est vide
        if not self.emails:
            print('Inbox is empty.\n')
            return
        
        # Convertir en index 0-indexé
        actual_index = index - 1
        
        # Vérifier si l'index est valide
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        
        # Afficher l'email complet
        self.emails[actual_index].display_full_email()

    def delete_email(self, index):
        """
        Supprime un email spécifique par son numéro (1-indexé).
        
        Paramètres:
        index (int): Numéro de l'email dans la liste (1, 2, 3...)
        
        Gère les erreurs : boîte vide ou numéro invalide.
        """
        # Vérifier si la boîte est vide
        if not self.emails:
            print('Inbox is empty.\n')
            return
        
        # Convertir en index 0-indexé
        actual_index = index - 1
        
        # Vérifier si l'index est valide
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return
        
        # Supprimer l'email
        del self.emails[actual_index]
        print('Email deleted.\n')


# ============================================
# CLASSE USER
# ============================================
# Représente un utilisateur avec sa boîte de réception
# ============================================

class User:
    """
    Classe représentant un utilisateur du système d'email.
    
    Attributs:
    name (str): Nom de l'utilisateur
    inbox (Inbox): Boîte de réception de l'utilisateur
    """
    
    def __init__(self, name):
        """
        Constructeur de la classe User.
        
        Paramètres:
        name (str): Nom de l'utilisateur
        """
        self.name = name          # Nom de l'utilisateur
        self.inbox = Inbox()      # Boîte de réception associée

    def send_email(self, receiver, subject, body):
        """
        Envoie un email à un autre utilisateur.
        
        Paramètres:
        receiver (User): Le destinataire de l'email
        subject (str): L'objet de l'email
        body (str): Le corps du message
        
        L'email est automatiquement ajouté à la boîte de réception du destinataire.
        """
        # Créer un nouvel email
        email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        
        # Ajouter l'email à la boîte de réception du destinataire
        receiver.inbox.receive_email(email)
        
        # Confirmation d'envoi
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    def check_inbox(self):
        """
        Affiche le contenu de la boîte de réception de l'utilisateur.
        """
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index):
        """
        Lit un email spécifique dans la boîte de réception.
        
        Paramètres:
        index (int): Numéro de l'email à lire
        """
        self.inbox.read_email(index)

    def delete_email(self, index):
        """
        Supprime un email spécifique de la boîte de réception.
        
        Paramètres:
        index (int): Numéro de l'email à supprimer
        """
        self.inbox.delete_email(index)


# ============================================
# FONCTION PRINCIPALE main()
# ============================================
# Exemple d'utilisation du système d'email
# ============================================

def main():
    """
    Fonction principale qui démontre l'utilisation du système d'email.
    
    Crée deux utilisateurs (Tory et Ramy), envoie des emails,
    puis affiche, lit et supprime des emails.
    """
    
    # Création des utilisateurs
    tory = User('Tory')
    ramy = User('Ramy')
    
    # Tory envoie un email à Ramy
    tory.send_email(ramy, 'Hello', 'Hi Ramy, just saying hello!')
    
    # Ramy répond à Tory
    ramy.send_email(tory, 'Re: Hello', 'Hi Tory, hope you are fine.')
    
    # Tory envoie un autre email à Ramy
    tory.send_email(ramy, "Hello", "Hi Ramy, just saying hello!")
    
    # Ramy répond à nouveau
    ramy.send_email(tory, "Re: Hello", "Hi Tory, hope you are fine.")
    
    # Ramy consulte sa boîte de réception
    ramy.check_inbox()
    
    # Ramy lit le premier email
    ramy.read_email(1)
    
    # Ramy supprime le premier email
    ramy.delete_email(1)
    
    # Ramy consulte à nouveau sa boîte (l'email supprimé n'apparaît plus)
    ramy.check_inbox()


# ============================================
# POINT D'ENTRÉE DU PROGRAMME
# ============================================

if __name__ == '__main__':
    main()

# ============================================
# EXEMPLE DE SORTIE ATTENDUE :
# ============================================
#
# Email sent from Tory to Ramy!
# Email sent from Ramy to Tory!
# Email sent from Tory to Ramy!
# Email sent from Ramy to Tory!
#
# Ramy's Inbox:
# Your Emails:
# 1. [Unread] From: Tory | Subject: Hello | Time: 2024-01-15 14:30
# 2. [Unread] From: Ramy | Subject: Re: Hello | Time: 2024-01-15 14:30
# 3. [Unread] From: Tory | Subject: Hello | Time: 2024-01-15 14:30
# 4. [Unread] From: Ramy | Subject: Re: Hello | Time: 2024-01-15 14:30
#
# --- Email ---
# From: Tory
# To: Ramy
# Subject: Hello
# Received: 2024-01-15 14:30
# Body: Hi Ramy, just saying hello!
# ------------
#
# Email deleted.
#
# Ramy's Inbox:
# Your Emails:
# 1. [Unread] From: Ramy | Subject: Re: Hello | Time: 2024-01-15 14:30
# 2. [Unread] From: Tory | Subject: Hello | Time: 2024-01-15 14:30
# 3. [Unread] From: Ramy | Subject: Re: Hello | Time: 2024-01-15 14:30
#
# ============================================
# RÉSUMÉ DE L'ARCHITECTURE :
# 1. Email : contient les données d'un message
# 2. Inbox : gère la collection d'emails
# 3. User : interface utilisateur pour les actions
# 4. Les emails sont marqués comme lus automatiquement à l'affichage
# 5. Interface 1-indexée pour la lisibilité humaine
# ============================================