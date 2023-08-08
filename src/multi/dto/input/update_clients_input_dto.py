from marshmallow import Schema, ValidationError, fields


class updateClientInputSchema(Schema):
    id                = fields.UUID(required=True, description="Client uuid") 
    name                = fields.Str(required=False, description="Client name")
    description  = fields.Str(required=False, description="Client description")
    active  = fields.Bool(required=False, description="Client status")

    class Meta:
        ordered = True


class updateClientInput:
    def create(body: updateClientInputSchema):
        try:
            return updateClientInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
