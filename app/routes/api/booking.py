from flask import Blueprint

from app.db.models.booking import Booking
from app.db.models.spot import Spot
from app.db.models.user import User
from app.db.models.userprofile import UserProfile


bp = Blueprint('Bookings', __name__, url_prefix='/api/bookings')

@bp.route('/')
def bookings_index():
  bookings = Booking.query.order_by(Booking.id).all()
  data = [booking.to_dict() for booking in bookings]
  return {"Bookings": data}