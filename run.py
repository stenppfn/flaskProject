from datetime import datetime
from decimal import Decimal
from app.factory import create_app
from flask import Flask,jsonify,Blueprint
from app.utils.code import ResponseCode,ResponseMessage
from app.utils.response import ResMsg
from app.utils.util import route

app = create_app(config_name="DEVELOPMENT")





if __name__ == "__main__":
    app.run()
