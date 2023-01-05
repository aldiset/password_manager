import os
from flask import Flask, redirect, url_for, request, render_template, session
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from app.models.user import User
from app.models.account import Account
from crud import read, read_all, create, update, delete, get_user, get_account_by_user_id

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Change this!
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return read(model=User, id=int(user_id))

@app.route('/', methods=['GET'])
def index():
    return render_template('index1.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        user = User(name=name, email=email, username=username, password=password, role=role)
        create(user) #membuat user
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Mengambil data dari form login
        username = request.form['username']
        password = request.form['password']

        # Mencari data user di tabel users
        user = get_user(username=username, password=password)

        # Jika user ditemukan, masuk ke halaman home
        if user:
            session['user_id'] = user.id
            return redirect(url_for('home'))
        # Jika user tidak ditemukan, tampilkan pesan error
        else:
            error = 'Username atau password salah'
            print(error)
            return render_template('login.html', error=error)

    # Jika request bukan POST, render halaman login
    return render_template('login.html')

# Mendefinisikan route home
@app.route('/home')
def home():
    # Mengambil data user dari session
    user_id = session.get('user_id')
    accounts = get_account_by_user_id(user_id=user_id)

    # Render halaman home dengan data user
    return render_template('user.html', accounts=accounts)

if __name__ == '__main__':
    app.run(debug=True)