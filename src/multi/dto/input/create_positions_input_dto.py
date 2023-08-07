from marshmallow import Schema, ValidationError, fields


class createPositionInputSchema(Schema):
    name                = fields.Str(required=True, description="Position name")
    description  = fields.Str(required=True, description="Position description")
    id_area = fields.UUID(required=True, description="Area uuid")

    class Meta:
        ordered = True


class createPositionsInput:
    def create(body: createPositionInputSchema):
        try:
            return createPositionInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
