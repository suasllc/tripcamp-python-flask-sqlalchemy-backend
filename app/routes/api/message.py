from flask import Blueprint
from flask.json import jsonify

from app.db.models import Message, Medium, Review, User, UserProfile, utils_to_dict


bp = Blueprint('Messages', __name__, url_prefix='/api/messages')

@bp.route('/')
def messages_index():
  messages = Message.query.order_by(Message.id).all()
  data = [message.to_dict() for message in messages]
  return {"messages": data}

# @bp.route('/reviews')
# def messages_with_reviews_index():
#   messages = Message.query.order_by(Message.id).all()
#   data = [message.to_dict() for message in messages]
#   # data = [utils_to_dict(message) for message in messages]
#   # print("\n\n\n message dicts", data)
#   return {"messages": data}