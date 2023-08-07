from marshmallow import Schema, fields, ValidationError
from .user_schema_output_dto import userSchema


class signUpOutputSchema(Schema):
    success = fields.Boolean(
        required=True, description="If this field is true, the operation is correctly"
    )
    message = fields.String(required=True, description="Message action")
    payload = fields.Nested(userSchema())

    class Meta:
        ordered = True


class signUpOutput:
    def create(input: signUpOutputSchema):
        try:
            return signUpOutputSchema().load(input)
        except ValidationError as err:
            raise Exception(err)
