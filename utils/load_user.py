import json
from models import User
from extensions import db
from utils.password_utils import hash_password

def load_users_from_json():
    # If DB already has users → don't insert again
    if User.query.first():
        print("Users already exist. Skipping JSON load.")
        return

    try:
        with open("users.json") as f:
            users = json.load(f)

        for u in users:
            user = User(
                firstName=u["firstName"],
                lastName=u["lastName"],
                email=u["email"],
                password=hash_password(u["password"]),
                age=u["age"],
                city=u["city"],
                state=u["state"],
                country=u["country"],
                zip=u["zip"],
                company=u.get("company"),
                web=u.get("web")
            )
            db.session.add(user)

        db.session.commit()
        print("Users loaded from JSON successfully!")

    except FileNotFoundError:
        print("users.json file not found.")