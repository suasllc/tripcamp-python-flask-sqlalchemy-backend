from .db import db
from .medium import Medium
from .utils import getUrls, utils_to_dict, attrs
from pprint import pprint
from json import JSONEncoder
class MyEncoder(JSONEncoder):
  def default(self, o):
    return o.__dict__  

class Spot(db.Model):
  __tablename__ = 'Spots'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False, unique=True)
  description = db.Column(db.Text, nullable=False)
  units = db.Column(db.Integer, nullable=False, default=1)
  gpsLocation = db.Column(db.Float, nullable=False)
  mediaUrlIds = db.Column(db.Integer, nullable=True)
  streetAddress = db.Column(db.String(255), nullable=True)
  city = db.Column(db.String(100), nullable=True)
  stateProvince = db.Column(db.String(100), nullable=True)
  zipCode = db.Column(db.Integer, nullable=True)
  country = db.Column(db.String(100), nullable=True)
  perNightRate = db.Column(db.Float, nullable=True)
  accommodationType = db.Column(db.Integer, nullable=True, default=0)
  website = db.Column(db.String(255), nullable=True)

  reviews = db.relationship('Review')

  def to_dict(self):
    # dct = utils_to_dict(self, 'mediaUrlIds', 'reviews', 'query')
    return {
      "id": self.id,
      "name": self.name,
      "description": self.description,
      "units": self.units,
      "gpsLocation": self.gpsLocation,
      # "mediaUrlIds": self.mediaUrlIds,
      # "urls": self.getUrls(),
      "urls": getUrls(self.mediaUrlIds),
      "streetAddress": self.streetAddress,
      "city": self.city,
      "stateProvince": self.stateProvince,
      "zipCode": self.zipCode,
      "country": self.country,
      "perNightRate": self.perNightRate,
      "accommodationType": self.accommodationType,
      "website": self.website,
      "reviews": [review.to_dict() for review in self.reviews]
    }
