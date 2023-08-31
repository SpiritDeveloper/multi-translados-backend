from flask.views import MethodView
from flask_smorest import Blueprint
from flask import jsonify
from ..dto import createVehicleInputSchema, createVehicleOutputSchema, createVehicleOutput, createVehicleInput, getVehicleOutputSchema, getVehicleOutput, getAllVehicleOutputSchema, getAllAreaOutput, updateVehicleInputSchema, updateVehicleOutputSchema, updateVehicleInput, updateVehicleOutput, deleteVehicleInputSchema, deleteVehicleOutputSchema, deleteVehicleInput, deleteVehicleOutput
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


  @vehicle.route("/update", methods=["PUT"])
  @vehicle.arguments(updateVehicleInputSchema, location="json")
  @vehicle.response(200, updateVehicleOutputSchema, content_type="application/json")
  def update(body: updateVehicleInputSchema):
    """Update vehicle"""
    update_vehicle = updateVehicleInput.update(body)
    return updateVehicleOutput.update(VehicleService.update(update_vehicle))


  @vehicle.route("/delete", methods=["DELETE"])
  @vehicle.arguments(deleteVehicleInputSchema, location="json")
  @vehicle.response(200, deleteVehicleOutputSchema, content_type="application/json")
  def delete(body: deleteVehicleInputSchema):
    """Delete vehicle"""
    delete_vehicle = deleteVehicleInput.delete(body)
    return deleteVehicleOutput.delete(VehicleService.delete(delete_vehicle))

  @vehicle.route("/delete", methods=["DELETE"])
  @vehicle.arguments(deleteVehicleInputSchema, location="json")
  @vehicle.response(200, deleteVehicleOutputSchema, content_type="application/json")
  def delete(body: deleteVehicleInputSchema):
    """Delete vehicle"""
    delete_vehicle = deleteVehicleInput.create(body)
    return deleteVehicleOutput.create(VehicleService.delete(delete_vehicle))