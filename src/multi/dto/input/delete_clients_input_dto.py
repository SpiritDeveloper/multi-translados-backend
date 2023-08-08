from marshmallow import Schema, ValidationError, fields


class deleteClientInputSchema(Schema):
    id = fields.UUID(required=True, description="Client uuid")


    class Meta:
        ordered = True


class deleteClientInput:
    def create(body: deleteClientInputSchema):
        try:
            return deleteClientInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
