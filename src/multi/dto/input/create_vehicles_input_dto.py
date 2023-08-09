from marshmallow import Schema, ValidationError, fields

class createVehicleInputSchema(Schema):
  model       = fields.Str(required=True, description="Vehicle model")
  performance = fields.Str(required=True, description="Vehicle fuel efficiency in kilometers per liter")

  class Meta:
    ordered = True


class createVehicleInput:
  def create(body: createVehicleInputSchema):
    try:
      return createVehicleInputSchema().load(body)
    except ValidationError as err:
      raise Exception(err)