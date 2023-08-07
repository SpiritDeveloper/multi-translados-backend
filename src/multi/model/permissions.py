from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy import func, exc
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db
from datetime import datetime


class Permissions(db.Model):

    __tablename__ = "permissions"
    id          = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    view        = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    active    = Column(Boolean(), nullable=False, default=True)

    def save(**kwargs):
        try:
            permission = Permissions(**kwargs)
            db.session.add(permission)
            db.session.commit()
            return permission
        except Exception as error:
            print(error)
            return {}
        finally:
            pass

    def find():
        try:
            return Permissions.query.filter_by().all()
        except:
            return {}
        finally:
            pass

    def find_one(**kwargs):
        try:
            return db.session.query(Permissions).filter_by(**kwargs).first()
        except exc.SQLAlchemyError as err:
            print(err)
            return {}
        finally:
            db.session.close()

    def update(**update):
        try:
            update["updatedAt"] = datetime.now()
            updated = (
                db.session.query(Permissions)
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
                db.session.query(Permissions)
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
