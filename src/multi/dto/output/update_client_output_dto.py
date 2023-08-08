from marshmallow import Schema, ValidationError, fields
from .client_schema_output_dto import clientSchema

class updateClientOutputSchema(Schema):
    success                = fields.Boolean(required=True, description="True if action is correctly")
    message  = fields.Str(required=True, description="Message action")
    payload = fields.Nested(clientSchema())

    class Meta:
        ordered = True


class updateClientOutput:
    def create(body: updateClientOutputSchema):
        try:
            return updateClientOutputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)