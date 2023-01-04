# Membuat objek engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root@localhost/password_manager')

# Membuat objek Base
Base = declarative_base()

# Membuat objek sesi
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()
