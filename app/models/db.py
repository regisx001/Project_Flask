from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    """
    Initialise la base de données avec l'application Flask donnée.

    Args:
        app (Flask): L'instance de l'application Flask.

    Fonctionnement:
        - Initialise la base de données avec l'application Flask via `db.init_app(app)`.
        - Crée le contexte de l'application avec `app.app_context()`.
        - Crée toutes les tables définies dans les modèles avec `db.create_all()`.
    """
    db.init_app(app)
    with app.app_context():
        db.create_all()
