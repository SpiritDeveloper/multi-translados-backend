from marshmallow import Schema, ValidationError, fields


class updateRecordAreaSchema(Schema):
    id = fields.UUID()

class updateAreaOutputSchema(Schema):
    success                = fields.Boolean(required=True, description="True if action is correctly")
    message  = fields.Str(required=True, description="Message action")
    payload = fields.Nested(updateRecordAreaSchema())

    class Meta:
        ordered = True


class updateAreaOutput:
    def create(body: updateAreaOutputSchema):
        try:
            return updateAreaOutputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
