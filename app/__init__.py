def create_app(config_name):
    from .api_1 import api as api_1_blueprint
    app.register_blueprint(api_1_blueprint,url_prefix='/api/v1.0')
