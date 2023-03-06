from flask import Blueprint, request
from ..service.user_service import (
    get_all_bills_of_user,
    save_bill_of_user,
    get_bill_id_of_user
)

user = Blueprint("user", __name__)

@user.route("/<user>/bills", methods=["GET"])
def getAll(user):
    try:
        return get_all_bills_of_user(user)
    except Exception as e   :
        return {"msg":e.args}

@user.route("/<user>/bills", methods=["POST"])
def saveBill(user):
    data = request.get_json()
    return save_bill_of_user(user, data)


@user.route("/<user>/bills/<bill_id>", methods=["GET", "DELETE"])
def getOneBill(user, bill_id):
    return get_bill_id_of_user(user, bill_id, request.method)