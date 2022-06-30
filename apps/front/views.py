from flask import Blueprint

bp = Blueprint('front', __name__)  # 因为前台是直接访问就不用加url_prefix


@bp.route('/')
def index():
    return 'front index'
