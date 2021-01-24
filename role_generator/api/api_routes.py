from flask import Flask, request, jsonify, Response
from api import app
import random
#demobranch
@app.route('/get/role_id', methods=['GET'])
def get_text():
    value = random.randint(0,5)
    value = 0
    return Response(str(value), mimetype='text/plain')
