from flask import Blueprint

KettleStatus_blueprint = Blueprint('kettle_status', __name__, static_folder=None)


@KettleStatus_blueprint.route('/test-of-paths')
def status_of_kettle():
    return "Test Succeeded"
