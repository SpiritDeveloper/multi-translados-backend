from flask.views import MethodView
from flask_smorest import Blueprint
from flask import jsonify
from ..dto import createAreaInputSchema, updateAreaInputSchema, deleteAreaInputSchema, createAreaOutputSchema, updateAreaOutputSchema, deleteAreaOutputSchema, getAllAreaOutputSchema, getAreaOutputSchema, getAreaOutput, getAllAreaOutput, createAreaOutput, createAreaInput, updateAreaInput, updateAreaOutput, deleteAreaInput, deleteAreaOutput
from ..services.area_service import AreaService
area = Blueprint(
    "Area", "area", url_prefix="/area/", description="Area Services"
)


class Area(MethodView):
    @area.errorhandler(404)
    def controlled_errors(e):
        return (
            jsonify(success=False, message=e.description, payload={}),
            404,
        )

    @area.errorhandler(Exception)
    def general_exception(e):
        try:
            return (
                jsonify(
                    success=False,
                    message=e.data["messages"]["json"],
                    payload={},
                ),
                422,
            )
        except:
            return (
                jsonify(success=402, message=str(e), payload={}),
                422,
            )

    @area.route("/get/<uuid:areaId>", methods=["GET"])
    @area.response(200, getAreaOutputSchema, content_type="application/json")
    def get_one(areaId: str):
        """Get area by uuid"""
        return getAreaOutput.create(AreaService.get(areaId))
        
    
    @area.route("/get", methods=["GET"])
    @area.response(200, getAllAreaOutputSchema, content_type="application/json")
    def get_all():
        """Get all areas"""
        return getAllAreaOutput.create(AreaService.get_all())
    
    
    @area.route("/create", methods=["POST"])
    @area.arguments(createAreaInputSchema, location="json")
    @area.response(200, createAreaOutputSchema, content_type="application/json")
    def create(body: createAreaInputSchema):
        """Create a new area"""
        new_area = createAreaInput.create(body)
        return createAreaOutput.create(AreaService.create(new_area))
    
    @area.route("/update", methods=["PUT"])
    @area.arguments(updateAreaInputSchema, location="json")
    @area.response(200, updateAreaOutputSchema, content_type="application/json")
    def update(body: updateAreaInputSchema):
        """Update area"""
        update_area = updateAreaInput.create(body)
        return updateAreaOutput.create(AreaService.update(update_area))
    
    @area.route("/delete", methods=["DELETE"])
    @area.arguments(deleteAreaInputSchema, location="json")
    @area.response(200, deleteAreaOutputSchema, content_type="application/json")
    def delete(body: deleteAreaInputSchema):
        """Delete area"""
        delete_area = deleteAreaInput.create(body)
        return deleteAreaOutput.create(AreaService.delete(delete_area))
    
  