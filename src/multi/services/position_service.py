from ..dto import createPositionInputSchema, updatePositionInputSchema, deletePositionInputSchema
from ..model import Positions, Areas
from ..exceptions.positions_exeption import PositionException
from ..exceptions.area_exeption import AreaException
from ..utils.validate_attribute import validateAttribute
from datetime import datetime
class PositionService:
    def get(positionId: str):
        get_position = Positions.find_one( id= positionId )
        
        if not get_position: 
            PositionException.notFound()

        response = {}
        response['success'] = True
        response['message'] = 'the position was successfully obtained'
        response['payload'] = get_position.__dict__

        return response
    
    def get_all():
        get_all_positions = Positions.find()
        
        positions = []
        
        for position in get_all_positions:
            positions.append(position.__dict__)
            
        response = {}
        response['success'] = True
        response['message'] = 'the position were obtained satisfactorily'
        response['payload'] = positions

        return response
    
    def create(body: createPositionInputSchema):
        exist = Areas.find_one( id = body['id_area'] )
        
        if not exist: 
            AreaException.notFound()

        new_position  = Positions.save(**body)

        if not new_position:
            PositionException.notCreated()

        position  = Positions.find_one( id = new_position.id )
        
        response = {}
        response['success'] = True
        response['message'] = 'position successfully created'
        response['payload'] = position.__dict__

        return response
    
    def update(body: updatePositionInputSchema):
        get_position = Positions.find_one( id = body ['id'])

        if not get_position:
            PositionException.notFound()

        get_area = Areas.find_one( id = body['id_area'] )

        if not get_area:
            AreaException.notFound()

        if validateAttribute(body, 'active'):
            body['deletedAt'] = None

            if not body['active']:
                body['deletedAt'] = datetime.now()

        
        update = Positions.updated(**body)

        if not update:
            AreaException.notUpdated()


        get_position_updated = Positions.find_one( id = body['id'] )    

        response = {}
        response['success'] = True
        response['message'] = 'position successfully created'
        response['payload'] = get_position_updated.__dict__

        return response
    
    def delete(body: deletePositionInputSchema):
        get_position = Positions.find_one( id = body['id'] )

        if not get_position:
            PositionException.notFound()

        
        delete = Positions.delete(**body)

        if not delete:
            PositionException.notDeleted()

        get_position.active = False
        
        response = {}
        response['success'] = True
        response['message'] = 'position successfully created'
        response['payload'] = get_position.__dict__

        return response