from flask import (
  Blueprint, redirect, render_template, url_for, request, make_response, Response
)
# from flask.Response import set_cookie
import os

from flask.json import jsonify
from flask_login import current_user, login_user, logout_user, login_required


from ..forms import LoginForm, SinupForm
from ...db.models.user import User
from ...db.models.userprofile import UserProfile

# static_folder = os.path.join(os.pardir, 'static')
static_folder = './static'
print('\n\n\n static_folder', static_folder)

bp = Blueprint("session", __name__, static_folder=static_folder, static_url_path='')


@bp.route("/api/session", methods=["GET", "POST"])
def login():
  if current_user.is_authenticated:
    print('\n\n\n Authenticated', current_user.to_dict_safe())
    return jsonify({"user": current_user.to_dict_safe()})
  if request.method == 'GET':
    print('\n\n\n\n method = ', request.method)  
    return {"user": "undefined"}
  print('\n\n\n\n request.values.to_dict()', request.values, request.method)

  credential = request.values.to_dict()['credential']
  password = request.values.to_dict()['password']
  user = User()
  if credential.find('@') != -1:
    email = credential
    user = User.query.filter(User.email == email).first()
  else:
    username = credential
    user = User.query.filter(User.username == username).first()

  if not user or not user.check_password(password):
    return jsonify({"error": "unauthorize user"}), 401
  else:
    login_user(user)
    return jsonify({"user": user.to_dict_safe()})

@bp.route("/session/login", methods=["GET", "POST"])
def login_form():
  if current_user.is_authenticated:
      return redirect('/api/spots')
  form = LoginForm()
  if form.validate_on_submit():  
    n = form.username.data
    user = User.query.filter(User.username == n).first()
    if not user or not user.check_password(form.password.data):
        return redirect(url_for(".login_form"))
    login_user(user)
    return redirect('/api/spots')
  return render_template("login.html", form=form)


@bp.route('/session/logout', methods=['GET',"POST"])
def logout():
  logout_user()
  return redirect(url_for('.login'))

@bp.route('/session/signup', methods=['GET','POST'])
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

@bp.route('/session/profile')
@login_required
def profile():
  userProfile = UserProfile.query.filter(UserProfile.userId == current_user.id).first()
  return {"userProfile": userProfile.to_dict()}

@bp.route('/api/csrf/restore')
def setcookie():
  print('\n\n\n\n', dir(request))
  print('\n\n\n\n', request.cookies.to_dict())
  # if request.method == 'POST':
  resp = make_response("")
  # resp.set_cookie('XSRF-TOKEN',  request.cookies.to_dict()['XSRF-TOKEN'])

  return resp
  # return bp.send_static_file('index.html')

'''
  router.get('/api/csrf/restore', (req, res) => {
    res.cookie('XSRF-TOKEN', req.csrfToken());
    res.status(201).json({});
  });
'''