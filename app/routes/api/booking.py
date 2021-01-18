from flask import Blueprint, request
from sqlalchemy import or_, and_
from flask_login import current_user, login_required, login_user

from app.db.models import Booking, Spot, User, UserProfile


bp = Blueprint('Bookings', __name__, url_prefix='/api/bookings')

@bp.route('/')
# @login_required
def bookings_index():
  # if not current_user.is_authenticated:
  #   user = User.query.get(1)
  #   login_user(user)
  # bookings = Booking.query.order_by(Booking.id).all()
  # data = [booking.to_dict() for booking in bookings]
  print('\n\n\n bookings', current_user.is_authenticated, current_user.id) 

  # if current_user.is_anonymous: return { 'bookings': []}

  myTripBookings = Booking.query \
    .filter(Booking.userId == current_user.id) \
    .order_by(Booking.id) \
    .all()
  myTripData = [booking.to_dict() for booking in myTripBookings]
    
  mySpotIds = list(map(lambda spot: spot.id, current_user.spots))
  print('\n\n mySpotIds', mySpotIds)
  bookingsOfMyProps = Booking.query \
    .filter(Booking.spotId.in_(mySpotIds)) \
    .order_by(Booking.id) \
    .all()
  bookingsOfMyPropsData = [booking.to_dict() for booking in bookingsOfMyProps]
  print('\n\n bookings',  bookingsOfMyPropsData) 
  return { "Bookings": bookingsOfMyPropsData}

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