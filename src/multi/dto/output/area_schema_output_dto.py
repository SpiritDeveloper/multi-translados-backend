from marshmallow import Schema, fields


class areaSchema(Schema):
    id                = fields.UUID(required=True, description="UUID of area")
    name                = fields.Str(required=True, description="Name of area")
    description  = fields.Str(required=True, description="Description of area")
    active  = fields.Boolean(required=True, description="Status record")

    class Meta:
        ordered = True