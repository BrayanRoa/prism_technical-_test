from app.db import db
from sqlalchemy.exc import NoResultFound
from marshmallow import ValidationError
from datetime import date
from ..entity.user_entity import UserEntity
from ..entity.bill_entity import BillEntity
from ..schema.user_schema import user_schema
from ..schema.bill_schema import bill_schema
from ..model.bill_dto import BillDTO

BillEntity.start_mapper()


def get_all_bills_of_user(username):
    try:
        user = db.session.query(UserEntity).filter(UserEntity.username == username).one()
        result = user_schema.dump(user)
        return result
    except NoResultFound:
        raise ValueError(f"there is no person with username {username}")

def save_bill_of_user(user, data):
    try:
        info_user = get_all_bills_of_user(user)
        bill = bill_schema.load(data)
        db.session.add(
            BillDTO(
                type=bill["type"],
                value=bill["value"],
                observation=bill["observation"],
                date_bill=date.today(),
                user_id=info_user["id"]
            )
        )
        db.session.commit()
        return {
            "type":bill["type"],
            "observation":bill["observation"],
            "value":bill["value"],
            "user":user,
            "id":info_user["id"],
            "date":date.today()
        }, 201
    except ValidationError as e:
        return {"msg":e.messages},400
    except Exception as e:
        return {"error":e.args}, 400
    
    
def get_bill_id_of_user(user, bill_id, request):
    try:
        info_user = get_all_bills_of_user(user)
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
    except Exception as error:
        return {"error": error.args}, 400