from flask.views import MethodView
from flask_smorest import Blueprint
from flask import jsonify
from src.multi.dto.output.main_output_dto import responseSchema

main = Blueprint("Main", "main", url_prefix="/", description="Main")


class Main(MethodView):
    @main.route("/", methods=["GET"])
    @main.response(200, responseSchema, content_type="application/json")
    @main.doc(authorize=False)
    def get():
        """Get status to server"""
        return jsonify(
            {
                "starting": "Running...",
                "name": "microservice-multitranslados",
                "version": "V1.0.0",
            }
        )
