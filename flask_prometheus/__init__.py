import time
from flask import request
from prometheus_client import Counter, Histogram
from prometheus_client import start_http_server


def monitor(app, port=8000, addr=""):
    FLASK_REQUEST_LATENCY = Histogram(
        "%s_flask_request_latency_seconds" % app.name,
        "Flask Request Latency",
        ["method", "endpoint"],
    )
    FLASK_REQUEST_COUNT = Counter(
        "%s_flask_request_count" % app.name,
        "Flask Request Count",
        ["method", "endpoint", "http_status"],
    )

    def before_request():
        request.start_time = time.time()

    def after_request(response):
        request_latency = time.time() - request.start_time
        FLASK_REQUEST_LATENCY.labels(request.method, request.path).observe(
            request_latency
        )
        FLASK_REQUEST_COUNT.labels(
            request.method, request.path, response.status_code
        ).inc()

        return response

    app.before_request(before_request)
    app.after_request(after_request)
    start_http_server(port, addr)


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    monitor(app, port=8000)

    @app.route("/")
    def index():
        return "Hello"

    # Run the application!
    app.run()
