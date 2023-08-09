from marshmallow import Schema, fields, EXCLUDE

class vehicleSchema(Schema):
  id          = fields.UUID(required=True, description="UUID of vehicle")
  model       = fields.Str(required=True, description="Model of vehicle")
  performance = fields.Str(required=True, description="Fuel efficiency in kilometers per liter of vehicle")


  class Meta:
    ordered = True
    unknown = EXCLUDE