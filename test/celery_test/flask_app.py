from flask import Flask
from celery_app import async_add

flask_app = Flask(__name__)
@flask_app.route('/test', methods=["GET"])
def test_add():
    """
    测试相加
    :return:
    """
    result = async_add.delay(1, 2)
    return str(result.get(timeout=1))

if __name__ == '__main__':
    flask_app.run()

