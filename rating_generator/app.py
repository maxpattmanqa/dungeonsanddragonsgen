from flask import Flask, request, jsonify, Response
import random
app = Flask(__name__)
# ratings generator needs to when received needs to take information form other 3 
@app.route('/get/text', methods=['GET'])
def get_text():
    
    value = random.randint(0,5)
    return Response(str(value), mimetype='text/plain')

@app.route('/post/text', methods=['POST'])
def post_text():
    return Response("Data you sent: " + request.data.decode("utf-8"), mimetype='text/plain')

@app.route('/get/json', methods=['GET'])
def get_json():
    return jsonify({"data": "Hello from ratings_generator"})

@app.route('/post/json', methods=['POST'])
def post_json():
    jsondata = request.get_json()
    print(jsondata)
    return jsonify({"data": request.get_json()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5005)