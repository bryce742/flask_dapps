from flask import Blueprint
from flask import render_template


buy_bp = Blueprint('buy', __name__, template_folder='templates', static_folder='static')



@buy_bp.route('/buy', methods=['GET'])
def buy():
    content = {
        "page_name": "Ape Elon's Glizzy!",
        "page_subtitle": "Think with your $GLIZZ before you ape!"
    }
    meme_ca = 'MSGYLRarqfxgoigPTE8qSDrLzu4hXsHhLzYjeX2pump'
    return render_template('buy.html', title='Buy', content=content, meme_ca=meme_ca)