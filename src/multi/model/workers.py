from sqlalchemy import Column, String, DateTime, Boolean, Float
from sqlalchemy import func, exc
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db
from datetime import datetime


class Workers(db.Model):

    __tablename__ = "workers"
    id                  = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    name                = Column(String(100), nullable=False)
    paternal_last_name  = Column(String(100), nullable=False)
    maternal_last_name  = Column(String(100), nullable=False)
    birth_day           = Column(DateTime(), nullable=True)
    date_hire           = Column(DateTime(), nullable=False)
    salary              = Column(Float, nullable=False)
    street_name         = Column(String(255), nullable=False)
    interior_number     = Column(String(4), nullable=False)
    exterior_number     = Column(String(4), nullable=False)
    neighborhood        = Column(String(255), nullable=False)
    zip_code            = Column(String(5), nullable=False)
    municipality        = Column(String(255), nullable=False)
    state               = Column(String(255), nullable=False)
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    active    = Column(Boolean(), nullable=False, default=True)

    def save(**kwargs):
        try:
            worker = Workers(**kwargs)
            db.session.add(worker)
            db.session.commit()
            return worker
        except Exception as error:
            print(error)
            return {}
        finally:
            pass

    def find():
        try:
            return Workers.query.filter_by().all()
        except:
            return {}
        finally:
            pass

    def find_one(**kwargs):
        try:
            return db.session.query(Workers).filter_by(**kwargs).first()
        except exc.SQLAlchemyError as err:
            print(err)
            return {}
        finally:
            db.session.close()

    def update(**update):
        try:
            update["updatedAt"] = datetime.now()
            updated = (
                db.session.query(Workers)
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
                db.session.query(Workers)
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