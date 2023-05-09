'''This module manages the user update FastAPI router.'''

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from apis.schemas.user import UpdateUserRequest, UserResponse
from database import crud, models
from database.session import get_db
from security.dependencies import authenticate_user


router = APIRouter()


@router.post('/update', status_code=status.HTTP_200_OK, dependencies=[Depends(authenticate_user)], response_model=UserResponse)
async def update_user(
    item: UpdateUserRequest,
    db: Session = Depends(get_db)
):
    '''
    Update a user data profile.

        :param email [str]: User email.
        :param password [str]: User password.
        :param is_active [bool]: User status.

        :returns [UserResponse]: User has successfully been updated.
    '''

    crud.update_object(
        db=db,
        table=models.UserTable,
        column=models.UserTable.email,
        value=item.email,
        data=dict(is_active=item.isActive)
    )

    # format response
    user = crud.get_object(
        db=db,
        table=models.UserTable,
        column=models.UserTable.email,
        value=item.email
    )

    return UserResponse(
        email=user.email,
        isActive=user.is_active,
        createdAt=user.created_at,
        updatedAt=user.updated_at
    )
