import bcrypt
from flask_jwt_extended import create_access_token
from app.models import User
from app.extensions import db

def hash_password(plain: str):
    # Garante que o decode seja compatível
    return bcrypt.hashpw(plain.encode(), bcrypt.gensalt()).decode('utf-8')

def check_password(plain: str, hashed: str):
    return bcrypt.checkpw(plain.encode(), hashed.encode())

def create_user(email: str, password: str):
    # Verifica se o usuário já existe
    if User.query.filter_by(email=email).first():
        raise ValueError("Usuário já existe com este e-mail.")
    user = User(email=email, password=hash_password(password))
    db.session.add(user)
    db.session.commit()
    return user

def authenticate(email: str, password: str):
    user = User.query.filter_by(email=email).first()
    if user and check_password(password, user.password):
        return create_access_token(
            identity=str(user.id),
            additional_claims={"email": user.email}
        )
    return None