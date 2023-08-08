from marshmallow import Schema, ValidationError, fields
from .client_schema_output_dto import clientSchema


class getAllClientOutputSchema(Schema):
    success                = fields.Boolean(required=True, description="True if action is correctly")
    message  = fields.Str(required=True, description="Message action")
    payload = fields.List(fields.Nested(clientSchema))

    class Meta:
        ordered = True


class getAllClientOutput:
    def create(body: getAllClientOutputSchema):
        try:
            return getAllClientOutputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
