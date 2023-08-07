from sqlalchemy import Column, ForeignKey, String, DateTime, Boolean, Enum
from sqlalchemy import func, exc
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db
from enum import Enum
from datetime import datetime

#? https://stackoverflow.com/questions/33612625/how-to-model-enums-backed-by-integers-with-sqlachemy
#? https://docs.sqlalchemy.org/en/14/core/type_basics.html#sqlalchemy.types.Enum
class TypeEnum(Enum):
  chassis         = "chassis"
  bodywork        = "bodywork"
  civilLiability  = "civil liability"

class TransferPolicies(db.Model):

    __tablename__ = "transfer_policies"
    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    id_move       = Column(UUID(as_uuid=True), ForeignKey("moves.id", ondelete="CASCADE", name="id_move"))
    company_name  = Column(String(255), nullable=False)
    #* Opción 1
    #! category     = Column(Enum(TypeEnum), nullable=False)
    #* Opción 2, no tengo pruebas, pero tampoco dudas
    type          = Column(Enum(["chassis", "bodywork", "civil liability"]), nullable=False)
    policy_number = Column(String(50), nullable=False)
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=True)
    active    = Column(Boolean(), nullable=False, default=True)

    def save(**kwargs):
        try:
            transfer = TransferPolicies(**kwargs)
            db.session.add(transfer)
            db.session.commit()
            return transfer
        except Exception as error:
            print(error)
            return {}
        finally:
            pass

    def find():
        try:
            return TransferPolicies.query.filter_by().all()
        except:
            return {}
        finally:
            pass

    def find_one(**kwargs):
        try:
            return db.session.query(TransferPolicies).filter_by(**kwargs).first()
        except exc.SQLAlchemyError as err:
            print(err)
            return {}
        finally:
            db.session.close()

    def update(**update):
        try:
            update["updatedAt"] = datetime.now()
            updated = (
                db.session.query(TransferPolicies)
                .filter_by(id=str(update["id"]))
                .update(update, synchronize_session="fetch")
            )
            db.session.commit()
            return updated
        except Exception as error:
            print(error)
            return {}

    def delete(**kwargs) -> int:
        try:
            updated = (
                db.session.query(TransferPolicies)
                .filter_by(**kwargs)
                .update(
                    {"active": False, "deletedAt": datetime.now()},
                    synchronize_session="fetch",
                )
            )
            db.session.commit()
            return updated
        except exc.SQLAlchemyError as err:
            print(err)
            db.session.rollback()
            return {}
