from flask import Flask, request, jsonify, Response
from api import app
@app.route('/post/rating_num', methods=['POST'])
def generate_rating_num():
    data = request.json
    race_num = data["race_num"]
    role_num = data["role_num"]
    weapon_num=data["weapon_num"]
    #value = int(race_num) + int(role_num) + int(weapon_num)
    value = 1
    return Response(str(value),mimetype='text/plain')