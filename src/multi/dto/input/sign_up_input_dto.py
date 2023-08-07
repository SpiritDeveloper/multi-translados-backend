from marshmallow import Schema, ValidationError, fields


class singUpInputSchema(Schema):
    name                = fields.Str(required=True, description="User name")
    paternal_last_name  = fields.Str(required=True, description="User paternal lastname")
    maternal_last_name  = fields.Str(required=True, description="User maternal lastname")
    email               = fields.Email(required=True, description="User email")
    password            = fields.Str(required=True, description="User password")
    id_position         = fields.UUID(required=True, description="User positionId")
    profile_photo = fields.Str(required=False, description="User URL photo perfile", missing='') 

    class Meta:
        ordered = True


class signUpInput:
    def create(body: singUpInputSchema):
        try:
            return singUpInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
