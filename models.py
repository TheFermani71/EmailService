from sqlalchemy import Column, Integer, String
from database import Base

class Subscriber(Base):
    __tablename__ = 'subscribers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)

    def __repr__(self):
        return f"<Subscriber(name='{self.name}', email='{self.email}')>"
