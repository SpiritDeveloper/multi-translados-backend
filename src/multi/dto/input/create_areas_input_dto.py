from marshmallow import Schema, ValidationError, fields


class createAreaInputSchema(Schema):
    name                = fields.Str(required=True, description="Area name")
    description  = fields.Str(required=True, description="Area description")

    class Meta:
        ordered = True


class createAreaInput:
    def create(body: createAreaInputSchema):
        try:
            return createAreaInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
