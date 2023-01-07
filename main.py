import os
from flask import Flask, redirect, url_for, request, render_template, session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

from app.models.user import User
from app.models.account import Account
from app.database.crud import CRUDUser as user, CRUDAccount as account
from app.security.hashed import hash, check

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Change this!
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return user.get_by_id(id=user_id)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        # mengambil data dari form
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = hash(request.form['password'])
        
        # membuat object
        object = User(name=name, email=email, username=username, password=password)
        # input data ke database
        user.add(object=object)

        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Mengambil data dari form login
        username = request.form['username']
        password = request.form['password']

        # Mencari data user di tabel users
        data_user = user.get_user_by_username(username=username)

        # Jika user ditemukan, masuk ke halaman home
        if data_user and check(data_user.password, password):
            session['user_id'] = data_user.id
            login_user(data_user)
            return redirect(url_for('user_page'))

        message = 'Username atau password salah'
        return render_template('login.html', message=message)

    # Jika request bukan POST, render halaman login
    return render_template('login.html')

@app.route('/logout', methods=['GET'])
@login_required
def logout():
    try:
        logout_user()
    except Exception as err:
        print(err)
    finally:
        return redirect(url_for("login"))

@app.route("/user", methods=['GET'])
@login_required
def user_page():
    # Mengambil data user dari session
    try:
        accounts = Account
        if current_user:
            user_id = session.get('user_id') if not session.get('user_id') else current_user.id
            accounts = account.get_by_user_id(user_id=user_id)
        return render_template('user.html', accounts=accounts)
    except Exception as err:
        print(err)
    
    return redirect(url_for('index'))

@app.route("/account/add", methods=['POST', 'GET'])
@login_required
def add_account():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        user_id = session.get('user_id')
        
        object = Account(name=name, username=username, password=password, user_id=user_id)
        account.add(object=object)
    return redirect(url_for('user_page'))

@app.route("/account/update/<int:id>", methods=['POST','GET'])
@login_required
def update_account(id):
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        account.update(id=id, name=name, username=username, password=password)
        return redirect(url_for('user_page'))
    data = account.get_by_id(id)
    return render_template('edit.html', account=data)

@app.route("/account/delete/<int:id>", methods=['DELETE', 'GET'])
@login_required
def delete_account(id):
    account.delete(id=id)
    return redirect(url_for('user_page'))


if __name__ == '__main__':
    app.run(debug=True)