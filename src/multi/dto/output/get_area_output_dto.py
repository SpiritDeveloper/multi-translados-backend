from marshmallow import Schema, ValidationError, fields
from .area_schema_output_dto import areaSchema


class getAreaOutputSchema(Schema):
    success                = fields.Boolean(required=True, description="True if action is correctly")
    message  = fields.Str(required=True, description="Message action")
    payload = fields.Nested(areaSchema())

    class Meta:
        ordered = True


class getAreaOutput:
    def create(body: getAreaOutputSchema):
        try:
            return getAreaOutputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
