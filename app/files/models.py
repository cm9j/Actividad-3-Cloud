from tortoise import fields
from tortoise.models import Model


class File(Model):
    id = fields.IntField(pk=True)
    filename = fields.CharField(max_length=255)
    content_type = fields.CharField(max_length=100)
    path = fields.CharField(max_length=255)
    owner_id = fields.IntField()

    class Meta:
        table = "files"
