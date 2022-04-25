from flask import Blueprint
from .celery import add, flask_app_context

bp = Blueprint("test", __name__, url_prefix='/')


@bp.route('/testAdd', methods=["GET"])
def test_add():
    """
    测试相加
    :return:
    """
    result = add.delay(1, 2)
    return result.get(timeout=1)


@bp.route('/testFlaskAppContext', methods=["GET"])
def test_flask_app_context():
    """
    测试相加
    :return:
    """
    result = flask_app_context.delay()
    return result.get(timeout=1).replace('<Config', '')
