from app.database import session
from app.models.user import User
from app.models.account import Account


def create(data):
    session.add(data)
    session.commit()
    session.close()
    return data

def read(model, id):
    return session.query(model).filter(model.id == id).first()

def read_all(model):
    return session.query(model).all()

def update(model, id, data_update):
    data = session.query(model).filter(model.id == id).first()
    for key, value in data_update.items():
        setattr(data, key, value)
    session.commit()

def delete(model, id):
    data = session.query(model).filter(model.id == id).first()
    session.delete(data)
    session.commit()

def get_user(username, password):
    return session.query(User).filter(User.username == username, User.password == password).first()

def get_account_by_user_id(user_id):
    return session.query(Account).filter(Account.user_id == user_id).all()
