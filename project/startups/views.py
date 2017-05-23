from flask import Blueprint, redirect, request, url_for, render_template
from project import db
from project.startups.models import Startup 
from project.startups.forms import NewStartupForm
from project.owners.models import Owner 

startups_blueprint = Blueprint(
	'startups',
	__name__,
	template_folder = 'templates'
)

@startups_blueprint.route("/", methods=['GET', 'POST'])
def index(id):
	all_startups = Startup.query.all()
	owner = Owner.query.get(id)
	form = NewStartupForm()
	if request.form =="POST":
		if form.validate():
			new_startup = Startup(request.form['name'], request.form['industry'])
			db.session.add(new_startup)
			db.session.commit()
			return redirect(url_for("startups.index"))

			# , all_startups=all_startups

	return render_template('startups/index.html', all_startups=all_startups, owner=owner)

@startups_blueprint.route("/new")
def new(id):
	return render_template("startups/new.html", form=NewStartupForm(), id=id)


@startups_blueprint.route("/<int:startup_id>/edit")
def edit(id, startup_id):
	found_startup = Startup.query.get(startup_id)
	form = NewStartupForm(obj=found_startup)
	
	return render_template("startups/edit.html", id=id, startup_id=startup_id, form=form, startup=found_startup)



@startups_blueprint.route("/<int:startup_id>/show", methods=['GET', 'PATCH', 'DELETE'])
def show(id, startup_id):
	found_startup = Startup.query.get(startup_id)
	if request.method ==b'PATCH':
		found_startup.name = request.form['name']
		found_startup.industry =request.form['industry']
		db.session.add(found_startup)
		db.session.commit()
		return redirect(url_for("startups.show",id=id, startup_id=startup_id))
	if request.method == b'DELETE':
		db.session.delete(found_startup)
		db.session.commit()
		return redirect(url_for("startups.show",id=id, startup_id=startup_id))

	return render_template("startups/show.html", startup=found_startup, id=id, startup_id=startup_id)

