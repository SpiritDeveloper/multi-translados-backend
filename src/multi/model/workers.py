from sqlalchemy import Column, String, DateTime, Boolean, Float
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db


class Workers(db.Model):

    __tablename__ = "workers"
    id                  = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    name                = Column(String(100), nullable=False)
    paternal_last_name  = Column(String(100), nullable=False)
    maternal_last_name  = Column(String(100), nullable=False)
    birth_day           = Column(DateTime(), nullable=True)
    date_hire           = Column(DateTime(), nullable=False)
    salary              = Column(Float, nullable=False)
    street_name         = Column(String(255), nullable=False)
    interior_number     = Column(String(4), nullable=False)
    exterior_number     = Column(String(4), nullable=False)
    neighborhood        = Column(String(255), nullable=False)
    zip_code            = Column(String(5), nullable=False)
    municipality        = Column(String(255), nullable=False)
    state               = Column(String(255), nullable=False)
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    active    = Column(Boolean(), nullable=False, default=True)

    def __repr__(self):
        return "<Worker {}>".format(self.username)
