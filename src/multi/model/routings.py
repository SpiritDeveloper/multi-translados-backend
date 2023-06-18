from sqlalchemy import Column, ForeignKey, String, DateTime, Boolean, Enum
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db
from enum import Enum

#? https://stackoverflow.com/questions/33612625/how-to-model-enums-backed-by-integers-with-sqlachemy
#? https://docs.sqlalchemy.org/en/14/core/type_basics.html#sqlalchemy.types.Enum
class TypeEnum(Enum):
  origin         = "origin"
  destiny        = "destiny"

class TransferPolicies(db.Model):

    __tablename__ = "transfer_policies"
    id              = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    id_move         = Column(UUID(as_uuid=True), ForeignKey("moves.id", ondelete="CASCADE", name="id_move"))
    street_name     = Column(String(255), nullable=False)
    interior_number = Column(String(4), nullable=False)
    exterior_number = Column(String(4), nullable=False)
    neighborhood    = Column(String(255), nullable=False)
    municipality    = Column(String(255), nullable=False)
    state           = Column(String(255), nullable=False)
    zip_code        = Column(String(5), nullable=False)
    category        = Column(Enum(TypeEnum), nullable=False)

    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    active    = Column(Boolean(), nullable=False, default=True)

    def __repr__(self):
        return "<TransferPolicy {}>".format(self.username)

