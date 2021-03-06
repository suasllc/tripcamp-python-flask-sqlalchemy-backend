from flask import Blueprint
from flask.json import jsonify

from app.db.models import Spot, Medium, Review, User, UserProfile, utils_to_dict


bp = Blueprint('Spots', __name__, url_prefix='/api/spots')

@bp.route('/')
def spots_index():
  spots = Spot.query.order_by(Spot.id).all()
  data = [spot.to_dict() for spot in spots]
  return {"Spots": data}

@bp.route('/reviews')
def spots_with_reviews_index():
  spots = Spot.query.order_by(Spot.id).all()
  data = [spot.to_dict() for spot in spots]
  # data = [utils_to_dict(spot) for spot in spots]
  # print("\n\n\n spot dicts", data)
  return {"spots": data}