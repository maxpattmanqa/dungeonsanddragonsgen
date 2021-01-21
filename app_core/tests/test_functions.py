import pytest
from flask_testing import TestCase
from application.routes import view_homepage, insert_charachter_entry, get_charachter_entry , get_race_entry_by_id , get_role_entry_by_id, get_weapon_entry_by_id
from application import app,db
from create import provision_db
from unittest.mock import patch

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

class TestDBFunctionality(TestBase):

    def test_insert_charachter_entry(self):
        insert_charachter_entry(first_name="test_name",second_name="test_second_name" ,race_id=1,weapon_id=1 ,role_id=1)
        #query the database and assert it exists 
        db_ret_val = get_charachter_entry("test_name","test_second_name")
        assert(db_ret_val.first_name == "test_name")
        assert (db_ret_val.second_name == "test_second_name")
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



    





