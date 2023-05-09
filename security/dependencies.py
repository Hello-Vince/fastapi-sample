'''This module manages global application dependencies.'''

import json
from fastapi import Request, status
from sqlalchemy.orm import Session

from apis.schemas import user
from helpers.api_exceptions import ResponseValidationError
from database import crud, models
from security.hashing import SecureHash


async def verify_request_content(request: Request):
    '''Ensure request content is JSON serializable.'''

    try:
        _json = await request.json()
    except json.decoder.JSONDecodeError:
        _json = None
    return _json


def authenticate_user(db: Session, item: user.UpdateUserRequest):
    '''Ensure user is authenticated.'''

    user = crud.get_object(
        db=db,
        table=models.UserTable,
        column=models.UserTable.email,
        value=item.email
    )
    if not user:
        raise ResponseValidationError(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message='Invalid email.'
        )

    if not SecureHash.verify(item.password, user.hashed_password):
        raise ResponseValidationError(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message='Invalid password.'
        )

    return user
