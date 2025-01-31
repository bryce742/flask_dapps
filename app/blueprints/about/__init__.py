from flask import Blueprint 
from flask import render_template

about_bp = Blueprint('about', __name__, template_folder='templates', static_folder='static')


@about_bp.route('/about', methods=['GET'])
def about():
    content = {
        "page_name": "Community!",
        "page_subtitle": "Come on, don't be shy, have a $GLIZZ!",
        "socials": [
            {
                "platform": "X",
                "platform_logo": "Twitter-X-Logo.png",
                "platform_username": "@getelonsglizzy",
                "platform_link": "https://x.com/getelonsglizzy"
            },
            {
                "platform": "Telegram",
                "platform_logo": "tg_logo.png",
                "platform_username": "@elonsglizzy",
                "platform_link": "https://t.me/elonsglizzy"
            }
        ]
    }
    return render_template('about.html', title='About', content=content)