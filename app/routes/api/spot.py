from flask import Blueprint

from app.db.models.spot import Spot
from app.db.models.review import Review
from app.db.models.user import User
from app.db.models.userprofile import UserProfile


bp = Blueprint('Spots', __name__, url_prefix='/api/spots')

@bp.route('/')
def spots_index():
  spots = Spot.query.order_by(Spot.id).all()
  data = [spot.to_dict() for spot in spots]
  return {"Spots": data}