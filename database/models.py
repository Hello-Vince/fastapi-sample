'''This module defines all database tables.'''

from enum import Enum as Enumerations
from sqlalchemy import Column, Boolean, Integer, Float, String, DateTime, Enum
from sqlalchemy.sql import func

from database.session import Base


# Enumerations
class Status(Enumerations):
    '''Status values.'''

    APPROVED = 'approved'
    DECLINED = 'declined'
    PENDING = 'pending'


# Database Columns
class AdminsTable(Base):
    '''Define admins as a database table.'''

    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class UserTable(Base):
    '''Define users as a database table.'''

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False)
    status = Column(Enum(Status))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class FarmsTable(Base):
    '''Define farms as a database table.'''

    __tablename__ = 'farms'

    id = Column(Integer, primary_key=True, autoincrement=True)
    GroupScheme = Column(String, nullable=False)
    Country = Column(String, nullable=False)
    Province = Column(String, nullable=False)
    Latitude = Column(Float, nullable=False)
    Longitude = Column(Float, nullable=False)
    FarmId = Column(String, nullable=False)
    FarmSize = Column(Float, nullable=False)
    UnitNumber = Column(String, nullable=False)
    EffectiveArea = Column(Float, nullable=False)
    AreaTypeName = Column(String, nullable=False)
    ProductGroup = Column(String, nullable=False)
    GenusName = Column(String, nullable=False)
    SpeciesName = Column(String, nullable=False)
    PlantAge = Column(Float, nullable=False)
    SphaSurvival = Column(Float, nullable=False)
    PlannedPlantDT = Column(String, nullable=False)
    IsActive = Column(Boolean, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
