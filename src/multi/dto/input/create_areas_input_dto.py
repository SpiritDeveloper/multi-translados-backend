from marshmallow import Schema, ValidationError, fields


class createAreasInputSchema(Schema):
    name                = fields.Str(required=True, description="Area name")
    description  = fields.Str(required=True, description="Area description")

    class Meta:
        ordered = True


class createAreasInput:
    def create(body: createAreasInputSchema):
        try:
            return createAreasInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
