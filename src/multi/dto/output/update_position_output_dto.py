from marshmallow import Schema, ValidationError, fields
from .position_schema_output_dto import positionSchema

class updatePositionOutputSchema(Schema):
    success                = fields.Boolean(required=True, description="True if action is correctly")
    message  = fields.Str(required=True, description="Message action")
    payload = fields.Nested(positionSchema())

    class Meta:
        ordered = True


class updatePositionOutput:
    def create(body: updatePositionOutputSchema):
        try:
            return updatePositionOutputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
