from app.database import session
from app.models.user import User
from app.models.account import Account

class CRUDUser:
    def add(object):
        session.add(object)
        session.commit()
        session.close()
        return True
    
    def get_by_id(id: int):
        return session.query(User).filter(User.id == id).first()
    
    def get_user_by_username(username):
        return session.query(User).filter(User.username == username).first()


class CRUDAccount:
    def add(object):
        session.add(object)
        session.commit()
        session.close()
        return True
    
    def get_by_id(id):
        return session.query(Account).filter(Account.id == id).first()
        
    def get_by_user_id(user_id):
        return session.query(Account).filter(Account.user_id==user_id).all()
    
    def update(id, name, username, password):
        account = session.query(Account).filter(Account.id == id).first()
        account.name = name
        account.username = username
        account.password = password
        session.commit()
        session.close()
        return True

    def delete(id):
        account = session.query(Account).filter(Account.id == id).first()
        session.delete(account)
        session.commit()
        session.close()
        return True