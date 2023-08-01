from sqlalchemy import Column, ForeignKey, String, DateTime, Boolean
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db


class VinUnities(db.Model):

    __tablename__ = "vin_unities"
    id      = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    id_move = Column(UUID(as_uuid=True), ForeignKey("moves.id", ondelete="CASCADE", name="id_move"))
    amount  = Column(String(255), nullable=False)
    year    = Column(String(255), nullable=False)
    weight  = Column(String(18), nullable=False)
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    active    = Column(Boolean(), nullable=False, default=True)

    def __repr__(self):
        return "<VinUnit {}>".format(self.username)
