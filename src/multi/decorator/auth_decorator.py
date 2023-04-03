from flask import request
from functools import wraps
from ..exceptions.auth_exeptions import AuthErrors
from ..utils.jwt import Jwt
from ..model.users import Users


def auth(func):
    @wraps(func)
    def __Auth(*args, **kwargs):

        token = request.headers.get("Authorization")

        if not token:
            AuthErrors.tokenNotFound()

        if not "Bearer" in token:
            AuthErrors.bearerNotFound()

        token = token.split()[1]

        ip = request.remote_addr

        decrypt: object = Jwt().decode(token)

        existUser: Users = Users.find_one(id=decrypt["uuid"], active=True)

        if not existUser:
            AuthErrors.invalidToken()

        del existUser.deleteAt
        del existUser.startAt
        del existUser.updateAt

        existUser.ip = ip

        request.user = existUser

        return func(*args, **kwargs)

    return __Auth
