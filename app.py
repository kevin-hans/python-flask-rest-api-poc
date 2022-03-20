import imp
from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
import logging
from model.user import User
from model.photo import Photo
from globalapp import app
from flask import Response
import json
from utils.AlchemyEncoder import AlchemyEncoder

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.getLogger('flask_cors').level = logging.DEBUG


@app.route("/")
@cross_origin()
def hello_world():
    return "<p>Hello, world!</p>"
    
@app.route("/json")
@cross_origin()
def hello_json():
    return jsonify({ "message": "日本語" })

@app.route("/user/list")
@cross_origin()
def getUserList1():
  return Response(json.dumps(User.query.all(), cls=AlchemyEncoder))

@app.route("/photo/list")
@cross_origin()
def getPhotoList():
  return Response(json.dumps(Photo.query.all(), cls=AlchemyEncoder))
   