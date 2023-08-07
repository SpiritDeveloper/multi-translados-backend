from marshmallow import Schema, fields, EXCLUDE


class positionSchema(Schema):
    id                = fields.UUID(required=True, description="UUID of position")
    name                = fields.Str(required=True, description="Name of position")
    description  = fields.Str(required=True, description="Description of position")
    id_area                = fields.UUID(required=True, description="UUID of area")
    active  = fields.Boolean(required=True, description="Status record")

    class Meta:
        ordered = True
        unknown = EXCLUDE