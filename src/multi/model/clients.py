from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy import func, exc
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db
from datetime import datetime


class Clients(db.Model):

    __tablename__ = "clients"
    id              = Column(UUID(as_uuid=True), primary_key=True, default=uuid4())
    code            = Column(String(255), nullable=False)
    business_name   = Column(String(255), nullable=False)
    rfc             = Column(String(18), nullable=False)
    street_name     = Column(String(255), nullable=False)
    phone_number    = Column(String(255), nullable=False)
    interior_number = Column(String(4), nullable=True)
    exterior_number = Column(String(4), nullable=True)
    neighborhood    = Column(String(255), nullable=False)
    state           = Column(String(255), nullable=False)
    zip_code        = Column(String(5), nullable=False)
    logo            = Column(String(255), nullable=True)
    startedAt = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())
    deletedAt = Column(DateTime(timezone=True), nullable=True)
    active    = Column(Boolean(), nullable=False, default=True)

    def save(**kwargs):
        try:
            client = Clients(**kwargs)
            db.session.add(client)
            db.session.commit()
            return client
        except Exception as error:
            print(error)
            return {}
        finally:
            pass

    def find():
        try:
            return Clients.query.filter_by().all()
        except:
            return {}
        finally:
            pass

    def find_one(**kwargs):
        try:
            return db.session.query(Clients).filter_by(**kwargs).first()
        except exc.SQLAlchemyError as err:
            print(err)
            return {}
        finally:
            db.session.close()

    def update(**update):
        try:
            update["updatedAt"] = datetime.now()
            updated = (
                db.session.query(Clients)
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
            update = (
                db.session.query(Clients).filter_by(**kwargs)
                .update(
                    # Tu pusiste deleteAt pero es deletedAt, al rato corrijo esos v:
                    {"activate" : False, "deletedAt" : datetime.now()},
                    synchronize_session = "fetch"
                )
            )
            db.session.commit()
            return update
        except exc.SQLAlchemyError as err:
            print (err)
            db.session.rollback()
            return {}