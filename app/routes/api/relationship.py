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
  # return {"relationships": {"all": data, "myRequests": myR, 'myFriends': myF}}
  return {"relationships": {'myFriends': myF}}
