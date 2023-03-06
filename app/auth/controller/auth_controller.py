from app.db import db
from flask import Blueprint, request
from sqlalchemy.exc import NoResultFound 
from ...user.entity.user_entity import UserEntity
from ...user.schema.user_schema import user_schema

auth = Blueprint("auth", __name__)

@auth.route("/", methods=["POST"])
def login():
    """Login del user
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
            passw:
              type: string
                
    responses:
      200:
        description: Login del user
        schema:
          $ref: '#/definitions/UserInfo'
    """
    try:
        data = request.get_json()
        user = (db.session.query(UserEntity)
                .filter(
                    UserEntity.username == data["username"],
                    UserEntity.passw == data["passw"])
                ).one()
        result = user_schema.dump(user)
        return {
            "login":True,
            "username":result["username"],
            "email":result["email"],
            "mensaje":"Welcome"}
    except NoResultFound:
        return {"login":False, "mensaje":"Usuario o contraseña invalido"}
    except Exception as e:
        return {"error":e.args}