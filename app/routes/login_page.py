from flask import Blueprint, request, session, Response, render_template, make_response, current_app, redirect, url_for, jsonify
login_blueprint = Blueprint('login', __name__)

# landing page for api
@login_blueprint.route('/', methods=['GET',])
def login_landing_page():
    pass