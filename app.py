from flask import Flask, render_template
from dotenv import load_dotenv
from api.views.one_min_approved import one_min_approved
from api.views.five_min_approved import five_min_approved
from api.views.one_min_no_approved import one_min_no_approved
from api.views.five_min_no_approved import five_min_no_approved
from api.views.one_min_approved_map import one_min_approved_map

load_dotenv(verbose=True)


def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    return app
  
app = create_app('config.default_settings.Config')
app_context = app.app_context()
app_context.push()

# Blueprint registration of views
app.register_blueprint(one_min_approved)
app.register_blueprint(five_min_approved)
app.register_blueprint(one_min_no_approved)
app.register_blueprint(five_min_no_approved)
app.register_blueprint(one_min_approved_map)

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=8082, passthrough_errors=True)