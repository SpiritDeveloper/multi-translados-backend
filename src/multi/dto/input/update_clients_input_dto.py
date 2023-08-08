from marshmallow import Schema, ValidationError, fields


class updateClientInputSchema(Schema):
    id              = fields.UUID(required=True, description="Client uuid")
    code            = fields.Str(required=False, description="Client code")
    business_name   = fields.Str(required=False, description="Client business name")
    rfc             = fields.Str(required=False, description="Client RFC")
    street_name     = fields.Str(required=False, description="Client street name")
    phone_number    = fields.Str(required=False, description="Client phone number")
    interior_number = fields.Str(required=False, description="Client interior number")
    exterior_number = fields.Str(required=False, description="Client exterior number")
    neighborhood    = fields.Str(required=False, description="Client neighborhood")
    state           = fields.Str(required=False, description="Client state")
    zip_code        = fields.Str(required=False, description="Client zip code")
    logo            = fields.Str(required=False, description="Client logo")
    active          = fields.Bool(required=False, description="Client status")

    class Meta:
        ordered = True


class updateClientInput:
    def create(body: updateClientInputSchema):
        try:
            return updateClientInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
