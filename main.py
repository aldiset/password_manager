import os
from flask import Flask, redirect, url_for, request, render_template, session
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin

from app.models.user import User
from app.models.account import Account
from app.database.crud import CRUDUser as user, CRUDAccount as account

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Change this!
login_manager = LoginManager()
login_manager.init_app(app)


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
        password = request.form['password']
        
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
        data_user = user.login(username=username, password=password)

        # Jika user ditemukan, masuk ke halaman home
        if data_user is not None:
            session['user_id'] = data_user.id
            return redirect(url_for('home'))

        # Jika user tidak ditemukan, tampilkan pesan error
        else:
            error = 'Username atau password salah'
            return render_template('login.html', error=error)

    # Jika request bukan POST, render halaman login
    return render_template('login.html')

# Mendefinisikan route home
@app.route("/home", methods=['POST','GET'])
def home():
    is_success = None
    # Mengambil data user dari session
    user_id = session.get('user_id')

    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        
        object = Account(name=name, username=username, password=password, user_id=user_id)
        account.add(object=object)
        is_success = "Success"    
    accounts = account.get_by_user_id(user_id=user_id)
    return render_template('user.html', is_success=is_success, accounts=accounts)

@app.route("/home/<int:id>", methods=['UPDATE'])
def update_account(id):
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    account.update(id=id, name=name, username=username, password=password)
    redirect(url_for('home'))

@app.route("/home/<int:id>", methods=['DELETE', 'GET'])
def delete_account(id):
    account.delete(id=id)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)