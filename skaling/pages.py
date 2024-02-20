from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    make_response,
    #redirect,
    #url_for,
)

from skaling.database import get_db

bp = Blueprint("pages", __name__)


@bp.route("/", methods=("GET", "POST"))
def home():
    db = get_db()

    ## Old way, non responsive
    # if request.method == "POST":
    #    name = request.form["name"]
    #    ex_type = request.form["type"]
    #    speed = int(request.form["speed"])
    #    direction = request.form["dir"]
    #    if direction == "inc":
    #        speed += 5
    #    elif direction == "dec":
    #        speed -= 5

    #    db.execute("UPDATE scales SET speed = (?) WHERE name = (?) AND type = (?)",
    #            (speed, name, ex_type))
    #    db.commit()

    exercises = db.execute("SELECT name, type, speed FROM scales")
    return render_template("pages/home.html", exercises=exercises)


@bp.route("/change-speed", methods=["POST"])
def change_speed():
    db = get_db()
    req = request.get_json()
    # print(req, type(req))
    # print(f"{req['name']} ||| {req['type']} ||| {req['new_speed']} ")
    db.execute(
        "UPDATE scales SET speed = (?) WHERE name = (?) AND type = (?)",
        (req["new_speed"], req["name"], req["type"]),
    )
    db.commit()

    res = make_response(jsonify({"message": "JSON received"}), 200)
    return res
