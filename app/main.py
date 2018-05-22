import logging
from flask import Flask
from app.rest.restController import message_requests

app = Flask(__name__)
app.register_blueprint(message_requests)

logger = logging.getLogger('gunicorn.error')


@app.route('/')
def hello():
    logger.info('hello')
    return 'Hello World!'


@app.route('/keep-alive')
def keep_alive():
    return '200 OK'


@app.errorhandler(500)
def server_error(e):
    logger.info('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    # logging.basicConfig(filename='/opt/behalf/cto/reporting/log/reporting.log', level=logging.INFO)
    app.run(port=8080, debug=True)
