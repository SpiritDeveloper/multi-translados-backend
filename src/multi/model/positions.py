from sqlalchemy import Column, ForeignKey, String, DateTime, Boolean, Enum
from sqlalchemy import func, exc
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db
from datetime import datetime

class Positions(db.Model):

    __tablename__ = "positions"
    id          = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    id_area     = Column(UUID(as_uuid=True), ForeignKey("areas.id", ondelete="CASCADE", name="id_areas"))
    title       = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    active    = Column(Boolean(), nullable=False, default=True)

    def save(**kwargs):
        try:
            user = Positions(**kwargs)
            db.session.add(user)
            db.session.commit()
            return user
        except Exception as error:
            print(error)
            return {}
        finally:
            pass

    def find():
        try:
            return Positions.query.filter_by().all()
        except:
            return {}
        finally:
            pass

    def find_one(**kwargs):
        try:
            return db.session.query(Positions).filter_by(**kwargs).first()
        except exc.SQLAlchemyError as err:
            print(err)
            return {}
        finally:
            db.session.close()

    def updated(**update):
        try:
            update["updateAt"] = datetime.now()
            updated = (
                db.session.query(Positions)
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
                db.session.query(Positions)
                .filter_by(**kwargs)
                .update(
                    {"active": False, "deleteAt": datetime.now()},
                    synchronize_session="fetch",
                )
            )
            db.session.commit()
            return updated
        except exc.SQLAlchemyError as err:
            print(err)
            db.session.rollback()
            return {}