from flask import Blueprint, request, session, Response, render_template, make_response, current_app, redirect, url_for, jsonify
api_blueprint = Blueprint('api', __name__)

# landing page for api
@api_blueprint.route('/', methods=['GET',])
def api_landing_page():
    pass