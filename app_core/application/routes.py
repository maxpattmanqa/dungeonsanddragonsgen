

from application import app, db
from flask import render_template, request, redirect,url_for
#from application.forms
from application.models import Charachter , Race , Role , Weapon
from flask import Flask
import requests
from requests import get

from application.forms import GenerateCharachterForm

#print(Charachter.query.all())
ip = get('https://api.ipify.org').text
server_url = 'http://'+ip

@app.route('/')
def view_homepage():
    return render_template('home.html')

@app.route('/charachtercreator',methods=['GET','POST'])
def view_charachter_creator():
    form = GenerateCharachterForm()
    if(request.method == 'POST') and (form.validate_on_submit()):
        first_name= form.first_name.data
        second_name=form.second_name.data
        race = generate_race()
        weapon = generate_weapon()
        role = generate_role()
        charachter = Charachter(first_name=first_name,second_name=second_name,race_id=int(race),weapon_id=int(weapon),role_id=int(role))
        db.session.add(charachter)
        db.session.commit()

    return render_template('character_creator.html',form=form)

@app.route('/tournament')
def view_tournament():
    return render_template('tournament.html')

@app.route('/characterprofiles',methods=['GET','POST'])
def view_charachter_profiles():
    charachters = Charachter.query.all()
    return render_template('character_profiles.html',charachters=charachters)


#database query functions 
#Api resonse test for generate weapon 

@app.route('/get/generate_weapon')
def generate_weapon():
    response = requests.get(server_url+':5002/get/text')
    return str(response.text)

@app.route('/get/generate_race')
def generate_race():
    response = requests.get(server_url+':5003/get/text')
    return str(response.text) 

@app.route('/get/generate_role')
def generate_role():
    response = requests.get(server_url+':5001/get/text')
    return str(response.text) 





















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