from .db import db


class Relationship(db.Model):
  __tablename__ = 'Relationships'

  id = db.Column(db.Integer, primary_key=True)
  user1Id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
  user2Id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
  status = db.Column(db.Integer, nullable=False)
  lastActionUserId = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
  followingship = db.Column(db.Integer, nullable=False)

  user1 = db.relationship('User', foreign_keys=user1Id)
  user2 = db.relationship('User', foreign_keys=user2Id)


  def to_dict(self):
    return {
      "id": self.id,
      "user1Id": self.user1Id,
      "user2Id": self.user2Id,
      "status": self.status,
      "lastActionUserId": self.lastActionUserId,
      "followingship": self.followingship,
      "user1": self.user1.to_dict_safest(),
      "user2": self.user2.to_dict_safest(),
    }

