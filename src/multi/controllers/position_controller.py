from flask.views import MethodView
from flask_smorest import Blueprint
from flask import jsonify


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
    @position.response(200, {}, content_type="application/json")
    def get_one(positionId):
        """Get position by uuid"""
        return {}
    
    @position.route("/get", methods=["GET"])
    @position.response(200, {}, content_type="application/json")
    def get_all():
        """Get all positions"""
        return {}
    
    
    @position.route("/create", methods=["POST"])
    @position.response(200, {}, content_type="application/json")
    def create():
        """Create a new position"""
        return {}
    
    @position.route("/update", methods=["PUT"])
    @position.response(200, {}, content_type="application/json")
    def update():
        """Update position"""
        return {}
    
    @position.route("/delete", methods=["DELETE"])
    @position.response(200, {}, content_type="application/json")
    def delete():
        """Delete position"""
        return {}
    
  