from tortoise.models imoprt Model
from app.models.base import BaseModel
class user(Model):
    id = fields.UUIDField(primary_key = True)
    email = fields.CharField(max_lenght = 255)
    password_hash = fields.CharField(max_lenght = 255)
    name = fields.CharField(max_lenght = 100)
    balance = fields.DecimalField(max_digits=10, decimal_places=2, default = 0)
    role = fields.CharField(max_lenght = 20)

