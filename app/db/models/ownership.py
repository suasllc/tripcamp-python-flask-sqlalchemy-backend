from .db import db


class Ownership(db.Model):
  __tablename__ = 'Ownerships'

  id = db.Column(db.Integer, primary_key=True)
  userId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
  spotId = db.Column(db.Integer, db.ForeignKey("Spots.id"), nullable=False)
  status = db.Column(db.Integer, nullable=True, default=0)

  spot = db.relationship('Spot', foreign_keys=spotId)
  user = db.relationship('User', foreign_keys=userId)


  def to_dict(self):
    return {
      "id": self.id,
      "userId": self.userId,
      "spotId": self.spotId,
    }

