from marshmallow import Schema, ValidationError, fields


class deleteAreaInputSchema(Schema):
    id = fields.UUID(required=True, description="Area uuid")


    class Meta:
        ordered = True


class deleteAreaInput:
    def create(body: deleteAreaInputSchema):
        try:
            return deleteAreaInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
