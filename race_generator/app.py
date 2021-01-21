from flask import Flask, request, jsonify, Response
import random
app = Flask(__name__)
# ratings generator needs to when received needs to take information form other 3 
# app.logger().info("/get/race_id HIT!")
@app.route('/get/race_id', methods=['GET'])
def get_race_id():

    rand_value = random.randint(0,5)
    return Response(str(rand_value), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5003)