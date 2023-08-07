from marshmallow import Schema, ValidationError, fields
from .position_schema_output_dto import positionSchema


class getAllPositionOutputSchema(Schema):
    success                = fields.Boolean(required=True, description="True if action is correctly")
    message  = fields.Str(required=True, description="Message action")
    payload = fields.List(fields.Nested(positionSchema))

    class Meta:
        ordered = True


class getAllPositionOutput:
    def create(body: getAllPositionOutputSchema):
        try:
            return getAllPositionOutputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
