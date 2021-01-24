from flask import Flask,request,jsonify, Response
from api import app
import random

@app.route('/get/weapon_id', methods=['GET'])
def get_text():
    #value = random.randint(0,5)
    value = 0
    return Response(str(value), mimetype='text/plain')
