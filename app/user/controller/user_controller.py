from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, verify_jwt_in_request
from ..service.user_service import (
    get_all_bills_of_user,
    save_bill_of_user,
    get_bill_id_of_user,
    register_user
)

user = Blueprint("user", __name__)


@user.route("/register", methods=["POST"])
def register():
    """Register user
    --- 
    tags: 
        - User
        
    parameters:
      - name: body
        in: body
        required: true
        schema:
          $ref: '#/definitions/userAccess'  
        
    definitions:
        userAccess:
          type: object
          properties:
            username:
              type: string
            password:
              type: string
            email:
              type: string
                
    responses:
      200:
        description: Register user
        
    """
    data = request.get_json()
    return register_user(data)

@user.route("/<user>/bills", methods=["GET"])
@jwt_required()
def getAll(user):
    """Get all bills of a user
    --- 
    tags: 
        - User
        
    parameters:
      - name: user
        in: path
        type: string
        required: true
        description: username de la persona 
        
    definitions:
        User:
          type: object
          properties:
            email:
              type: string
            id:
              type: number
            username:
              type: string
            bills:
              type: object
              properties:
                date_bill: 
                  type: date
                id: 
                  type: number
                observation:
                  type: string
                type:
                  type: number
                value:
                  type: number
                
    responses:
      200:
        description: get all bills of a user
    """
    try:
        return get_all_bills_of_user(user)
    except Exception as e:
        return {"msg":e.args}

@user.route("/<user>/bills", methods=["POST"])
@jwt_required()
def saveBill(user):
    """Registration of an entry or exit of the user
    --- 
    tags: 
        - User
        
    parameters:
      - name: user
        in: path
        type: string
        required: true
        description: username
      - name: body
        in: body
        required: tru 
        schema:
          $ref: '#/definitions/BillInfo'  
        
    definitions:
        BillInfo:
          type: object
          properties:
            type:
              type: number
            value:
              type: number
            observation:
              type: string
                
    responses:
      201:
        description: Registration of an entry or exit of the user 
        
    """
    data = request.get_json()
    return save_bill_of_user(user, data)


@user.route("/<user>/bills/<bill_id>", methods=["GET"])
@jwt_required()
def getOneBill(user, bill_id):
    """get a bill from a user
    ---
    tags: 
        - User
        
    parameters:
      - name: user
        in: path
        type: string
        required: true
        description: person's username
      - name: bill_id
        in: path
        type: string
        required: true
        description: bill's id
            
    definitions:
        VerBill:
          type: object
          properties:
            date_bill: 
              type: date
            id: 
              type: number
            observation:
              type: string
            type:
              type: number
            value:
              type: number
                
    responses:
      200:
        description: get a bill from a user
        schema:
          $ref: '#/definitions/VerBill'
    """
    return get_bill_id_of_user(user, bill_id, request.method)


@user.route("/<user>/bills/<bill_id>", methods=["DELETE"])
@jwt_required()
def deleteOneBill(user, bill_id):
    """Remove a bill from the user
    --- 
    tags: 
        - User
        
    parameters:
      - name: user
        in: path
        type: string
        required: true
        description: person's username
      - name: bill_id
        in: path
        type: string
        required: true
        description: bill's id
        
    definitions:
        BillInfo:
          type: object
          properties:
            type:
              type: number
            value:
              type: number
            observation:
              type: string
                
    responses:
      200:
        description: bill removed
        
    """
    return get_bill_id_of_user(user, bill_id, request.method)