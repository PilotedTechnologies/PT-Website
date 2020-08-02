from flask import Blueprint, request, session, Response, render_template, make_response, current_app, redirect, url_for, jsonify
demo_blueprint = Blueprint('demo', __name__)

# landing page for api
@demo_blueprint.route('/', methods=['GET',])
def demo_landing_page():
    pass