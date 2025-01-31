from flask import Flask


# app instanitation and setting blueprints
app = Flask(__name__, template_folder='base_templates', static_folder='static')

from app.blueprints.home import home_bp
app.register_blueprint(home_bp)

from app.blueprints.about import about_bp
app.register_blueprint(about_bp)

from app.blueprints.buy import buy_bp
app.register_blueprint(buy_bp)

