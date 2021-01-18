from flask import Blueprint
from flask.json import jsonify
from sqlalchemy import or_, and_

from app.db.models import Relationship, Medium, Review, User, UserProfile, utils_to_dict


bp = Blueprint('Relationships', __name__, url_prefix='/api/relationships')

@bp.route('/users/<int:id>')
def relationships_index(id):
  relationships = Relationship.query.filter(or_(Relationship.user1Id == id, Relationship.user2Id == id)).order_by(Relationship.id).all()
  data = [relatnship.to_dict() for relatnship in relationships]
  myFriends = Relationship.query \
    .filter(and_(or_(Relationship.user1Id == id, \
      Relationship.user2Id == id)), \
      Relationship.status == 1) \
    .order_by(Relationship.id).all()
  myF = [relatnship.to_dict() for relatnship in myFriends]
  myRequests = Relationship.query.filter(and_(Relationship.lastActionUserId == id, Relationship.status == 0)).order_by(Relationship.id).all()
  myR = [relatnship.to_dict() for relatnship in myRequests]
  theirRequests = Relationship.query.filter(and_(Relationship.lastActionUserId != id, \
    Relationship.status == 0, \
    or_(Relationship.user1Id == id, Relationship.user2Id == id))) \
    .order_by(Relationship.id).all()
  theirR = [relatnship.to_dict() for relatnship in theirRequests]
  myFollowers = Relationship.query \
    .filter(or_(Relationship.followingship == 1, \
      or_(and_(Relationship.user1Id == id, Relationship.followingship == 21), \
        and_(Relationship.user2Id == id, Relationship.followingship == 12)))) \
    .order_by(Relationship.id).all()
  myFlers = [relatnship.to_dict() for relatnship in myFollowers]    
  myFollowings = Relationship.query \
    .filter(or_(Relationship.followingship == 1, \
      or_(and_(Relationship.user1Id == id, Relationship.followingship == 12), \
        and_(Relationship.user2Id == id, Relationship.followingship == 21)))) \
    .order_by(Relationship.id).all()
  myFlings = [relatnship.to_dict() for relatnship in myFollowers]
  return {"relationships": {"all": data, "myRequests": myR, \
    'theirRequests': theirR, 'myFriends': myF, \
    'myFollowers': myFlers, 'myFollowings': myFlings}}
  # return {"relationships": {'myFriends': myF}}
