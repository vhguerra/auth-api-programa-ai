import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', "dev-secret-key")
    SQLALCHEMY_DATABASE_URI =os.environ.get('SECRET_KEY', "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY' , "DEV-JWT-SECRET" )
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # 1 hour
    API_KEYS = os.environ.get('API_KEYS',"dev-key")
    API_KEYS_HEADER = os.environ.get('API_KEYS_HEADER',"X-API-KEY")