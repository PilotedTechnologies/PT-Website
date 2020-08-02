from flask import Blueprint, request, session, Response, render_template, make_response, current_app, redirect, url_for, jsonify

services_blueprint = Blueprint('services', __name__)

# landing page for about us
@services_blueprint.route('/', methods=['GET',])
def services_landing_page():
    pass