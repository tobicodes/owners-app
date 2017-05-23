from project import db
## import Startup here?

class Owner(db.Model):
    __tablename__ = 'owners'

    ## Defining the columns for our table

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    startups = db.relationship('Startup', backref='owner', lazy ='dynamic')

    ## defining the rows i.e. what each instance will have as data

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name