from sqlalchemy import Column, ForeignKey, String, DateTime, Boolean
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db


class WorkerBadge(db.Model):

    __tablename__ = "workers_badges"
    id                  = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    id_worker           = Column(UUID(as_uuid=True), ForeignKey("workers.id", ondelete="CASCADE", name="id_worker"))
    idBadge            = Column(String(255), nullable=False) #Gafete de identificación
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    active    = Column(Boolean(), nullable=False, default=True)

    def __repr__(self):
        return "<Operator {}>".format(self.username)
