"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Favorites
from api.utils import generate_sitemap, APIException

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/user', methods=['POST'])
def user_create():
    data=request.json
    new_user=User(email=data["email"], password=data["password"], is_active=True)
    User.query.filter_by(email=data["email"]).first()
    if new_user is not None:
        return jsonify({
            "msg": "Email registrado"

        }), 401
    print(new_user)
    db.session.add(new_user)
    db.session.commit()
    print(new_user.serialize())
    return "ok"

@api.route('/user/<int:user_id>', methods=['GET'])
def user_get(user_id):
    user=User.query.get(user_id)
    if (user is None):
        return "Usuario no registrado", 404
    return (user.serialize())

@api.route('/favorites/<string:element>/<int:element_id>', methods=['POST'])
def favorite_planet_create(element, element_id):
    user_id=request.get_json()["user_id"]
    new_Favorite=Favorites(type=element, element_id=element_id, user_id=user_id)
    db.session.add(new_Favorite)
    db.session.commit()
    return jsonify({"msg": "Favorite created"}), 201

@api.route('/favorites/<string:element>/<int:element_id>', methods=['DELETE'])
def favorite_planet_delete(element, element_id):
    user_id=request.get_json()["user_id"]
    new_Favorite=Favorites.quey.filter_by(type=element, element_id=element_id, user_id=user_id).first()
    if(favorite is None):
        return jsonify({"msg": "Favorite not found"}), 404

    db.session.delete(favorite)
    db.session.commit()
    return jsonify({"msg": "Favorite created"}), 201
