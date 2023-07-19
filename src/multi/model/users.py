from sqlalchemy import Column, ForeignKey, String, DateTime, Boolean
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db


class Users(db.Model):

    __tablename__ = "users"
    id        = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    name                = Column(String(100), nullable=False)
    paternal_last_name  = Column(String(100), nullable=False)
    maternal_last_name  = Column(String(100), nullable=False)
    email               = Column(String(80), nullable=False)
    password            = Column(String(20), nullable=False)
    id_position         = Column(UUID(as_uuid=True), ForeignKey("position.id", ondelete="CASCADE", name="id_position"))
    profile_photo       = Column(String(255), nullable=False)
    #? https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    active    = Column(Boolean(), nullable=False, default=True)

    def __repr__(self):
        return "<User {}>".format(self.username)
