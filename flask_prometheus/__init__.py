
import time

from prometheus_client import Counter, Histogram
from prometheus_client import start_http_server
from flask import request

FLASK_REQUEST_ENDPOINT_SENTINEL = '-'
FLASK_REQUEST_LATENCY = Histogram('flask_request_latency_seconds', 'Flask Request Latency',
				['method', 'endpoint'])
FLASK_REQUEST_COUNT = Counter('flask_request_count', 'Flask Request Count',
				['method', 'endpoint', 'http_status'])


def before_request():
    request.start_time = time.time()


def after_request(response):
    request_latency = time.time() - request.start_time

    endpoint = request.url_rule.rule if request.url_rule else FLASK_REQUEST_ENDPOINT_SENTINEL
    
    FLASK_REQUEST_LATENCY.labels(request.method, endpoint).observe(request_latency)
    FLASK_REQUEST_COUNT.labels(request.method, endpoint, response.status_code).inc()

    return response

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
