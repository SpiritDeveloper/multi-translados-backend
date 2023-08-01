from marshmallow import Schema, ValidationError, fields


class deletePositionInputSchema(Schema):
    id = fields.UUID(required=True, description="Position uuid")


    class Meta:
        ordered = True


class deletePositionInput:
    def create(body: deletePositionInputSchema):
        try:
            return deletePositionInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
