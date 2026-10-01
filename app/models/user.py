from tortoise import fields
from app.models.base import BaseModel
class user(BaseModel):
    email = fields.CharField(max_length = 255, unique = True)
    password_hash = fields.CharField(max_length = 255)
    phone_number = fields.CharField(max_length = 10, unique = True)
    name = fields.CharField(max_length = 100, )
    balance = fields.DecimalField(max_digits=10, decimal_places=2, default = 0)
    role = fields.CharField(max_length = 20)
    is_active = fields.BooleanField(default = True)
    is_verified = fields.BooleanField(default = False)

    class Meta:
        table = "users"

    
