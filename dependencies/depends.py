#!/usr/bin/python3

"""Dependencies for authenticating user"""

from typing import Any, Generator
from fastapi import Depends, HTTPException, status
from config.config import settings
from utils import auth
from utils.oauth1 import AuthJWT
from engine.loadb import load
from models import user as userModel

db = load()

class NotVerified(Exception):
    pass


class UserNotFound(Exception):
    pass


def get_current_user(Authorize: AuthJWT = Depends()):

    try:
        Authorize.jwt_required()
        user_id = Authorize.get_jwt_subject()
        print(user_id)
        data = Authorize.get_raw_jwt()
        user = db.query_eng(userModel.Users).filter(
            userModel.Users.name == user_id).first()
        if not user:
            raise UserNotFound('User no longer exist')


    except Exception as e:
        error = e.__class__.__name__
        print(error)
        if error == 'MissingTokenError':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='You are not logged in')
        if error == 'UserNotFound':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='User no longer exist')
        if error == 'NotVerified':
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail='Please verify your account')
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Token is invalid or has expired')

    return data