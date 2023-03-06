from app.ext import ma
from marshmallow import fields

class UserSchema(ma.Schema):
    
    id = fields.Integer()
    username = fields.String()
    passw = fields.String()
    email = fields.String()
    
    bill = fields.Nested("BillSchema" ,many=True, exclude=("user_id",))
    
user_schema = UserSchema(exclude=("passw",))
user_schema_without_info_person = UserSchema(only=("bill",))
list_user_schema = UserSchema(many=True)
    