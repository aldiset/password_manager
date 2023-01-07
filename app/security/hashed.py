from flask_bcrypt import generate_password_hash, check_password_hash

def hash(password):
    return generate_password_hash(password)

def check(pw_hash, password):
    return check_password_hash(pw_hash, password)