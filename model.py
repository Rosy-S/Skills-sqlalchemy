"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):

    __tablename__ = "models"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    brand_name = db.Column(db.String(50), db.ForeignKey('brands.name'))
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self): 
        return "<Model id=%s>" % (self.id)
    #     return "<Model id=%s year=%s brand_name=%s name=%s>" % (self.id, self.year, self.brand_name, self.name)
    
    #Defining relationship with Brand
    brand = db.relationship("Brand", 
                            backref=db.backref("models"))

class Brand(db.Model):

    __tablename__ = "brands"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    founded = db.Column(db.Integer)
    headquarters = db.Column(db.String(50))
    discontinued = db.Column(db.Integer)

    def __repr__(self):
        return "<brand id=%s>" % (self.id) 
    #     return "<Brand id=%s name=%s founded=%s headquarters=%s>" % (self.id, self.name, self.founded, self.headquarters)

# End Part 1
##############################################################################
# Helper functions


#Query functions 
def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_list = Model.query.filter(Model.year == year).all()
    for model in model_list: 
        print model.id, model.name, model.brand.headquarters
    pass

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''
    brand_list = Brand.query.all()
    for brand in brand_list: 
        print brand.name, brand.models.name 


    pass


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auto.db'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
