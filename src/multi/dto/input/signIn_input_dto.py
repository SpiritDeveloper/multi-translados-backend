from marshmallow import Schema, ValidationError, fields


class singInInputSchema(Schema):
    email = fields.Email(required=True, description="User email")
    password = fields.String(required=True, description="User password")

    class Meta:
        ordered = True


class signInInput:
    def create(body: singInInputSchema):
        try:
            return singInInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
