from flask.views import MethodView
from flask_smorest import Blueprint
from flask import jsonify


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
    @area.response(200, {}, content_type="application/json")
    def get_one(areaId):
        """Get area by uuid"""
        return {}
    
    @area.route("/get", methods=["GET"])
    @area.response(200, {}, content_type="application/json")
    def get_all():
        """Get all areas"""
        return {}
    
    
    @area.route("/create", methods=["POST"])
    @area.response(200, {}, content_type="application/json")
    def create(areaId):
        """Create a new area"""
        return {}
    
    @area.route("/update", methods=["PUT"])
    @area.response(200, {}, content_type="application/json")
    def update(areaId):
        """Update area"""
        return {}
    
    @area.route("/delete", methods=["DELETE"])
    @area.response(200, {}, content_type="application/json")
    def delete(areaId):
        """Delete area"""
        return {}
    
  