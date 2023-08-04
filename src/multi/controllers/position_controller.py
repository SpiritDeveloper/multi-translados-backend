from flask.views import MethodView
from flask_smorest import Blueprint
from flask import jsonify
from ..dto import createPositionInputSchema, deletePositionInputSchema, updatePositionInputSchema, getAllPositionOutputSchema, getPositionOutputSchema, createPositionOutputSchema, updatePositionOutputSchema, deletePositionInputSchema

position = Blueprint(
    "Position", "position", url_prefix="/position/", description="Position Services"
)


class Position(MethodView):
    @position.errorhandler(404)
    def controlled_errors(e):
        return (
            jsonify(success=False, message=e.description, payload={}),
            404,
        )

    @position.errorhandler(Exception)
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

    @position.route("/get/<uuid:positionId>", methods=["GET"])
    @position.response(200, getPositionOutputSchema, content_type="application/json")
    def get_one(positionId: str):
        """Get position by uuid"""
        return {}
    
    @position.route("/get", methods=["GET"])
    @position.response(200, getAllPositionOutputSchema, content_type="application/json")
    def get_all():
        """Get all positions"""
        return {}
    
    
    @position.route("/create", methods=["POST"])
    @position.arguments(createPositionInputSchema, location="json")
    @position.response(200, createPositionOutputSchema, content_type="application/json")
    def create(body: createPositionInputSchema):
        """Create a new position"""
        return {}
    
    @position.route("/update", methods=["PUT"])
    @position.arguments(updatePositionInputSchema, location="json")
    @position.response(200, updatePositionOutputSchema, content_type="application/json")
    def update(body: updatePositionInputSchema):
        """Update position"""
        return {}
    
    @position.route("/delete", methods=["DELETE"])
    @position.arguments(deletePositionInputSchema, location="json")
    @position.response(200, deletePositionInputSchema, content_type="application/json")
    def delete(body: deletePositionInputSchema):
        """Delete position"""
        return {}
    
  