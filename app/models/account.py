# Import library
from sqlalchemy import Column, Integer, String
from app.database import Base

# Mendefinisikan model Account
class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    password = Column(String)
    url = Column(String)
    user_id = Column(Integer)
