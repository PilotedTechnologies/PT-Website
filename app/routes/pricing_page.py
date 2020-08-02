from flask import Blueprint, request, session, Response, render_template, make_response, current_app, redirect, url_for, jsonify
pricing_blueprint = Blueprint('pricing', __name__)

# landing page for api
@pricing_blueprint.route('/', methods=['GET',])
def pricing_landing_page():
    pass
