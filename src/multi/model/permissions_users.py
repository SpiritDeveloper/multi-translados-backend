from sqlalchemy import Column, ForeignKey, String, DateTime, Boolean
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db


class PermissionsClients(db.Model):

    __tablename__ = "permissions_clients"
    id              = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    id_person       = Column(UUID(as_uuid=True), ForeignKey("persons.id", ondelete="CASCADE", name="id_person"))
    id_permission   = Column(UUID(as_uuid=True), ForeignKey("permissions.id", ondelete="CASCADE", name="id_permission"))
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    active    = Column(Boolean(), nullable=False, default=True)

    def __repr__(self):
        return "<PermissionClient {}>".format(self.username)