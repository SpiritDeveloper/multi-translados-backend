from flask.views import MethodView
from flask_smorest import Blueprint
from flask import jsonify
from ..dto import singInInputSchema, signInInput, signInOutput, signInOutputSchema, singUpInputSchema, signUpInput
from ..services.security_service import Security as SecurityClass

security = Blueprint(
    "Security", "security", url_prefix="/security/", description="Security Services"
)


class Security(MethodView):
    @security.errorhandler(404)
    def controlled_errors(e):
        return (
            jsonify(success=False, message=e.description, payload={}),
            404,
        )

    @security.errorhandler(Exception)
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

    @security.route("/signIn", methods=["POST"])
    @security.arguments(singInInputSchema, location="json")
    @security.response(200, signInOutputSchema, content_type="application/json")
    def signIn(body: singInInputSchema):
        """Sign In"""
        body: singInInputSchema = signInInput.create(body)
        return signInOutput.create(SecurityClass.signIn(body))
    
    @security.route("/signUp", methods=["POST"])
    @security.arguments(singUpInputSchema, location="json")
    @security.response(200, signInOutputSchema, content_type="application/json")
    def signIn(body: singUpInputSchema):
        """Sign Up"""
        body: singUpInputSchema = signUpInput.create(body)
        return signInOutput.create(SecurityClass.signUp(body))
