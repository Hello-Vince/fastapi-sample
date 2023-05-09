'''This module manages the insertion of initial data to the database.'''

from config import get_settings
from database import crud, models, session
from helpers.misc import try_except
from security.hashing import SecureHash


settings = get_settings()


ADMIN_MASTER = models.AdminsTable(
    username=settings.ADMIN.USERNAME,
    hashed_password=SecureHash.create(settings.ADMIN.PASSWORD),
    is_active=True
)


def setup_database():
    '''Insert initial data to the database.'''
    try:
        db = session.SessionLocal()
        try_except(crud.create_object, db=db, data=ADMIN_MASTER)
    finally:
        db.close()
