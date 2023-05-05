import logging
import logging.config
import yaml
import os
from flask import Flask
from app.api.services import ArticleAPI
from app.utils.core import JSONEncoder
from app.utils.core import JSONEncoder,db

def create_app(config_name=None, config_path=None):
    app = Flask(__name__)

    # 读取配置文件
    if not config_path:
        pwd = os.getcwd()
        config_path = os.path.join(pwd, 'config/config.yaml')
    if not config_name:
        config_name = 'PRODUCTION'

    # 读取配置文件
    conf = read_yaml(config_name, config_path)
    app.config.update(conf)

    # 返回json格式转换
    app.json_encoder = JSONEncoder

    # 注册数据库连接
    db.app = app
    db.init_app(app)
    # db.create_all()

    article_view = ArticleAPI.as_view('article_api')
    app.add_url_rule('/article/', defaults={'key': None},view_func=article_view, methods=['GET', ])
    app.add_url_rule('/article/', view_func=article_view, methods=['POST', ])
    app.add_url_rule('/article/<string:key>', view_func=article_view,methods=['GET', 'PUT', 'DELETE'])

    # 读取msg配置
    with open(app.config['RESPONSE_MESSAGE'], 'r', encoding='utf-8') as f:
        msg = yaml.safe_load(f.read())
        app.config.update(msg)

    return app


def read_yaml(config_name, config_path):
    """
    config_name:需要读取的配置内容
    config_path:配置文件路径
    """
    if config_name and config_path:
        with open(config_path, 'r', encoding='utf-8') as f:
            conf = yaml.safe_load(f.read())
        if config_name in conf.keys():
            return conf[config_name]
            # return conf[config_name.upper()]
        else:
            raise KeyError('未找到对应的配置信息')
    else:
        raise ValueError('请输入正确的配置名称或配置文件路径')
