from marshmallow import Schema, ValidationError, fields
from .vehicle_schema_output_dto import vehicleSchema

class createVehicleOutputSchema(Schema):
  success = fields.Boolean(required=True, description="True if action is correctly")
  message = fields.Str(required=True, description="Message action")
  payload = fields.Nested(vehicleSchema())

  class Meta:
    ordered = True


class createVehicleOutput:
  def create(body: createVehicleOutputSchema):
    try:
      return createVehicleOutputSchema().load(body)
    except ValidationError as err:
      raise Exception(err)