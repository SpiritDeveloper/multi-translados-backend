from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db


class Clients(db.Model):

    __tablename__ = "clients"
    id              = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    code            = Column(String(255), nullable=False)
    business_name   = Column(String(255), nullable=False)
    rfc             = Column(String(18), nullable=False)
    street_name     = Column(String(255), nullable=False)
    phone_number    = Column(String(255), nullable=False)
    interior_number = Column(String(4), nullable=False)
    exterior_number = Column(String(4), nullable=False)
    neighborhood    = Column(String(255), nullable=False)
    state           = Column(String(255), nullable=False)
    zip_code        = Column(String(5), nullable=False)
    logo            = Column(String(255), nullable=False)
    #? https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    active    = Column(Boolean(), nullable=False, default=True)

    def __repr__(self):
        return "<Client {}>".format(self.username)
