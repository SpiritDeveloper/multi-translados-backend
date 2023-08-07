from sqlalchemy import Column, ForeignKey, String, DateTime, Boolean
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db


class Vehicles(db.Model):

    __tablename__ = "vehicles"
    id          = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    model       = Column(String(255), nullable=False)
    performance = Column(String(255), nullable=False)
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=True)
    active    = Column(Boolean(), nullable=False, default=True)

    def __repr__(self):
        return "<Vehicle {}>".format(self.username)
