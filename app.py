from flask import Flask
from views.items import items_blueprint
from views.alerts import alerts_blueprint


app = Flask(__name__)
app.register_blueprint(items_blueprint, url_prefix='/items')
app.register_blueprint(alerts_blueprint, url_prefix='/alerts')


if __name__ == "__main__":
    app.run(debug=True)
