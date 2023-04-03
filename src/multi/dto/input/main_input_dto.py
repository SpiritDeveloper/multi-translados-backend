from marshmallow import Schema, ValidationError


class mainInputSchema(Schema):
    class Meta:
        ordered = True


class mainInput:
    def create(body: mainInputSchema):
        try:
            return mainInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
