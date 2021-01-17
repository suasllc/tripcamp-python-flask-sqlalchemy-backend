from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
# from flask_wtf.csrf import CSRFProtect


from .routes.api.spot import bp as spotbp
from .routes.api.booking import bp as bookingbp
from .routes.api import session
from .db.models import db
from .db.models.user import User
from .config import Configuration

app = Flask(__name__, static_url_path='/public')
# csrf = CSRFProtect(app)
app.register_blueprint(spotbp)
app.register_blueprint(bookingbp)
app.register_blueprint(session.bp)
app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = "session.login"

@app.route('/')
def index():
  return app.send_static_file('index.html')

@login.user_loader
def load_user(id):
    return User.query.get(int(id))  

