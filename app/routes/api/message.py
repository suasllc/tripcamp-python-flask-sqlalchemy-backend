from flask import Blueprint, request
from flask.json import jsonify
from sqlalchemy import or_, and_
from flask_login import current_user, login_required

from app.db.models import Message, Medium, Review, User, UserProfile, utils_to_dict


bp = Blueprint('Messages', __name__, url_prefix='/api/messages')

@bp.route('/')
@login_required
def messages_index():
  messages = Message.query \
    .filter(or_(Message.senderId == current_user.id, Message.recipientId == current_user.id)) \
    .order_by(Message.id).all()
  data = [message.to_dict() for message in messages]
  return {"messages": data}

@bp.route('/friends/<int:friendId>')
@login_required
def messages_fid_index(friendId):
  messages = Message.query \
    .filter(or_(and_(Message.senderId == current_user.id, Message.recipientId == friendId), \
      and_(Message.recipientId == current_user.id, Message.senderId == friendId))) \
    .order_by(Message.id).all()
  data = [message.to_dict() for message in messages]
  return {"messages": data}

'''
router.get('/',
  requireAuth,
  asyncHandler(async (req, res, next) => {
    const myId = req.user.id;
    if (!myId) {
      return next(errorToSend(401, 'Getting messages failed', ["Unauthorized user"]));
      //TODO: check this myId again the id sent by the user from frontend?
    }
    try {
      const messages = await Message.findAll({
        where: {
          [Op.or]: [
            { senderId: myId },
            { recipientId: myId }
          ],
        },
        order: [['createdAt', 'ASC']]
      })
      res.json({ messages });
    } catch (e) {
      return next(errorToSend(401, 'Getting messages failed', ["Error in posting the message"]));
    }
  })
);

router.get('/friends/:friendId',
  requireAuth,
  asyncHandler(async (req, res, next) => {
    const myId = req.user.id;
    const friendId = req.params.friendId;
    if (!myId) {
      return next(errorToSend(401, 'Getting messages failed', ["Unauthorized user"]));
      //TODO: check this myId again the id sent by the user from frontend?
    }
    try {
      const messages = await Message.findAll({
        where: {
          [Op.or]: [
            { senderId: myId, recipientId: friendId},
            { senderId: friendId, recipientId: myId }
          ],
        },
        order: [['createdAt', 'ASC']]
      })
      res.json({ messages });
    } catch (e) {
      return next(errorToSend(401, 'Getting messages failed', ["Error in posting the message"]));
    }
  })
);

router.post('/',
  requireAuth,
  asyncHandler(async (req, res, next) => {
    const messageDataObj = req.body.message;
    console.log('messageDataObj', messageDataObj);
    if (req.user.id !== messageDataObj.senderId) {
      // console.log(req.user.id, messageDataObj.senderId, "Unauthorized user");
      return next(errorToSend(401, 'Getting messages failed', ["Unauthorized user"]));
    }
    //TODO: implement backend message validation before attempting to create a row in database
    try {
      const message = await Message.create(messageDataObj);
      res.json({ message });
    } catch (error) {
      return next(errorToSend(401, 'Getting messages failed', ["Error in posting the message"]));
    }
  })
);
router.patch('/:id',
  requireAuth,
  asyncHandler(async (req, res, next) => {
    const messageDataObj = req.body.message;
    // console.log('messageDataObj', messageDataObj);
    if (req.user.id !== messageDataObj.senderId) {
      return next(errorToSend(401, 'Getting messages failed', ["Unauthorized user"]));
    }
    //TODO: implement backend message validation before attempting to create a row in database
    try {
      const message = await Message.findByPk(Number(req.params.id));
      message.update({ status: 1 });
      res.json({ message });
    } catch (error) {
      return next(errorToSend(401, 'Getting messages failed', ["Error in posting the message"]));
    }
  })
);
'''