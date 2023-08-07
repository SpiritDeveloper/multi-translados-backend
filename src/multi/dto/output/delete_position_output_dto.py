from marshmallow import Schema, ValidationError, fields


class deleteRecordSchema(Schema):
    id = fields.UUID()

class deletePositionOutputSchema(Schema):
    success                = fields.Boolean(required=True, description="True if action is correctly")
    message  = fields.Str(required=True, description="Message action")
    payload = fields.Nested(deleteRecordSchema())

    class Meta:
        ordered = True


class deletePositionOutput:
    def create(body: deletePositionOutputSchema):
        try:
            return deletePositionOutputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
