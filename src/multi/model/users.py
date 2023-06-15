from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from .. import db


class Users(db.Model):

    __tablename__ = "users"
    id = Column(String(255), primary_key=True, default='')
    firstName = Column(String(25), nullable=False)
    lastName = Column(String(60), nullable=False)
    email = Column(String(80), nullable=False)
    description = Column(String(255))
    password = Column(String(20), nullable=False)
    url = Column(String(800), nullable=True)

    def __repr__(self):
        return "<User {}>".format(self.username)