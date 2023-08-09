from marshmallow import Schema, ValidationError, fields


class updateVehicleInputSchema(Schema):
    id          = fields.UUID(required=True, description="Vehicle uuid")
    model       = fields.Str(required=False, description="Vehicle model")
    performance = fields.Str(required=False, description="Vehicle performance")
    active      = fields.Bool(required=False, description="Vehicle status")

    class Meta:
        ordered = True


class updateVehicleInput:
    def create(body: updateVehicleInputSchema):
        try:
            return updateVehicleInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)
