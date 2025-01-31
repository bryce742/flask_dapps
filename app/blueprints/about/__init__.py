from flask import Blueprint 
from flask import render_template

about_bp = Blueprint('about', __name__, template_folder='templates', static_folder='static')


@about_bp.route('/about', methods=['GET'])
def about():
    content = {
        "page_name": "About",
        "page_subtitle": "Come bug the mods on our socials!"
    }
    return render_template('about.html', title='About', content=content)