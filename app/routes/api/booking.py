from flask import Blueprint
from sqlalchemy import or_, and_
from flask_login import current_user, login_required

from app.db.models.booking import Booking
from app.db.models.spot import Spot
from app.db.models.user import User
from app.db.models.userprofile import UserProfile


bp = Blueprint('Bookings', __name__, url_prefix='/api/bookings')

@bp.route('/')
@login_required
def bookings_index():
  bookings = Booking.query.order_by(Booking.id).all()
  data = [booking.to_dict() for booking in bookings]
  return {"Bookings": data}

# @bp.route('/<int:bookingId>')
# def bookings_id(bookingId):


'''
router.get('/',
  requireAuth,
  asyncHandler(async (req, res, next) => {
    const userId = req.user.id;
    try {
      const user = await User.findByPk(userId, {
        include: { model: Spot, through: Ownership }
      });
      const spotIds = user.Spots.map(spot => spot.id);

      const myTripBookings = await Booking.findAll({
        where: {
          userId,
        },
        order: [['id', 'ASC']]
      });
      const bookingsOfMyProps = await Booking.findAll({
        where: {
          spotId: spotIds
        },
        order: [['id', 'ASC']],
        include: User
      });
      res.json({ bookings: [...myTripBookings, ...bookingsOfMyProps] });
    } catch (e) {
      return next(errorToSend(401, 'Booking failed', ["no bookings found"]));
    }
  })
);
router.delete('/:bookingId',
  requireAuth,
  asyncHandler(async (req, res, next) => {
    const bookingInDatabase = await Booking.findByPk(req.params.bookingId);
    if (!bookingInDatabase || req.user.id !== bookingInDatabase.userId) {
      return next(errorToSend(401, 'Booking failed', ["Unauthorized user"]));
    }
    //TODO: implement backend booking validation before attempting to create a row in database
    try {
      await bookingInDatabase.destroy();
      res.json({ bookingId: req.params.bookingId });
    } catch (error) {
      return next(errorToSend(401, 'Booking failed', [error]));
    }
  })
);
'''