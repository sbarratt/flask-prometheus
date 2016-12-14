# Flask-Prometheus

## About
Out of the box, this flask extension makes it extremely easy to monitor your application using SoundCloud's Prometheus. For more on Prometheus, see their [website](prometheus.io).

This extension instruments every flask route and exports the following metrics:
* Histogram: `<flask_request_latency_seconds> {'endpoint', 'method'}`
* Summary: `<flask_request_count> {'endpoint','method','http_status'}`

## Installation
```
pip install flask_prometheus
```

## Basic Usage
Type the following into an interpreter:
```
from flask import Flask
from flask_prometheus import monitor 

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'

monitor(app, port=8000)
app.run()
```

Now, naviagate `localhost:5000` a few times and then view metrics on `localhost:8000` which should look like:
```
# HELP flask_request_count Flask Request Count
# TYPE flask_request_count counter
flask_request_count{endpoint="/",http_status="200",method="GET"} 4.0
# HELP flask_request_latency_seconds Flask Request Latency
# TYPE flask_request_latency_seconds histogram
flask_request_latency_seconds_bucket{endpoint="/",le="0.005",method="GET"} 4.0
flask_request_latency_seconds_bucket{endpoint="/",le="0.01",method="GET"} 4.0
flask_request_latency_seconds_bucket{endpoint="/",le="0.025",method="GET"} 4.0
flask_request_latency_seconds_bucket{endpoint="/",le="0.05",method="GET"} 4.0
flask_request_latency_seconds_bucket{endpoint="/",le="0.075",method="GET"} 4.0
flask_request_latency_seconds_bucket{endpoint="/",le="0.1",method="GET"} 4.0
flask_request_latency_seconds_bucket{endpoint="/",le="0.25",method="GET"} 4.0
flask_request_latency_seconds_bucket{endpoint="/",le="0.5",method="GET"} 4.0
flask_request_latency_seconds_bucket{endpoint="/",le="0.75",method="GET"} 4.0
flask_request_latency_seconds_bucket{endpoint="/",le="1.0",method="GET"} 4.0
flask_request_latency_seconds_bucket{endpoint="/",le="2.5",method="GET"} 4.0
flask_request_latency_seconds_bucket{endpoint="/",le="5.0",method="GET"} 4.0
flask_request_latency_seconds_bucket{endpoint="/",le="7.5",method="GET"} 4.0
flask_request_latency_seconds_bucket{endpoint="/",le="10.0",method="GET"} 4.0
flask_request_latency_seconds_bucket{endpoint="/",le="+Inf",method="GET"} 4.0
flask_request_latency_seconds_count{endpoint="/",method="GET"} 4.0
flask_request_latency_seconds_sum{endpoint="/",method="GET"} 0.0010027885437011719
```

Beware, this seems to not work when the app is run in debug mode.
