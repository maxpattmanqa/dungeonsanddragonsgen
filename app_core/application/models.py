from application import db

class Race(db.Model):
    __tablename__  = 'race'
    id = db.Column(db.Integer,primary_key=True)
    race = db.Column(db.String(30),nullable=False)
    race_relationship = db.relationship('Charachter', backref='race')
    def __repr__(self):
        return f"<'{self.id}','{self.race}>"

class Weapon(db.Model):
    __tablename__  = 'weapon'
    id = db.Column(db.Integer,primary_key=True)
    weapon= db.Column(db.String(30),nullable=False)
    weapon_relationship = db.relationship('Charachter', backref='weapon')
    def __repr__(self):
        return f"<'{self.id}','{self.weapon}'>"


class Role(db.Model):
    __tablename__  = 'role'
    id = db.Column(db.Integer,primary_key=True)
    role = db.Column(db.String(30),nullable=False)
    role_relationship = db.relationship('Charachter', backref='role')
    def __repr__(self):
        return f"<'{self.id}','{self.role}'>"

class Charachter(db.Model):
    __tablename__ = 'charachter'
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(30),nullable=False)
    second_name = db.Column(db.String(30),nullable=False)
    rating = db.Column(db.Integer,nullable=False)
    race_id =db.Column(db.Integer,db.ForeignKey('race.id'))
    weapon_id=db.Column(db.Integer,db.ForeignKey('weapon.id'))
    role_id=db.Column(db.Integer,db.ForeignKey('role.id'))
    def __repr__(self):
        return f"<'{self.id}','{self.first_name}','{self.second_name}','{self.race_id}','{self.weapon_id}','{self.role_id}','{self.rating}'>"

