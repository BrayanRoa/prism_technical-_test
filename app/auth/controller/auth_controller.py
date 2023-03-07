from app.db import db
from flask import Blueprint, request, jsonify
from ...user.entity.user_entity import UserEntity
from ...user.schema.user_schema import user_schema
from flask_jwt_extended import create_access_token

auth = Blueprint("auth", __name__)

@auth.route("/", methods=["POST"])
def login():
    """Login of user
    ---
    tags: 
        - Login
        
    parameters:
      - name: body
        in: body
        required: tru 
        schema:
          $ref: '#/definitions/UserInfo' 
            
    definitions:
        UserInfo:
          type: object
          properties:
            username:
              type: string
            password:
              type: string
                
    responses:
      200:
        description: Login successfully
        schema:
          $ref: '#/definitions/UserInfo'
    """
    try:
      data = (
        db.session.query(UserEntity)
        .filter(UserEntity.username == request.json["username"])
        .one())
      if not UserEntity.check_password(data.passw, request.json["password"]):
        return {"login":False, "message":"invalid username or password"}
      result = user_schema.dump(data)
      return {
        "login":True, 
        "access-token":"Bearer " + create_access_token(identity=result["email"])
      }
    except Exception as e:
      return jsonify({"error":e.args})