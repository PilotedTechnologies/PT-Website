from flask import Blueprint, request, session, Response, render_template, make_response, current_app, redirect, url_for, jsonify

about_us_blueprint = Blueprint('about_us', __name__)

# landing page for about us
@about_us_blueprint.route('/', methods=['GET',])
def about_us_landing_page():
    pass

# Recive form input. Process it(into somekind of DB). Give Success/Failure outcome
@about_us_blueprint.route('/contact-form', methods=['POST',])
def contact_form():
    pass