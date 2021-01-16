import os


class Configuration:
  SECRET_KEY=os.environ.get('SECRET_KEY')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  
  JWT_SECRET = os.environ.get('JWT_SECRET')
  JWT_EXPIRES_IN = os.environ.get('JWT_EXPIRES_IN')
