from project import db


class Startup(db.Model):
	__tablename__ = 'startups'

	 ## Defining the columns for our table
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.Text, nullable = False)
	industry =db.Column(db.Text, nullable =False)
	owner_id =db.Column(db.Integer, db.ForeignKey('owners.id'))


	## Defining each instance i.e. each row in our table

	def __init__(self, name, industry, owner_id):
		self.name = name
		self.industry = industry
		self.owner_id = owner_id


