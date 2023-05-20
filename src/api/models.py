from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    birth_year= db.Column(db.String(15), nullable=False)
    eye_color= db.Column(db.String(10), nullable=False)
    gender=db.Column(db.String(10), nullable=False)
    hair_color=db.Column(db.String(10), nullable=False)
    height=db.Column(db.Float, nullable=False)
    homeworld_id= db.Column(db.Integer, db.ForeignKey("planets.id"))
    homeworld=db.relationship("Planets")

    def __repr__(self):
        return '<People %r>' % self.name
    
class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    climate= db.Column(db.String(15), nullable=False)
    gravity= db.Column(db.String(10), nullable=False)
    terrain=db.Column(db.String(10), nullable=False)
    population=db.Column(db.Float, nullable=False)
    orbital_period=db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name
   
class Favorites(db.Model):
    __tablename__='favorites'
    id=db.Column(db.Integer, primary_key=True)
    type=db.Column(db.String(20), nullable=False)
    element_id=db.Column(db.Integer, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey("users.id"))
    user=db.relationship(User)

    def __repr__(self):
        return '<Favorite %r/%r>' % self.type % self.element_id