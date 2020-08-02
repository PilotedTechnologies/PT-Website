from flask import Blueprint, request, session, Response, render_template, make_response, current_app, redirect, url_for, jsonify
landing_blueprint = Blueprint('landing', __name__)

# landing page for api
@landing_blueprint.route('/', methods=['GET',])
def landing_page():
    return render_template('landing.j2')