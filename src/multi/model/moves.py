from sqlalchemy import Column, ForeignKey, String, DateTime, Boolean
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db


class Moves(db.Model):

    __tablename__ = "moves"
    id                = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    id_client         = Column(UUID(as_uuid=True), ForeignKey("clients.id", ondelete="CASCADE", name="id_client"))
    id_vehicle        = Column(UUID(as_uuid=True), ForeignKey("vehicles.id", ondelete="CASCADE", name="id_vehicle"))
    id_operator       = Column(UUID(as_uuid=True), ForeignKey("operators.id", ondelete="CASCADE", name="id_operator"))
    total_kilometers  = Column(String(255), nullable=False)
    contact_name      = Column(String(255), nullable=False)
    contact_phone     = Column(String(18), nullable=False)
    rfc               = Column(String(18), nullable=False)
    business_name     = Column(String(255), nullable=False)
    sat_key           = Column(String(255), nullable=False)
    measure_unit      = Column(String(255), nullable=False)
    packaging         = Column(String(4), nullable=False)
    #? https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    endedAt   = Column(DateTime(timezone=True), nullable=False)
    updatedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    active    = Column(Boolean(), nullable=False, default=True)

    def __repr__(self):
        return "<Move {}>".format(self.username)
