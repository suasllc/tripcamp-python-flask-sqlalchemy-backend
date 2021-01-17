from .db import db


class Medium(db.Model):
  __tablename__ = 'Media'

  id = db.Column(db.Integer, primary_key=True)
  url = db.Column(db.String(255), nullable=False, unique=True)
  name = db.Column(db.String(100), nullable=True)
  type = db.Column(db.String(25), nullable=True)
  source = db.Column(db.Integer, nullable=True)

  def to_dict(self):
    return {
      "id": self.id,
      "url": self.url,
      "name": self.name,
      "type": self.type,
      "source": self.source
    }

