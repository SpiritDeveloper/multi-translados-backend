from marshmallow import Schema, ValidationError, fields


class deleteVehicleInputSchema(Schema):
    id = fields.UUID(required=True, description="Vehicle uuid")


    class Meta:
        ordered = True


class deleteVehicleInput:
    def create(body: deleteVehicleInputSchema):
        try:
            return deleteVehicleInputSchema().load(body)
        except ValidationError as err:
            raise Exception(err)