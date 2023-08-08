from marshmallow import Schema, fields, EXCLUDE


class clientSchema(Schema):
    id                = fields.UUID(required=True, description="UUID of client")
    code              = fields.Str(required=True, description="Code of client")
    business_name     = fields.Str(required=True, description="Business name of client")
    rfc				  			= fields.Str(required=True, description="RFC of client")
    street_name       = fields.Str(required=True, description="Street name of client")
    phone_number      = fields.Str(required=True, description="phone number of client")
    interior_number   = fields.Str(required=True, description="Interior number of client")
    exterior_number   = fields.Str(required=True, description="Exterior number of client")
    neighborhood      = fields.Str(required=True, description="Neighborhood of client")
    state             = fields.Str(required=True, description="State of client")
    zip_code          = fields.Str(required=True, description="Zip code of client")
    logo              = fields.Str(required=True, description="Logo of client")
    active  = fields.Boolean(required=True, description="Status record")

    class Meta:
        ordered = True
        unknown = EXCLUDE