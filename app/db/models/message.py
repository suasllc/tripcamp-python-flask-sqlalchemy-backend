from .db import db


class Message(db.Model):
  __tablename__ = 'Messages'

  id = db.Column(db.Integer, primary_key=True)
  senderId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
  recipientId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
  body = db.Column(db.Text, nullable=False)
  status = db.Column(db.Integer, nullable=True, default=0)

  sender = db.relationship('User', foreign_keys=[senderId])
  recipient = db.relationship('User', foreign_keys=[recipientId])

  def to_dict(self):
    return {
      "id": self.id,
      "senderId": self.senderId,
      "recipientId": self.recipientId,
      "body": self.body,
      "status": self.status
    }

