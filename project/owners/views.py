## we need to create the blueprint for our owners resource in this file

from flask import Blueprint 
#importing the Blueprint module that all our blueprints will inherit from

from project.owners.models import Owner
# importing the Owner class that represents our owners table

from flask import request, redirect, render_template, url_for
# we need these to handle our routing

from project.owners.forms import NewOwnerForm
## we need to get the Class that creates forms from forms.py

from project import db
## we need the db alias to find data from our database

owners_blueprint = Blueprint(
	'owners',
	__name__,
	template_folder = 'templates'
)

@owners_blueprint.route('/',methods =["GET", "POST"])
def index():
	owners = Owner.query.all()
	if request.method =="POST":
		form = NewOwnerForm()
		if form.validate():
			new_owner = Owner(request.form['first_name'], request.form['last_name'])
			db.session.add(new_owner)
			db.session.commit()
			return redirect(url_for('owners.index'))
	return render_template("owners/index.html", owners = owners)


@owners_blueprint.route('/new')
def new():
	return render_template('owners/new.html', form = NewOwnerForm())

@owners_blueprint.route('/<int:id>/edit')
def edit(id):
	found_owner = Owner.query.get(id)
	form = NewOwnerForm(obj =found_owner)
	return render_template('owners/edit.html',form=form, owner = found_owner)


@owners_blueprint.route('/<int:id>', methods =['GET', 'PATCH','DELETE'])
def show(id):
	found_owner = Owner.query.get(id)
	if request.method ==b'PATCH':
		found_owner.first_name = request.form['first_name']
		found_owner.last_name = request.form['last_name']
		db.session.add(found_owner)
		db.session.commit()
		return redirect(url_for('owners.index'))
	if request.method  ==b'DELETE':
		db.session.delete(found_owner)
		db.session.commit()
		return redirect(url_for('owners.index'))

	return render_template('owners/show.html',owner = found_owner)





