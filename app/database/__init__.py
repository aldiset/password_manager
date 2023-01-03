# Membuat objek engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('mysql://root:root@localhost/password_manager')

# Membuat objek Base
Base = declarative_base()

# Membuat tabel users jika belum ada
Base.metadata.create_all(engine)

# Membuat objek sesi
Session = sessionmaker(bind=engine)
