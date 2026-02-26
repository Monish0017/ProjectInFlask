from flask import Blueprint, request, jsonify
from models import User
from utils.password_utils import verify_password
from utils.jwt_utils import generate_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(force=True)

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    if not verify_password(password, user.password):
        return jsonify({"error": "Wrong password"}), 401

    token = generate_token(user.id)

    return jsonify({
        "message": "Login successful",
        "access_token": token,
        "user_id": user.id
    }), 200