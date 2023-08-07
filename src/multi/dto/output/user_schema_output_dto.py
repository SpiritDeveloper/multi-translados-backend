from marshmallow import Schema, fields, EXCLUDE


class userSchema(Schema):
    id                = fields.UUID(required=True, description="UUID of user")
    name                = fields.Str(required=True, description="Name of user")
    paternal_last_name  = fields.Str(required=True, description="Paternal lastname of user")
    maternal_last_name  = fields.Str(required=True, description="Maternal lastname of user")
    email  = fields.Str(required=True, description="Email or user")
    id_position  = fields.UUID(required=True, description="Position UUID of user")
    profile_photo  = fields.Str(required=True, description="Url phone perfil")
    active  = fields.Boolean(required=True, description="Status record")

    class Meta:
        ordered = True
        unknown = EXCLUDE