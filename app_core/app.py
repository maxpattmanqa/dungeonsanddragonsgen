from flask import Flask
import requests
from requests import get
app = Flask(__name__)
ip = get('https://api.ipify.org').text
server_url = 'http://'+ip

@app.route('/')
def helloworld():
    return "HELLO WORLD !"

#Api resonse test for generate weapon 
@app.route('/generate_weapon')
def generate_weapon():
    response = requests.get(server_url+'')
    return 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5100)