from ..dto import createAreaInputSchema, updateAreaInputSchema, deleteAreaInputSchema

class AreaService:
    def get(areaId: str):
        print(areaId)
        return {}
    
    def get_all():
        return {}
    
    def create(body: createAreaInputSchema):
        print(body)
        return {}
    
    def update(body: updateAreaInputSchema):
        print(body)
        return {}
    
    def delete(body: deleteAreaInputSchema):
        print(body)
        return {}