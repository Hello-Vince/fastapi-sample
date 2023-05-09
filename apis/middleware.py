'''This module includes routers into the FastAPI framework.'''

from fastapi import APIRouter

from apis.routers import admin_login, admin_mgmt
from apis.routers import create_user, update_user


api_routers = APIRouter()

# Admin
admin_schema = True  # pylint: disable=[C0103]
prefix = '/admin'  # pylint: disable=[C0103]
tags = ['Admin']
api_routers.include_router(admin_login.router, prefix=prefix, tags=tags, include_in_schema=admin_schema)
api_routers.include_router(admin_mgmt.router, prefix=prefix, tags=tags, include_in_schema=admin_schema)


# User
prefix = '/user'  # pylint: disable=[C0103]
tags = ['User']
api_routers.include_router(create_user.router, prefix=prefix, tags=tags)
api_routers.include_router(update_user.router, prefix=prefix, tags=tags)
