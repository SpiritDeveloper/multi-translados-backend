from marshmallow import Schema, ValidationError, fields
from .client_schema_output_dto import clientSchema

class deleteClientOutputSchema(Schema):
    success = fields.Boolean(required=True, description="True if action is correctly")
    message = fields.Str(required=True, description="Message action")
    payload = fields.Nested(clientSchema())

    class Meta:
        ordered = True


class deleteClientOutput:
    def create(body: deleteClientOutputSchema):
        try:
            return deleteClientOutputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
