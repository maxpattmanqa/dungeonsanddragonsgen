from flask import Flask, request, jsonify, Response
import random
app = Flask(__name__)
# ratings generator needs to when received needs to take information form other 3 
@app.route('/get/text', methods=['GET'])
def get_text():
    
    value = 1
    return Response(str(value), mimetype='text/plain')

@app.route('/post/text', methods=['POST'])
def post_text():
    return Response("Data you sent: " + request.data.decode("utf-8"), mimetype='text/plain')

@app.route('/get/json', methods=['GET'])
def get_json():
    return jsonify({"data": "Hello from ratings_generator"})

@app.route('/post/rating_num', methods=['POST'])
def generate_rating_num():
    app.logger.info("/post/rating_num HIT!")
    data = request.json
    race_num = data["race_num"]
    role_num = data["role_num"]
    weapon_num=data["weapon_num"]
    value = int(race_num) + int(role_num) + int(weapon_num)
    
    return Response(str(value),mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5005)