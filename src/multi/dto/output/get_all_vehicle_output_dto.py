from marshmallow import Schema, ValidationError, fields
from .vehicle_schema_output_dto import vehicleSchema


class getAllVehicleOutputSchema(Schema):
    success = fields.Boolean(required=True, description="True if action is correctly")
    message = fields.Str(required=True, description="Message action")
    payload = fields.List(fields.Nested(vehicleSchema))

    class Meta:
        ordered = True


class getAllVehicleOutput:
    def create(body: getAllVehicleOutputSchema):
        try:
            return getAllVehicleOutputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
