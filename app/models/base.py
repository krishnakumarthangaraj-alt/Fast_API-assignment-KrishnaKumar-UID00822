import uuid
from tortoise.models import Model
from tortoise import fields
class BaseModel(Model):
    id =  fields.UUIDField(
        pk = True,
        default = uuid.uuid4
    )