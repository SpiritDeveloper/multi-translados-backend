from marshmallow import Schema, ValidationError, fields


class updatePositionSchema(Schema):
    id                = fields.Str(required=True, description="Position uuid")
    name                = fields.Str(required=False, description="Position name")
    description  = fields.Str(required=False, description="Position description")
    title  = fields.Str(required=False, description="Position title")
    area_id = fields.UUID(required=False, description="Area uuid")

    class Meta:
        ordered = True


class updatePositionInput:
    def create(body: updatePositionSchema):
        try:
            return updatePositionSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
