from marshmallow import Schema, ValidationError, fields


class deleteRecordSchema(Schema):
    id = fields.UUID()

class deleteAreaOutputSchema(Schema):
    success                = fields.Boolean(required=True, description="True if action is correctly")
    message  = fields.Str(required=True, description="Message action")
    payload = fields.Nested(deleteRecordSchema())

    class Meta:
        ordered = True


class deleteAreaOutput:
    def create(body: deleteAreaOutputSchema):
        try:
            return deleteAreaOutputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
