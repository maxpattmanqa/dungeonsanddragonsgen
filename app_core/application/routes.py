
from application import app, db
from flask import render_template, request, redirect,url_for
from application.models import Charachter , Race , Role , Weapon
from flask import Flask
import requests
from requests import get
from application.forms import GenerateCharachterForm
from flask.json import jsonify

#route to homepage
@app.route('/')
def view_homepage():
    return render_template('home.html')

#route to the character creator screem
@app.route('/charachtercreator',methods=['GET','POST'])
def view_charachter_creator():
    form = GenerateCharachterForm()
    if(request.method == 'POST') and (form.validate_on_submit()):
        first_name= form.first_name.data
        second_name=form.second_name.data
        race_num = generate_race()
        int(race_num)
        weapon_num = generate_weapon()
        int(weapon_num)
        role_num = generate_role()
        int(role_num)
        rating= generate_rating(race_num=race_num,role_num=role_num,weapon_num=weapon_num)
        int(rating)
        charachter = Charachter(first_name=first_name,second_name=second_name,rating=int(rating),race_id=int(race_num),weapon_id=int(weapon_num),role_id=int(role_num))
        db.session.add(charachter)
        db.session.commit()

    return render_template('character_creator.html',form=form)

#route to the tournament page 
@app.route('/tournament')
def view_tournament():
    return render_template('tournament.html')

#route to the charachterprofiles page
@app.route('/characterprofiles',methods=['GET','POST'])
def view_charachter_profiles():
    charachters = Charachter.query.all()
    return render_template('character_profiles.html',charachters=charachters)

# this calls 
@app.route('/get/generate_weapon', methods=['GET','POST'])
def generate_weapon():
    response = requests.get('http://stack-project_weapons_generator:5002/get/weapon_id')
    return str(response.text)

@app.route('/get/generate_race',methods=['GET'])
def generate_race():
    #response = requests.get(server_url+':5003/get/race_id')
    response = requests.get('http://stack-project_race_generator:5003/get/race_id')

    return str(response.text) 

@app.route('/get/generate_role',methods=['GET','POST'])
def generate_role():
    response = requests.get('http://stack-project_role_generator:5001/get/role_id')
    return str(response.text) 

@app.route('/get/generate_rating', methods=['GET','POST'])
def generate_rating(race_num,role_num,weapon_num):
    data = {
        "race_num":race_num,
        "role_num":role_num,
        "weapon_num":weapon_num
    }
    
   
    response = requests.post('http://stack-project_rating_generator:5005/post/rating_num',json=data)
    return str(response.text)
#db helper functionss  

def get_race_entry_by_id(race_id):
    return Race.query.filter_by(id=race_id).first()

def get_role_entry_by_id(role_id):
    return Role.query.filter_by(id=role_id).first()

def get_weapon_entry_by_id(weapon_id):
    return Weapon.query.filter_by(id=weapon_id).first()


def insert_charachter_entry(first_name, second_name,rating,race_id,weapon_id,role_id):
    db_insert_entry = Charachter(first_name=first_name,second_name=second_name,rating=int(rating),race_id=int(race_id),weapon_id=int(weapon_id),role_id=int(role_id))
    db.session.add(db_insert_entry)
    db.session.commit()

def get_charachter_entry(first_name,second_name):
    return Charachter.query.filter_by(first_name=first_name , second_name=second_name).first()









