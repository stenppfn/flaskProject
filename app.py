from datetime import datetime
from decimal import Decimal
from flask import Flask,jsonify,Blueprint

from application.utils.code import ResponseCode,ResponseMessage
from application.utils.response import ResMsg
from application.utils.util import route
from application.api.services import ArticleAPI
from application.utils.core import db
from application.factory import create_app

app = create_app(config_name="DEVELOPMENT")
app.app_context().push()


if __name__ == "__main__":
    app.run()
