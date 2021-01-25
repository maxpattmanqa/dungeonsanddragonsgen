from flask import Flask, request, jsonify, Response
from api import app
#import random

@app.route('/get/race_id', methods=['GET'])
def get_race_id():
#    rand_value = random.randint(1,6)
    rand_value =1
    return Response(str(rand_value), mimetype='text/plain')