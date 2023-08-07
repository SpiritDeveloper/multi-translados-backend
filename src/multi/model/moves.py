from sqlalchemy import Column, ForeignKey, String, DateTime, Boolean
from sqlalchemy import func,exc
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db
from datetime import datetime


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
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    endedAt   = Column(DateTime(timezone=True), nullable=False)
    updatedAt = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=True)
    active    = Column(Boolean(), nullable=False, default=True)

    def save(**kwargs):
        try:
            move = Moves(**kwargs)
            db.session.add(move)
            db.session.commit()
            return move
        except Exception as error:
            print(error)
            return {}
        finally:
            pass

    def find():
        try:
            return Moves.query.filter_by().all()
        except:
            return {}
        finally:
            pass

    def find_one(**kwargs):
        try:
            return db.session.query(Moves).filter_by(**kwargs).first()
        except exc.SQLAlchemyError as err:
            print(err)
            return {}
        finally:
            db.session.close()

    def update(**update):
        try:
            update["updatedAt"] = datetime.now()
            updated = (
                db.session.query(Moves)
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
                db.session.query(Moves)
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