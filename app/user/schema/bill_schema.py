from app.ext import ma
from marshmallow import fields, validate

class BillSchema(ma.Schema):
    
    id = fields.Integer()
    date_bill = fields.Date()
    value = fields.Decimal(required=True)
    type = fields.Integer(required=True, validate=validate.OneOf([1,2]))
    observation = fields.String(required=True)
    
    user_id = fields.Integer()
    
bill_schema = BillSchema(exclude=("user_id",))
list_bill_schema = BillSchema(many=True)