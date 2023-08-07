from sqlalchemy import Column, ForeignKey, String, DateTime, Boolean, Enum
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db
from enum import Enum

#? https://stackoverflow.com/questions/33612625/how-to-model-enums-backed-by-integers-with-sqlachemy
#? https://docs.sqlalchemy.org/en/14/core/type_basics.html#sqlalchemy.types.Enum
class CategoryEnum(Enum):
  tollBooth = "toll booth"
  passage   = "passage"
  food      = "food"
  others    = "others"

class ExtraExpenses(db.Model):

    __tablename__ = "extra_expenses"
    id          = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    id_move     = Column(UUID(as_uuid=True), ForeignKey("moves.id", ondelete="CASCADE", name="id_move"))
    description = Column(String(255), nullable=False)
    #* Opción 1
    category    = Column(Enum(CategoryEnum), nullable=False)
    #* Opción 2, no tengo pruebas, pero tampoco dudas
    #! category      = Column(Enum(["toll booth", "passage", "food", "others" ]), nullable=False)
    amount    = Column(String(18), nullable=False)
    #? https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=True)
    active    = Column(Boolean(), nullable=False, default=True)

    def __repr__(self):
        return "<ExtraExpense {}>".format(self.username)

