from marshmallow import Schema, ValidationError, fields


class updatePositionInputSchema(Schema):
    id                = fields.Str(required=True, description="Position uuid")
    name                = fields.Str(required=False, description="Position name")
    description  = fields.Str(required=False, description="Position description")
    id_area = fields.UUID(required=False, description="Area uuid")
    active = fields.Bool(required=False, description="Position status")

    class Meta:
        ordered = True


class updatePositionInput:
    def create(body: updatePositionInputSchema):
        try:
            return updatePositionInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
