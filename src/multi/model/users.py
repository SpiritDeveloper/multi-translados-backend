from sqlalchemy import Column, ForeignKey, String, DateTime, Boolean
from sqlalchemy import func, exc
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db
from datetime import datetime


class Users(db.Model):

    __tablename__ = "users"
    id        = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    name                = Column(String(100), nullable=False)
    paternal_last_name  = Column(String(100), nullable=False)
    maternal_last_name  = Column(String(100), nullable=False)
    email               = Column(String(80), nullable=False)
    password            = Column(String(20), nullable=False)
    id_position         = Column(UUID(as_uuid=True), ForeignKey("positions.id", ondelete="CASCADE", name="id_position"))
    profile_photo       = Column(String(255), nullable=False)
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=True)
    active    = Column(Boolean(), nullable=False, default=True)

    def save(**kwargs):
        try:
            user = Users(**kwargs)
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
            return Users.query.filter_by().all()
        except:
            return {}
        finally:
            pass

    def find_one(**kwargs):
        try:
            return db.session.query(Users).filter_by(**kwargs).first()
        except exc.SQLAlchemyError as err:
            print(err)
            return {}
        finally:
            pass

    def updated(**update):
        try:
            
            updated = (
                db.session.query(Users)
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
                db.session.query(Users)
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