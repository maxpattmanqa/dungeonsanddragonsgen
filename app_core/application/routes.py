

from application import app,db
from flask import render_template, request, redirect,url_for
#from application.forms
from application.models import Charachter , Race , Role , Weapon
from flask import Flask
import requests
from requests import get
from sqlalchemy.orm import sessionmaker




ip = get('https://api.ipify.org').text
server_url = 'http://'+ip

@app.route('/')
def view_homepage():
    return render_template('home.html')

@app.route('/charachtercreator')
def view_charachter_creator():
    return render_template('character_creator.html')

@app.route('/tournament')
def view_tournament():
    return render_template('tournament.html')

@app.route('/characterprofiles',methods=['GET','POST'])
def view_charachter_profiles():
 
    #charachters = db.session.query(Charachter).all()
    #print('We tried to get charachter profiles here '+str(charachters))
    return render_template('character_profiles.html')


#database query functions 

def get_charachters_list():
    print (Charachter.query.all())
    print('get charachters function was executec')
    query =  Charachter.query.all()
    return query












#Api resonse test for generate weapon 

@app.route('/get/generate_weapon')
def generate_weapon():
    response = requests.get(server_url+':5002/get/text')
    return str(response.text) + "Successful Ping "

@app.route('/get/generate_race')
def generate_race():
    response = requests.get(server_url+':5003/get/text')
    return str(response.text) + "Successful Ping "

@app.route('/get/generate_role')
def generate_role():
    response = requests.get(server_url+':5001/get/text')
    return str(response.text) + "Successful Ping "


@app.route('/get/sport', methods=['GET'])
def sport():
    response = requests.get('http://api:5000/get/number')
    if response.text == "1":
        return "Football"
    elif response.text == "2":
        return "Badminton"
    elif response.text == "3":
        return "Hockey"
    else:
        return "Boxing"