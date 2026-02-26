from flask import Flask
from extensions import db, jwt

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
    app.config["JWT_SECRET_KEY"] = "super-secret-key"

    db.init_app(app)
    jwt.init_app(app)

    from routes.user_routes import user_bp
    from routes.auth_routes import auth_bp

    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    # RUN ONCE WHEN APP STARTS
    with app.app_context():
        db.create_all()

        # load users from JSON only first time
        from utils.load_user import load_users_from_json
        load_users_from_json()

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)