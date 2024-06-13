from flask import Blueprint, render_template, request, jsonify

views = Blueprint(__name__,"views")

templates  = "index.html"

@views.route("/")
def home():
    return render_template(templates, name='Baatile')

#This is for dynamic routing
@views.route("/profile/<username>")
def profile(username):
    return render_template(templates, name=username)

#query parameters for this users
@views.route("/user")
def user():
    args = request.args
    name = args.get("name")
    return render_template(templates, name=name)

@views.route("/json")
def get_json():
    return jsonify({'name':'Baatile', 'description':'I love my awesome'})

@views.route("/api")
def get_api():
    data = request.json()
    return get_json(data)

