from flask import Blueprint, request, jsonify
from models import User
from extensions import db
from flask_jwt_extended import jwt_required , get_jwt_identity
from sqlalchemy import func
from utils.password_utils import hash_password

user_bp = Blueprint("users", __name__)

# Function used to convert the SQL Alchemy to Dict
def user_to_dict(user):
    return {
        "id": user.id,
        "firstName": user.firstName,
        "lastName": user.lastName,
        "email": user.email,
        "age": user.age,
        "city": user.city,
        "state": user.state,
        "country": user.country,
        "zip": user.zip,
        "company": user.company,
        "web": user.web
    }

@user_bp.route("", methods=["GET"])
def get_users():
    page = request.args.get("page")
    limit = request.args.get("limit")
    search = request.args.get("search")
    sort = request.args.get("sort")

    query = User.query

    if search:
        query = query.filter(
            (User.firstName.ilike(f"%{search}%")) |
            (User.lastName.ilike(f"%{search}%"))
        )

    if sort:
        if sort.startswith("-"):
            query = query.order_by(getattr(User, sort[1:]).desc())
        else:
            query = query.order_by(getattr(User, sort))

    if page is not None and limit is not None:
        page = int(page)
        limit = int(limit)

        users = query.paginate(page=page, per_page=limit)

        return jsonify({
            "page": page,
            "per_page": limit,
            "total": users.total,
            "users": [u.firstName for u in users.items]
        })

    users = query.all()

    # from dict convert to JSON
    return jsonify([user_to_dict(u) for u in users])


@user_bp.route("", methods=["POST"])
def create_user():

    # Here force to get data as json . Because I got 415 which is media unsupported error
    data = request.get_json(force=True)

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    from utils.password_utils import hash_password
    data["password"] = hash_password(data["password"])

    user = User(**data)
    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "User created"}), 201


@user_bp.route("/id" , methods=["GET"])
@jwt_required()
def get_user():
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)
    return jsonify(user_to_dict(user))


@user_bp.route("/update", methods=["PUT"])
@jwt_required()
def update_user(id):
    user_id = get_jwt_identity()
    user = User.query.get_or_404(user_id)

    data = request.get_json(force=True)

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    if "password" in data:
        from utils.password_utils import hash_password
        data["password"] = hash_password(data["password"])

    for key, value in data.items():
        setattr(user, key, value)

    db.session.commit()
    return jsonify({"message": "User fully updated"})


# Uses jwt_token to retrieve id . Then using that patch the body to db
@user_bp.route("/partial_update", methods=["PATCH"])
@jwt_required()
def patch_user(id):
    user_id = get_jwt_identity() # Get the id from token , using the global secret we declared in app.py
    user = User.query.get_or_404(user_id)
    data = request.get_json(force=True)

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    if "password" in data:
        from utils.password_utils import hash_password
        data["password"] = hash_password(data["password"])

    for key, value in data.items():
        setattr(user, key, value)

    db.session.commit()
    return jsonify({"message": "User partially updated"})

@user_bp.route("/<int:id>", methods=["DELETE"])
def delete_user(id):
    # get_or_404 , get or else throw a status code of 404 which is user not found   
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"msg": "Deleted"})

@user_bp.route("/summary", methods=["GET"])
def summary():
    avg_age = db.session.query(func.avg(User.age)).scalar()
    city_count = db.session.query(User.city, func.count(User.id))\
                    .group_by(User.city).all()

    return jsonify({
        "average_age": avg_age,
        "users_by_city": dict(city_count)
    })