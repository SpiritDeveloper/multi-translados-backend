from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db


class Permissions(db.Model):

    __tablename__ = "permissions"
    id          = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    view        = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    #? https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    active    = Column(Boolean(), nullable=False, default=True)

    def __repr__(self):
        return "<Permission {}>".format(self.username)
