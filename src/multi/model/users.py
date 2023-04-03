from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from sqlalchemy import exc

from sqlalchemy.orm import relationship
from ..conection import db, session


class Users(db):

    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=lambda: uuid4().hex)
    firstName = Column(String(25), nullable=False)
    lastName = Column(String(60), nullable=False)
    email = Column(String(80), nullable=False)
    description = Column(String(255))
    password = Column(String(20), nullable=False)
    url = Column(String(800), nullable=True)

    def find(**kwargs):
        try:
            return session.query(Users).filter_by(**kwargs).all()
        except exc.SQLAlchemyError as err:
            print(err)
            return {}
        finally:
            session.close()

    def find_one(**kwargs):
        try:
            return session.query(Users).filter_by(**kwargs).first()
        except exc.SQLAlchemyError as err:
            print(err)
            return {}
        finally:
            session.close()

    def create(**request):
        try:       
            user = Users(**request)
            session.add(user)
            session.commit()
            return user
        except exc.SQLAlchemyError as err:
            print(err)
            session.rollback()
            return {}
        

    def updated(**update) -> int:
        try:  
            update["updateAt"] = datetime.now()
            updated = (
                session.query(Users)
                .filter_by(id=str(update["id"]))
                .update(update, synchronize_session="fetch")
            )
            session.commit()
            return updated
        except exc.SQLAlchemyError as err:
            print(err)
            session.rollback()
            return {}
    

    def delete(**kwargs: any) -> int:
        try:        
            updated = (
                session.query(Users)
                .filter_by(**kwargs)
                .update(
                    {"active": False, "deleteAt": datetime.now()},
                    synchronize_session="fetch",
                )
            )
            session.commit()
            return updated
        except exc.SQLAlchemyError as err:
            print(err)
            session.rollback()
            return {}
        
