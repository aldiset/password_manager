# Import library
from sqlalchemy import Column, Integer, String
from app.database import Base

# Mendefinisikan model User
class User(Base):
    is_active = True
    is_authenticated = True
    
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    username = Column(String, unique=True)
    password = Column(String)
    
    def get_id(self):
        return self.id