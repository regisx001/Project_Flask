from datetime import timedelta


class Config:
    """
    Classe Config:
    Cette classe contient les configurations de l'application.

    Attributs:
    -----------
    - SECRET_KEY : str
        Clé secrète utilisée pour sécuriser les sessions et autres fonctionnalités.
    - SQLALCHEMY_DATABASE_URI : str
        URI de la base de données utilisée par SQLAlchemy.
    - SQLALCHEMY_TRACK_MODIFICATIONS : bool
        Désactive le suivi des modifications pour économiser les ressources.
    - SESSION_SQLALCHEMY_TABLE : str
        Nom de la table utilisée pour stocker les sessions.
    - SESSION_TYPE : str
        Type de session utilisé (ici, 'sqlalchemy').
    - SESSION_PERMANENT : bool
        Indique si les sessions sont permanentes.
    - PERMANENT_SESSION_LIFETIME : timedelta
        Durée de vie des sessions permanentes (1 heure par défaut).
    """

    SECRET_KEY = "your-secret-key-here"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_SQLALCHEMY_TABLE = 'sessions'
    SESSION_TYPE = 'sqlalchemy'
    SESSION_PERMANENT = True
    PERMANENT_SESSION_LIFETIME = timedelta(hours=1)
