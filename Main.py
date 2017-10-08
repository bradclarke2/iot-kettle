from flask import Flask

from app.KettleStatus import KettleStatus_blueprint

kettle_app = Flask(__name__)
kettle_app.register_blueprint(KettleStatus_blueprint)


@kettle_app.route('/')
def index():
    return "This is the IOT kettle endpoint"


if __name__ == '__main__':
    kettle_app.run(debug=True)
