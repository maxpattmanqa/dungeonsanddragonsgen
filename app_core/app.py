from flask import flask

app = Flask(__name__)
@app.route('/number', methods=['GET'])
def number():
    return 3

if __name__ == '__main__':
    app.run( host='0.0.0.0',port=5000, debug=True)