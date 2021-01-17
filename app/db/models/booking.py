from .db import db


class Booking(db.Model):
  __tablename__ = 'Bookings'

  id = db.Column(db.Integer, primary_key=True)
  userId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
  spotId = db.Column(db.Integer, db.ForeignKey("Spots.id"), nullable=False)
  startDate = db.Column(db.Date, nullable=False)
  endDate = db.Column(db.Date, nullable=False)
  guests = db.Column(db.Integer, nullable=False)
  status = db.Column(db.Integer, nullable=False)
  specialRequest = db.Column(db.Text, nullable=True)
  cost = db.Column(db.Float, nullable=True)

  spot = db.relationship('Spot')
  user = db.relationship('User')


  def to_dict(self):
    return {
      "id": self.id,
      "userId": self.userId,
      "spotId": self.spotId,
      "startDate": self.startDate,
      "endDate": self.endDate,
      "guests": self.guests,
      "status": self.status,
      "specialRequest": self.specialRequest,
      "cost": self.cost,
      "user": self.user.to_dict_safest(),
      "spot": self.spot.to_dict()
    }

