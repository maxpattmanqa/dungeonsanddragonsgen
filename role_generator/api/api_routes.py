from flask import Flask, request, jsonify, Response
from api import app
import random

@app.route('/get/role_id', methods=['GET'])
def get_text():
    value = random.randint(1,6)
    return Response(str(value), mimetype='text/plain')
