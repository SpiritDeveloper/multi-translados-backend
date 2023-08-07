from marshmallow import Schema, ValidationError, fields


class updateAreaInputSchema(Schema):
    id                = fields.Str(required=True, description="Area uuid") 
    name                = fields.Str(required=False, description="Area name")
    description  = fields.Str(required=False, description="Area description")
    active  = fields.Bool(required=False, description="Area status")

    class Meta:
        ordered = True


class updateAreaInput:
    def create(body: updateAreaInputSchema):
        try:
            return updateAreaInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
