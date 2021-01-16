from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user, login_required
from ..forms import LoginForm, SinupForm
from ...db.models.user import User
from ...db.models.userprofile import UserProfile

bp = Blueprint("session", __name__, url_prefix="/session")


@bp.route("/", methods=["GET", "POST"])
def login():
  if current_user.is_authenticated:
      return redirect('/api/spots')
  form = LoginForm()
  if form.validate_on_submit():  
    n = form.username.data
    user = User.query.filter(User.username == n).first()
    if not user or not user.check_password(form.password.data):
        return redirect(url_for(".login"))
    login_user(user)
    return redirect('/api/spots')
  return render_template("login.html", form=form)


@bp.route('/logout', methods=['GET',"POST"])
def logout():
  logout_user()
  return redirect(url_for('.login'))

@bp.route('/signup', methods=['GET','POST'])
def signup():
  form = SinupForm()
  if form.validate_on_submit():  
    n = form.username.data
    user = User.query.filter(User.username == n).first()
    if not user:
      user_dict['username'] = form.username.data
      user_dict['email'] = form.email.data
      user_dict['hashedPassword'] = User.make_password_hash(form.hashedPassword)
      user1 = User(user_dict)
      user1.save()
      login(user1)
    else:
      login_user(user)
    return redirect('/api/spots')  
  return render_template('signup.html', form=form)

@bp.route('/profile')
@login_required
def profile():
  userProfile = UserProfile.query.filter(UserProfile.userId == current_user.id).first()
  return {"userProfile": userProfile.to_dict()}
