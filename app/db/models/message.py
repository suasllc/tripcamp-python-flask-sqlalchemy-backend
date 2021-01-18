from .db import db


class Message(db.Model):
  __tablename__ = 'Messages'

  id = db.Column(db.Integer, primary_key=True)
  senderId = db.Column(db.Integer, nullable=False)
  recipientId = db.Column(db.Integer, nullable=False)
  body = db.Column(db.Text, nullable=False)
  status = db.Column(db.Integer, nullable=True, default=0)

  def to_dict(self):
    return {
      "id": self.id,
      "url": self.url,
      "name": self.name,
      "type": self.type,
      "source": self.source
    }

