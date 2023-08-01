from marshmallow import Schema, ValidationError, fields


class createPositionsInputSchema(Schema):
    name                = fields.Str(required=True, description="Position name")
    description  = fields.Str(required=True, description="Position description")
    title  = fields.Str(required=True, description="Position title")
    area_id = fields.UUID(required=True, description="Area uuid")

    class Meta:
        ordered = True


class createPositionsInput:
    def create(body: createPositionsInputSchema):
        try:
            return createPositionsInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
