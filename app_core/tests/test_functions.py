import pytest
from flask_testing import TestCase
from application.routes import view_homepage, insert_charachter_entry, get_charachter_entry , get_race_entry_by_id , get_role_entry_by_id, get_weapon_entry_by_id
from application import app,db
from application.models import Charachter , Race , Role , Weapon
#from create import provision_db
from unittest.mock import patch
from flask import url_for
import requests_mock
class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///site.db"
           # SECRET_KEY="TEST_SECRET_KEY"
          #  DEBUG=True
        )
        return app
    
    def setUp(self):
        db.drop_all()
        db.create_all()
        provision_db()


class TestRoutes(TestBase):

    def test_generate_weapon(self):
        with requests_mock.mock() as m:
            m.get("http://stack-project_weapons_generator:5002/get/weapon_id", text = '1')
            response = self.client.get(url_for('generate_weapon'))
            self.assertIn(b'1', response.data)


    def test_generate_role(self):
        with requests_mock.mock() as m:
            m.get("http://stack-project_role_generator:5001/get/role_id", text = '1')
            response = self.client.get(url_for('generate_role'))
            self.assertIn(b'1', response.data)
    
    def test_generate_race(self):
        with requests_mock.mock() as m:
            m.get('http://stack-project_race_generator:5003/get/race_id', text = '1')
            response = self.client.get(url_for('generate_race'))
            self.assertIn(b'1', response.data)

    # def test_generate_rating(self):
    #     with requests_mock.mock as m:
    #         m.post('http://stack-project_rating_generator:5005/post/rating_num', json={"race_num":1,"role_num":2,"weapon_num":3})
    #         response = self.client.get(url_for('generate_rating'))
    #         self.assertIn(b'6',response.data)













class TestDBFunctionality(TestBase):

    def test_insert_charachter_entry(self):
        insert_charachter_entry(first_name="test_name",second_name="test_second_name", rating=1,race_id=1,weapon_id=1 ,role_id=1)
        #query the database and assert it exists 
        db_ret_val = get_charachter_entry("test_name","test_second_name")
        assert(db_ret_val.first_name == "test_name")
        assert (db_ret_val.second_name == "test_second_name")
        assert (db_ret_val.rating == 1)
        assert (db_ret_val.race_id == 1)
        assert (db_ret_val.weapon_id == 1)
        assert (db_ret_val.role_id == 1)

    
    def test_get_race_entry_by_id(self):
        elf = get_race_entry_by_id(1)
        man = get_race_entry_by_id(2)
        dwarf =get_race_entry_by_id(3)
        goblin = get_race_entry_by_id(4)
        troll = get_race_entry_by_id(5)
        orc = get_race_entry_by_id(6)
        assert (elf.race == "Elf")
        assert (man.race == "Man")
        assert (dwarf.race == "Dwarf")
        assert (goblin.race == "Goblin")
        assert (troll.race == "Troll")
        assert (orc.race == "Orc")
       
        
    def test_get_role_entry_by_id(self):
        warrior = get_role_entry_by_id(1)
        paladin = get_role_entry_by_id(2)
        hunter = get_role_entry_by_id(3)
        mage = get_role_entry_by_id(4)
        warlock = get_role_entry_by_id(5)
        healer = get_role_entry_by_id(6)
        assert(warrior.role =="Warrior")
        assert(paladin.role == "Paladin")
        assert(hunter.role == "Hunter")
        assert(mage.role == "Mage")
        assert(warlock.role == "Warlock")
        assert(healer.role == "Healer")


    def test_get_weapon_entry_by_id(self):
        sword = get_weapon_entry_by_id(1)
        axe = get_weapon_entry_by_id(2)
        staff = get_weapon_entry_by_id(3)
        wand = get_weapon_entry_by_id(4)
        mace = get_weapon_entry_by_id(5)
        bow = get_weapon_entry_by_id(6)
        assert(sword.weapon =="Sword")
        assert(axe.weapon == "Axe")
        assert(staff.weapon == "Staff")
        assert(wand.weapon == "Wand")
        assert(mace.weapon == "Mace")
        assert(bow.weapon == "Bow")



    



#Provision db function for testing 
def provision_db():
    race_elf= Race(race='Elf')
    race_man =Race(race='Man')
    race_dwarf = Race(race='Dwarf')
    race_goblin = Race(race='Goblin')
    race_troll = Race(race='Troll')
    race_orc = Race(race='Orc')
    races = [race_elf,race_man,race_dwarf,race_goblin,race_troll,race_orc]
    for race in races:
        db.session.add(race)
        db.session.commit()
    #adding roles
    role_warrior = Role(role='Warrior')
    role_paladin = Role(role='Paladin')
    role_hunter = Role(role='Hunter')
    role_mage= Role(role='Mage')
    role_warlock=Role(role='Warlock')
    role_healer=Role(role='Healer')
    roles = [role_warrior,role_paladin,role_hunter,role_mage,role_warlock,role_healer]
    for role in roles:
        db.session.add(role)
        db.session.commit()

    #adding weapons 
    weapon_sword = Weapon(weapon='Sword')
    weapon_axe = Weapon(weapon='Axe')
    weapon_staff = Weapon(weapon='Staff')
    weapon_wand = Weapon(weapon='Wand')
    weapon_mace = Weapon(weapon='Mace')
    weapon_bow = Weapon(weapon='Bow')
    weapons =[weapon_sword,weapon_axe,weapon_staff,weapon_wand,weapon_mace,weapon_bow]
    for weapon in weapons:
        db.session.add(weapon)
        db.session.commit()

    dummy_charachter = Charachter(first_name='dummy',second_name='charachter',rating=1,race_id=1,weapon_id=2,role_id=1)
    db.session.add(dummy_charachter)
    db.session.commit() 
    # print(Race.query.all())
    # print(Weapon.query.all())
    # print(Role.query.all())
    # print(Charachter.query.all())

