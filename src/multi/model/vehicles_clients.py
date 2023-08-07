from sqlalchemy import Column, ForeignKey, String, DateTime, Boolean
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db


class VehiclesClients(db.Model):

    __tablename__ = "vehicles_clients"
    id          = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    id_vehicle  = Column(UUID(as_uuid=True), ForeignKey("vehicles.id", ondelete="CASCADE", name="id_vehicle"))
    id_client   = Column(UUID(as_uuid=True), ForeignKey("clients.id", ondelete="CASCADE", name="id_client"))
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=True)
    active    = Column(Boolean(), nullable=False, default=True)

    def __repr__(self):
        return "<VehicleClient {}>".format(self.username)
