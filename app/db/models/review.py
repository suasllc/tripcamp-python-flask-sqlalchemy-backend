from .db import db


class Review(db.Model):
  __tablename__ = 'Reviews'

  id = db.Column(db.Integer, primary_key=True)
  userId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
  spotId = db.Column(db.Integer, db.ForeignKey("Spots.id"), nullable=False)
  title = db.Column(db.String(255), nullable=False)
  body = db.Column(db.Text, nullable=False)
  rating = db.Column(db.Integer, nullable=False)
  upvotes = db.Column(db.Integer, nullable=True, default=0)
  mediaUrlIds = db.Column(db.Integer, nullable=True)
  type = db.Column(db.Integer, nullable=False, default=0)

  spot = db.relationship('Spot')
  user = db.relationship('User')


  def to_dict(self):
    return {
      "id": self.id,
      "userId": self.userId,
      "spotId": self.spotId,
      "title": self.title,
      "body": self.body,
      "rating": self.rating,
      "upvotes": self.upvotes,
      "mediaUrlIds": self.mediaUrlIds,
      "type": self.type,
      "user": self.user.to_dict_safest()
    }

