"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
models = Model.query.filter(Model.name == 'Corvette', Brand.name == 'Chevrolet').all()

# Get all models that are older than 1960.
old_models = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
brands_after = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
cor_models = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
brands_1903 = Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.
brands_discontinued = Brand.query.filter(db.or_(Brand.discontinued.isnot(None), 
												Brand.founded <1950)).all()

# Get any model whose brand_name is not Chevrolet.
anti_chevrolet = Model.query.filter(Model.name != 'Chevrolet').all()


# Fill in the following functions. (See directions for more info.)

# Function with a lot of queries:
def get_model_info_inefficient(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_list = Model.query.filter(Model.year == year).all()
    for model in model_list: 
    	print model.id, model.name, model.brand.headquarters
    pass

def get_model_info(year): 
	model_list = db.session.query(Model.id, Model.name, Brand.headquarters).filter(Model.year == year).join(Brand)
	for id, name, headquarters in model_list: 
		print id, name headquarters

	pass 
def get_brands_summary_inefficient():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''
    brand_list = Brand.query.all()
    for brand in brand_list: 
    	print brand.name, brand.model.name 
    pass

def get_brands_summary(): 
	brand_list = db.session.query(Model, Brand).join(Brand).all()
	for model,brand in brand_list: 
		print brand.name, model.name 

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    return Brand.query.filter(Brand.name.like("%" + mystr + "%")).all()


def get_models_between(start_year, end_year):
	return Model.query.filter(Model.year >= start_year, Model.year <= end_year).all()
    

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
		# The returned value is a query object that checks on the Brand class for all brand objects
		# that have a brand name of 'Ford'. This will not return any results until you invoke it 
		# with an ending that actually calls the query of either all, one, or first.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
		# An association table is a database table that holds common fields among other tables.
		# Using these common fields, association tables maps relationships among tables that would
		# otherwise have no common fields between these said tables. Unique tables can thus use
 	# 	association tables to get from one unique table to another. 

 	# 	Association tables manage either one to many relationship tables, or many to many relationship
 	# 	tables.
