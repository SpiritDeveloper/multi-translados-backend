from marshmallow import Schema, ValidationError, fields
from .client_schema_output_dto import clientSchema

class createClientOutputSchema(Schema):
    success = fields.Boolean(required=True, description="True if action is correctly")
    message = fields.Str(required=True, description="Message action")
    payload = fields.Nested(clientSchema())

    class Meta:
        ordered = True


class createClientOutput:
    def create(body: createClientOutputSchema):
        try:
            return createClientOutputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
