from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt
from .db import db
import string


class User(db.Model, UserMixin):
  __tablename__ = 'Users'

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(30), nullable=False, unique=True)
  email = db.Column(db.String(256), nullable=False, unique=True)
  hashedPassword = db.Column(db.String(60), nullable=False, unique=True)

  reviews = db.relationship('Review')
  userProfile = db.relationship('UserProfile')
  # messages = db.relationship('Message', foreign_keys=["User.senderId"])
  # messages = db.relationship('Message', foreign_keys=["User.recipientId"])

  def save(self):
    db.session.add(self)
    db.session.commit()


  def to_dict_safe(self):
    if self.userProfile:
      return {
        "id": self.id,
        "username": self.username,
        "userProfile": self.userProfile[0].to_dict_safe()
      }
    else:
      return {
        "id": self.id,
        "username": self.username,
      }

  def to_dict_safest(self):
    if self.userProfile:
      return {
        "username": self.username,
        "userProfile": self.userProfile[0].to_dict_safe()
      }
    else:
      return {
        "id": self.id,
        "username": self.username,
      }

  @property
  def password(self):
    return self.hashedPassword

  @password.setter
  def password(self, password):
    # self.hashedPassword = generate_password_hash(password)
    self.hashedPassword = User.make_password_hash(password)

  # @property
  # def username(self):
  #   return self.username
  
  # @username.setter
  # def username(self, uname):
  #   self.username = uname

  # @property
  # def email(self):
  #   return self.email
  
  # @email.setter
  # def email(self, eemail):
  #   self.email = eemail

  def check_password(self, password):
    # return check_password_hash(self.hashedPassword, password)  
    pwd = str(password).encode('utf-8')
    return bcrypt.checkpw(pwd, self.hashedPassword.tobytes())
  
  @staticmethod
  def make_password_hash(password):
    hash = bcrypt.hashpw(password=password.encode('utf-8'), salt=bcrypt.gensalt())
    return hash.decode('utf-8')
