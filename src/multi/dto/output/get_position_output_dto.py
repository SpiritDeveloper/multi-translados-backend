from marshmallow import Schema, ValidationError, fields
from .position_schema_output_dto import positionSchema


class getPositionOutputSchema(Schema):
    success                = fields.Boolean(required=True, description="True if action is correctly")
    message  = fields.Str(required=True, description="Message action")
    payload = fields.Nested(positionSchema())

    class Meta:
        ordered = True


class getPositionOutput:
    def create(body: getPositionOutputSchema):
        try:
            return getPositionOutputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
