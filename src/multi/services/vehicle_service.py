from ..dto import createVehicleInputSchema
from ..model import Vehicles
from ..exceptions.vehicle_exceptions import VehicleException
from ..utils.validate_attribute import validateAttribute
from datetime import datetime

class VehicleService:
  def create(body: createVehicleInputSchema):
    new_vehicle = Vehicles.save(**body)

    if not new_vehicle:
      VehicleException.notCreated()

    vehicle = Vehicles.find_one( id = new_vehicle.id )

    response = {}
    response['success'] = True
    response['message'] = 'vehicle successfully created'
    response['payload'] = vehicle.__dict__

    return response