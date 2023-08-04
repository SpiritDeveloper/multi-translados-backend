from marshmallow import Schema, ValidationError, fields
from .area_schema_output_dto import areaSchema


class getAllAreaOutputSchema(Schema):
    success                = fields.Boolean(required=True, description="True if action is correctly")
    message  = fields.Str(required=True, description="Message action")
    payload = fields.List(fields.Nested(areaSchema))

    class Meta:
        ordered = True


class getAllAreaOutput:
    def create(body: getAllAreaOutputSchema):
        try:
            return getAllAreaOutputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
