from marshmallow import Schema, fields, ValidationError


class tokenSchema(Schema):
    token = fields.String(
        required=True, description="Token sent in the header to other services"
    )


class signInOutputSchema(Schema):
    success = fields.Boolean(
        required=True, description="If this field is true, the operation is correctly"
    )
    message = fields.String(required=True, description="Message action")
    payload = fields.Nested(
        tokenSchema(), required=True, description="Payload response"
    )

    class Meta:
        ordered = True


class signInOutput:
    def create(input: signInOutputSchema):
        try:
            return signInOutputSchema().load(input)
        except ValidationError as err:
            raise Exception(err)
