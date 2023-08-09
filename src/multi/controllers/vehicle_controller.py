from flask.views import MethodView
from flask_smorest import Blueprint
from flask import jsonify
from ..dto import createVehicleInputSchema, createVehicleOutputSchema, createVehicleOutput, createVehicleInput, getVehicleOutputSchema, getVehicleOutput, getAllVehicleOutputSchema, getAllAreaOutput
from ..services.vehicle_service import VehicleService
vehicle = Blueprint(
  "Vehicle", "vehicle", url_prefix="/vehicle/", description="Vehicle Service"
)

class Vehicle(MethodView):
  @vehicle.errorhandler(404)
  def controlled_error(e):
    return(
      jsonify(success=False, message=e.description, payload={}),
      404,
    )

  @vehicle.errorhandler(Exception)
  def general_exception(e):
    try:
      return(
        jsonify(
          success=False,
          message=e.data["messages"]["json"],
          payload={},
        ),
        422,
      )
    except:
      return(
        jsonify(
          success=402,
          message=str(e),
          payload={},
        ),
        422
      )

  @vehicle.route("/get/<uuid:vehicleId>", methods=["GET"])
  @vehicle.response(200, getVehicleOutputSchema, content_type="application/json")
  def get_one(vehicleId: str):
    """Get vehicle by uuid"""
    return getVehicleOutput.create(VehicleService.get(vehicleId))


  @vehicle.route("/get", methods=["GET"])
  @vehicle.response(200, getAllVehicleOutputSchema, content_type="application/json")
  def get_all():
    """Get all vehicles"""
    return getAllVehicleOutput.create(VehicleService.get_all())


  @vehicle.route("/create", methods=["POST"])
  @vehicle.arguments(createVehicleInputSchema, location="json")
  @vehicle.response(200, createVehicleOutputSchema, content_type="application/json")
  def create(body: createVehicleInputSchema):
    """Create a new vehicle"""
    new_vehicle = createVehicleInput.create(body)
    return createVehicleOutput.create(VehicleService.create(new_vehicle))