from ..dto import createClientInputSchema, updateClientInputSchema, deleteClientInputSchema
from ..model import Clients
from ..exceptions.clients_exception import ClientException
from ..utils.validate_attribute import validateAttribute
from datetime import datetime

class ClientService:
  def get(clientId : str):
    get_client = Clients.find_one( id = clientId)

    if not get_client:
      ClientException.notFound()

    response = {}
    response['success'] = True
    response['message'] = 'The client was successfully  obtained'
    response['payload'] = get_client.__dict__

    return response


  def get_all():
    get_all_clients = Clients.find()

    clients = []

    for clients in get_all_clients:
      clients.append(client.__dict__)

    response = {}
    response['success'] = True
    response['message'] = 'the client was obtained satisfactorily'
    response['payload'] = clients

    return response


  def create(body: createClientInputSchema):
    new_client = Clients.save(**body)

    if not new_client:
      ClientException.notCreated()

    client = Clients.find_one( id = new_client.id )

    response = {}
    response['success'] = True
    response['message'] = 'client successfully created'
    response['payload'] = client.__dict__

    return response


  def update(body : updateClientInputSchema):
    get_client = Client.find_one( id = body['id'])

    if not get_client:
      ClientException.notFound()

      if not body['active']:
        body['deletedAt'] = datetime.now

    update = Client.update(**body)

    if not update:
      ClientException.notUpdated()


    get_client_updated = Clients.find_one( id = body['id'])

    response = {}
    responde['success'] = True
    response['message'] = 'client successfully created'
    response['payload'] = get_client_updated.__dict__

    return response


  def delete(body: deleteClientInputSchema):
        get_client = Clients.find_one( id = body['id'] )

        if not get_client:
            ClientException.notFound()


        delete = Clients.delete(**body)

        if not delete:
            ClientException.notDeleted()

        get_client.active = False

        response = {}
        response['success'] = True
        response['message'] = 'client successfully deleted'
        response['payload'] = get_client.__dict__

        return response