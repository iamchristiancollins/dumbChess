from flask import Blueprint

game_bp = Blueprint('game', __name__)

@game_bp.route('/')
def index():
    return "Dumb Chess is up and running!"
