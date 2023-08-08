from flask.views import MethodView
from flask_smorest import Blueprint
from flask import jsonify
from ..dto import createClientInputSchema, updateClientInputSchema, deleteClientInputSchema, createClientOutputSchema, updateClientOutputSchema, deleteClientOutputSchema, getAllClientOutputSchema, getClientOutputSchema, getClientOutput, getAllClientOutput, createClientOutput, createClientInput, updateClientInput, updateClientOutput, deleteClientInput, deleteClientOutput
from ..services.client_service import ClientService
client = Blueprint(
  "Client", "client", url_prefix="/client/", description="Client Services"
)

class Client(MethodView):
  @client.errorhandler(404)
  def controlled_errors(e):
    return (
      jsonify(success=False, message=e.description, payload={}),
      404,
    )

  @client.errorhandler(Exception)
  def general_exception(e):
    try:
      return(
        jsonify(
          success=False
          message=e.date["messages"]["json"],
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

  @client.route("/get/<uuid:clientId>", methods=["GET"])
  @client.response(200, getClientOutputSchema, content_type="application/json")
  def get_one(clientId: str):
    """Get client by uuid"""
    return getClientOutput.create(ClientService.get(clientId))


  @client.route("/get", methods=["GET"])
  @client.response(200, getAllClientOutputSchema, content_type="application/json")
  def get_all():
    """Get all clients"""
    return getAllClientOutput.create(ClientService.get_all())


  @client.route("/create", methods=["POST"])
  @client.arguments(createClientInputSchema, location="json")
  @client.response(200, createClientOutputSchema, content_type="application/json")
  def create(body: createClientInputSchema):
    """Create a new client"""
    new_client = createClientInput.create(body)
    return createClientOutput.create(ClientService.create(new_client))


  @client.route("update", methods=["PUT"])
  @client.arguments(updateClientInputSchema, location="json")
  @client.response(200, updateClientOutputSchema, content_type="application/json")
  def update(body: updateClientInputSchema):
    """Update client"""
    update_client = updateClientInput.create(body)
    return updateClientOutput.create(ClientService.update(update_client))


  @client.route("/delete", methods=["DELETE"])
  @client.arguments(deleteClientInputSchema, location="json")
  @client.response(200, deleteClientInputSchema):
    """Delete client"""
    delete_client = deleteClientInput.create(body)
    return deleteClientOutput.create(ClientService.delete(delete_client))