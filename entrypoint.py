from flask_sqlalchemy import SQLAlchemy

from .app import create_app
from .app.auth.models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:testing@localhost:5432/miniblog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
login_manager = LoginManager(app)
login_manager.login_view = "login"
db = SQLAlchemy(app)

app = create_app()

@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(int(user_id))