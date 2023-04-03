from flask.views import MethodView
from flask_smorest import Blueprint
from flask import jsonify
from ..dto import singInInputSchema, signInInput, signInOutput, signInOutputSchema
from ..services.security_service import Security as SecurityClass

security = Blueprint(
    "Security", "security", url_prefix="/security/", description="Sign in"
)


class Security(MethodView):
    @security.errorhandler(404)
    def controlled_errors(e):
        return (
            jsonify(code=404, errors=e.description, message="API error", status="API"),
            404,
        )

    @security.errorhandler(Exception)
    def general_exception(e):
        try:
            return (
                jsonify(
                    code=402,
                    errors=e.data["messages"]["json"],
                    message="API error",
                    status="API",
                ),
                422,
            )
        except:
            return (
                jsonify(code=402, errors=str(e), message="API error", status="API"),
                422,
            )

    @security.route("/signIn", methods=["POST"])
    @security.arguments(singInInputSchema, location="json")
    @security.response(200, signInOutputSchema, content_type="application/json")
    def signIn(body: singInInputSchema):
        """Sign In"""
        body: singInInputSchema = signInInput.create(body)
        return signInOutput.create(SecurityClass.signIn(**body))
