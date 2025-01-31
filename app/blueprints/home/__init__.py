from flask import Blueprint
from flask import render_template

home_bp = Blueprint('home', __name__, template_folder='templates', static_folder='static')

@home_bp.route('/', methods=['GET'])
@home_bp.route('/home', methods=['GET'])
def home():
    content = {
        "page_name": "Home",
        "page_subtitle": "Wall of Glizzy's"
    }
    return render_template('home.html', title='Home', content=content)


