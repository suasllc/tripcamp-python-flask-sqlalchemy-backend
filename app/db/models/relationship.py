from .db import db


class Relationship(db.Model):
  __tablename__ = 'Relationships'

  id = db.Column(db.Integer, primary_key=True)
  user1Id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
  user2Id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
  status = db.Column(db.Integer, nullable=False)
  lastActionUserId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
  followingship = db.Column(db.Integer, nullable=False)

  # user1 = db.relationship('User')
  # user2 = db.relationship('User')


  def to_dict(self):
    return {
      "id": self.id,
      "user1Id": self.user1Id,
      "user2Id": self.user2Id,
      "status": self.status,
      "lastActionUserId": self.lastActionUserId,
      "followingship": self.followingship,
      # "user": self.user.to_dict_safest(),
    }

