from .db import db


class UserProfile(db.Model):
  __tablename__ = 'UserProfiles'

  id = db.Column(db.Integer, primary_key=True)
  userId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False, unique=True)
  firstName = db.Column(db.String(50), nullable=False)
  lastName = db.Column(db.String(50), nullable=False)
  mediaUrlIds = db.Column(db.Integer, nullable=True)
  streetAddress = db.Column(db.String(255), nullable=True)
  city = db.Column(db.String(100), nullable=True)
  stateProvince = db.Column(db.String(100), nullable=True)
  zipCode = db.Column(db.Integer, nullable=True)
  country = db.Column(db.String(100), nullable=True)
  gpsLocation = db.Column(db.Float, nullable=True)
  type = db.Column(db.Integer, nullable=True)
  favorites = db.Column(db.Integer, nullable=True)
  rank = db.Column(db.Integer, nullable=True)
  followers = db.Column(db.Integer, nullable=True)
  followings = db.Column(db.Integer, nullable=True)
  cashEarned = db.Column(db.Float, nullable=True)
  cashSpent = db.Column(db.Float, nullable=True)
  badge = db.Column(db.String(50), nullable=True)

  # user = db.relationship('User')

  def to_dict(self):
    return {
      "id": self.id,
      "userId": self.userId,
      "firstName": self.firstName,
      "lastName": self.lastName,
      "mediaUrlIds": self.mediaUrlIds,
      "streetAddress": self.streetAddress,
      "city": self.city,
      "stateProvince": self.stateProvince,
      "zipCode": self.zipCode,
      "country": self.country,
      "gpsLocation": self.gpsLocation,
      "type": self.type,
      "favorites": self.favorites,
      "rank": self.rank,
      "followers": self.followers,
      "followings": self.followings,
      "cashEarned": self.cashEarned,
      "cashSpent": self.cashSpent,
      "badge": self.badge
    }

  def to_dict_safe(self):
    return {
      "firstName": self.firstName,
      "lastName": self.lastName,
      "country": self.country,
      "badge": self.badge
    }

