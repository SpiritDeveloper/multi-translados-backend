from marshmallow import Schema, fields


class positionSchema(Schema):
    id                = fields.UUID(required=True, description="UUID of position")
    title                = fields.Str(required=True, description="Name of position")
    description  = fields.Str(required=True, description="Description of position")
    id_area                = fields.UUID(required=True, description="UUID of area")
    active  = fields.Boolean(required=True, description="Status record")

    class Meta:
        ordered = True