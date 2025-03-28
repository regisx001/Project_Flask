from werkzeug.security import generate_password_hash, check_password_hash
from .db import db


class User(db.Model):
    """
    Classe User représentant un utilisateur dans la base de données.

    Attributs:
        id (int): Identifiant unique de l'utilisateur (clé primaire).
        username (str): Nom d'utilisateur unique, obligatoire.
        email (str): Adresse e-mail unique, obligatoire.
        password_hash (str): Hash du mot de passe de l'utilisateur.
        name (str): Nom complet de l'utilisateur.

    Méthodes:
        set_password(password):
            Définit le hash du mot de passe pour l'utilisateur.
            Args:
                password (str): Le mot de passe en clair.

        check_password(password):
            Vérifie si le mot de passe fourni correspond au hash enregistré.
            Args:
                password (str): Le mot de passe en clair.
            Returns:
                bool: True si le mot de passe correspond, False sinon.

        __repr__():
            Retourne une représentation lisible de l'objet User.
            Returns:
                str: Représentation sous forme de chaîne de caractères.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(100))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'
