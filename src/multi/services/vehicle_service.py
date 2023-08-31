from ..dto import createVehicleInputSchema, updateVehicleInputSchema, deleteVehicleInputSchema
from ..model import Vehicles
from ..exceptions.vehicle_exceptions import VehicleException
from ..utils.validate_attribute import validateAttribute
from datetime import datetime

class VehicleService:
  def get(vehicleId : str):
    get_vehicle = Vehicles.find_one( id = vehicleId)
    if not get_vehicle:
      VehicleException.notFound()

    response = {}
    response['success'] = True
    response['message'] = 'The vehicle was successfully obtained'
    response['payload'] = get_vehicle.__dict__

    return response


    def get_all():
      get_all_vehicles = Vehicles.find()

      vehicles = []

      for vehicles in get_all_vehicles:
        vehicles.append(vehicle.__dict__)

      response = {}
      response['success'] = True
      response['message'] = 'the vehicles were obtained satisfactorily'
      response['payload'] = vehicles

      return response


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


  def update(body : updateVehicleInputSchema):
    get_vehicle = Vehicle.find_one( id = body['id'])

    if not get_vehicle:
      VehicleException.notFound()

      if not body['active']:
        body['deletedAt'] = datetime.now

    update = Vehicle.update(**body)

    if not update:
      VehicleException.notUpdated()


    get_vehicle_updated = Vehicles.find_one( id = body['id'])

    response = {}
    responde['success'] = True
    response['message'] = 'vehicle successfully created'
    response['payload'] = get_vehicle_updated.__dict__

    return response

  def delete(body: deleteVehicleInputSchema):
    get_vehicle = Vehicles.find_one( id = body['id'])

    if not get_vehicle:
      VehicleException.notFound()


    delete = Vehicles.delete(**body)

    if not delete:
      VehicleException.notDeleted()

    get_vehicle.active = False

    response = {}
    response['success'] = True
    response['message'] = 'vehicle successfully created'
    response['payload'] = get_vehicle.__dict__

    return response