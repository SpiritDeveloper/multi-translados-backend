from sqlalchemy import Column, String, DateTime, Boolean, Float
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db


class Persons(db.Model):

    __tablename__ = "persons"
    id                  = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    name                = Column(String(100), nullable=False)
    paternal_last_name  = Column(String(100), nullable=False)
    maternal_last_name  = Column(String(100), nullable=False)
    birth_day           = Column(DateTime(), nullable=True)
    date_hire           = Column(DateTime(), nullable=False)
    salary              = Column(Float, nullable=False)
    #? https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    active    = Column(Boolean(), nullable=False, default=True)

    def __repr__(self):
        return "<Person {}>".format(self.username)
