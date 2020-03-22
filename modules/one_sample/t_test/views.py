from flask import Blueprint, render_template
from utils import helper


blueprint = Blueprint('ttest', __name__)


@blueprint.route('/one-sample/t-test')
def ttest():
    return render_template('one-sample-tests/t-test.html')


# dosya yüklenecek ve kullanıcı için dosyanın path i saklanacak sessionda


@blueprint.route('/one-sample/t-test', methods=('POST',))
def fileUpload():
    return helper.fileUploader(blueprint)


@blueprint.route('/one-sample/t-test/analyze', methods=('POST',))
def analyze():
    pass