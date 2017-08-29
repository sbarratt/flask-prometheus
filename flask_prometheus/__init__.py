import time

from flask import request
from prometheus_client import Counter, Histogram
from prometheus_client import start_http_server, make_wsgi_app
from werkzeug.wsgi import DispatcherMiddleware

FLASK_REQUEST_LATENCY = Histogram('flask_request_latency_seconds', 'Flask Request Latency',
				['method', 'endpoint'])
FLASK_REQUEST_COUNT = Counter('flask_request_count', 'Flask Request Count',
				['method', 'endpoint', 'http_status'])


def before_request():
    request.start_time = time.time()


def after_request(response):
    request_latency = time.time() - request.start_time
    FLASK_REQUEST_LATENCY.labels(request.method, request.path).observe(request_latency)
    FLASK_REQUEST_COUNT.labels(request.method, request.path, response.status_code).inc()

    return response


def monitor_app(app, path="/metrics"):
    app.before_request(before_request)
    app.after_request(after_request)

    prometheus_app = make_wsgi_app()

    return DispatcherMiddleware(app, {
        path: prometheus_app
    })


def monitor(app, port=8000, addr=''):
    app.before_request(before_request)
    app.after_request(after_request)
    start_http_server(port, addr)

if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)

    monitor(app, port=8000)

    @app.route('/')
    def index():
        return "Hello"

    # Run the application!
    app.run()
