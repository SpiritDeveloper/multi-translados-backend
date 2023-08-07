from ..dto import singInInputSchema, singUpInputSchema
from ..model.users import Users
from ..utils.jwt import Jwt
from ..exceptions.security_exeption import SecurityException

class SecurityService:
    def signIn(signIn: singInInputSchema):
        user: Users = Users.find_one(email=signIn["email"], password=signIn["password"])

        if not user:
            SecurityException.notFoundUser()

        user.id = str(user.id)
        user.id_position = str(user.id_position)

        del user.password
        del user.active
        del user.startedAt
        del user.deletedAt
        del user.updatedAt
        del user._sa_instance_state

        token: str = Jwt().encode(user.__dict__)

        if not token:
            SecurityException.notCreatedToken()

        response = {}
        response["success"] = True
        response["message"] = "sign in correctly"
        response["payload"] = {}
        response["payload"]["token"] = token
        return response

    def signUp(signUp: singUpInputSchema):
        user: Users = Users.find_one(email=signUp["email"])

        if user:
            SecurityException.userExist()

        newUser = Users.save(**signUp)

        if not newUser:
            SecurityException.userNotCreated()

        user: Users = Users.find_one(id=newUser.id)
        
        response = {}
        response["success"] = True
        response["message"] = "sign up correctly"
        response["payload" ]= user.__dict__

        return response