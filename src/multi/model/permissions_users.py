from sqlalchemy import Column, ForeignKey, String, DateTime, Boolean
from sqlalchemy import func, exc
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db
from datetime import datetime


class PermissionsClients(db.Model):

    __tablename__ = "permissions_clients"
    id              = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    id_person       = Column(UUID(as_uuid=True), ForeignKey("persons.id", ondelete="CASCADE", name="id_person"))
    id_permission   = Column(UUID(as_uuid=True), ForeignKey("permissions.id", ondelete="CASCADE", name="id_permission"))
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=True)
    active    = Column(Boolean(), nullable=False, default=True)

    def save(**kwargs):
        try:
            permission = PermissionsClients(**kwargs)
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
            return PermissionsClients.query.filter_by().all()
        except:
            return {}
        finally:
            pass

    def find_one(**kwargs):
        try:
            return db.session.query(PermissionsClients).filter_by(**kwargs).first()
        except exc.SQLAlchemyError as err:
            print(err)
            return {}
        finally:
            db.session.close()

    def update(**update):
        try:
            update["updatedAt"] = datetime.now()
            updated = (
                db.session.query(PermissionsClients)
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
                db.session.query(PermissionsClients)
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