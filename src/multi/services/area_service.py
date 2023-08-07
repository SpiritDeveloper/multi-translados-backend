from ..model import Areas
from ..exceptions.area_exeption import AreaException
from ..utils.validate_attribute import validateAttribute
from datetime import datetime
from ..dto import createAreaInputSchema, updateAreaInputSchema, deleteAreaInputSchema
class AreaService:
    def get(areaId: str):
        get_area = Areas.find_one( id= areaId )
        
        if not get_area: 
            AreaException.notFound()

        response = {}
        response['success'] = True
        response['message'] = 'the area was successfully obtained'
        response['payload'] = get_area.__dict__

        return response

    
    def get_all():
        get_all_area = Areas.find()
        
        areas = []
        
        for area in get_all_area:
            areas.append(area.__dict__)
            
        response = {}
        response['success'] = True
        response['message'] = 'the areas were obtained satisfactorily'
        response['payload'] = areas

        return response

    
    def create(body: createAreaInputSchema):
        exist = Areas.find_one( name = body['name'] )
        
        if exist: 
            AreaException.existingArea()

        new_area  = Areas.save(**body)

        if not new_area:
            AreaException.notCreated()

        area  = Areas.find_one( id = new_area.id )
        
        response = {}
        response['success'] = True
        response['message'] = 'area successfully created'
        response['payload'] = area.__dict__

        return response
    
    
    def update(body: updateAreaInputSchema):
        get_area = Areas.find_one( id = body['id'] )

        if not get_area:
            AreaException.notFound()

        if validateAttribute(body, 'active'):
            body['deletedAt'] = None

            if not body['active']:
                body['deletedAt'] = datetime.now()

        
        update = Areas.updated(**body)

        if not update:
            AreaException.notUpdated()


        get_area_updated = Areas.find_one( id = body['id'] )    

        response = {}
        response['success'] = True
        response['message'] = 'area successfully created'
        response['payload'] = get_area_updated.__dict__

        return response
    
    def delete(body: deleteAreaInputSchema):
        get_area = Areas.find_one( id = body['id'] )

        if not get_area:
            AreaException.notFound()

        
        delete = Areas.delete(**body)

        if not delete:
            AreaException.notDeleted()

        get_area.active = False
        
        response = {}
        response['success'] = True
        response['message'] = 'area successfully created'
        response['payload'] = get_area.__dict__

        return response
    