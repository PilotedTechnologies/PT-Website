from flask import Flask, redirect, url_for, jsonify
from routes import about_us_blueprint, services_blueprint, api_blueprint, demo_blueprint, landing_blueprint, login_blueprint, pricing_blueprint

app = Flask(__name__)
app.config.from_object('config.DevConfig')

app.register_blueprint(landing_blueprint, url_prefix='/home')
app.register_blueprint(services_blueprint, url_prefix='/services')
app.register_blueprint(demo_blueprint, url_prefix='/demo')
app.register_blueprint(pricing_blueprint, url_prefix='/pricing')
app.register_blueprint(api_blueprint, url_prefix='/api')
app.register_blueprint(about_us_blueprint, url_prefix='/about-us')
app.register_blueprint(landing_blueprint, url_prefix='/login')

@app.route('/')
def home():
    """Redirects root url to home url
    """
    return redirect(url_for('landing.landing_page'))


if __name__ == "__main__":
    app.run(port=app.config['PORT'], debug=app.config['DEBUG'])