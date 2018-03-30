from flask import Blueprint, render_template, request
from app.models import Engine
from app import db

home = Blueprint('home', __name__)


@home.route('/',methods=['GET', 'POST'])
def index():
    engines = []
    if request.method == "POST":
        engineId = request.form.get('engineId', None)
        description = request.form.get('engineTitle', None)
        thrust = request.form.get('engineThrust', None)
        try:
            engine = Engine.query.get(engineId)
            engine.title = description
            engine.thrust = thrust
        except TypeError:
            engine = Engine(id=engineId, title=description, thrust=thrust)
            db.session.add(engine)

        db.session.commit()

    for engine in Engine.query.all():
        engines.append((engine.id, engine.title, engine.thrust))
    return render_template("home/index.html", engines=engines)
