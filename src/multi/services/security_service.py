from ..dto import singInInputSchema
from ..model.users import Users
from ..utils.jwt import Jwt
from ..dto import signInOutputSchema
from ..exceptions.signIn_exeption import SignInErrors


class Security:
    def signIn(**kwargs: singInInputSchema) -> signInOutputSchema:
        user: Users = Users.find_one(email=kwargs["email"], password=kwargs["password"])

        if not user:
            SignInErrors.notFoundUser()

        user.uuid = str(user.id)

        del user.password
        del user.id
        del user.active
        del user.startAt
        del user.deleteAt
        del user.updateAt
        del user._sa_instance_state

        token: str = Jwt().encode(user.__dict__)

        if not token:
            SignInErrors.notCreatedToken()

        response: signInOutputSchema = {}
        response["success"] = True
        response["message"] = "sign in correctly"
        response["payload"] = {}
        response["payload"]["token"] = token
        return response
