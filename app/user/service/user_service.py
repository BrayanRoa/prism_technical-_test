from app.db import db
from sqlalchemy.exc import NoResultFound
from marshmallow import ValidationError
from datetime import date
from ..entity.user_entity import UserEntity
from ..entity.bill_entity import BillEntity
from ..schema.user_schema import user_schema
from ..schema.bill_schema import bill_schema
from ..model.bill_dto import BillDTO
from ..model.user_dto import UserDTO

BillEntity.start_mapper()
UserEntity.start_mapper()

def register_user(data):
    try:
        db.session.add(UserDTO(
            email=data["email"],
            usernama=data["username"],
            passw=data["password"]
        ))
        db.session.commit()
        return {"msg":"user created successfully"}, 201
    except Exception as e:
        return {"error":e.args}

def get_all_bills_of_user(username):
    user = db.session.query(UserEntity).filter(UserEntity.username == username).all()
    if len(user) == 1:
        result = user_schema.dump(user[0])
        return result
    return {"error":f"there is no person with username {username}", "code":404}


def save_bill_of_user(user, data):
    try:
        info_user = get_all_bills_of_user(user)
        if "code" in info_user:
            return {"error":f"there is no person with username {user}"}, 404
        bill = bill_schema.load(data)
        bill_dto = BillDTO(
                id=None,
                type=bill["type"],
                value=bill["value"],
                observation=bill["observation"],
                date_bill=date.today(),
                user_id=info_user["id"]
            )
        db.session.add(bill_dto)
        db.session.commit()
        info_bill = bill_schema.dump(bill_dto)
        return {
            "type":info_bill["type"],
            "observation":info_bill["observation"],
            "value":info_bill["value"],
            "user":user,
            "id":info_bill["id"],
            "date":date.today()
        }, 201
    except ValidationError as e:
        return {"msg":e.messages},400
    except Exception as e:
        return {"error":e.args}, 400
    
    
def get_bill_id_of_user(user, bill_id, request):
    try:
        info_user = get_all_bills_of_user(user)
        if "code" in info_user:
            return {"error":f"there is no person with username {user}"}, 404
        bill = (
            db.session.query(BillEntity)
            .filter(BillEntity.user_id == info_user["id"], BillEntity.id == bill_id)
            .one()
        )
        if request == "DELETE":
            db.session.delete(bill)
            db.session.commit()
            return get_all_bills_of_user(user)
        return bill_schema.dump(bill)
    except NoResultFound:
        return {"msg": "check the bill's id or username"}, 404