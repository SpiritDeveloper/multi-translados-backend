from marshmallow import Schema, ValidationError, fields

class createClientInputSchema(Schema):
  code            = fields.Str(required=True, description="Client code")
  business_name   = fields.Str(required=True, description="Client business name")
  rfc             = fields.Str(required=True, description="Client RFC")
  street_name     = fields.Str(required=True, description="Client street name")
  phone_number    = fields.Str(required=True, description="Client phone number")
  interior_number = fields.Str(required=True, description="Client interior number")
  exterior_number = fields.Str(required=True, description="Client exterior number")
  neighborhood    = fields.Str(required=True, description="Client neighborhood")
  state           = fields.Str(required=True, description="Client state")
  zip_code        = fields.Str(required=True, description="Client zip code")
  logo            = fields.Str(required=True, description="Client logo")

  class Meta:
    ordered = True

class createClientInput:
  def create(body: createClientInputSchema):
    try:
      return createClientInputSchema().load(body)
    except ValidationError as err:
      raise Exception(err)