from application import  app,db 
from application.models import Charachter , Race , Role , Weapon

db.drop_all()
db.create_all()

#adding races
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
    db.session.add(race)
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

dummy_charachter = Charachter(first_name='dummy',second_name='charachter',race_id=1,weapon_id=2,role_id=1)
db.session.add(dummy_charachter)
db.session.commit()
print(Race.query.all())
print(Weapon.query.all())
print(Role.query.all())
print(Charachter.query.all())
