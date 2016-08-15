# Flask-Prometheus

## About
Out of the box, this flask extension makes it extremely easy to monitor your application using Prometheus. For more on Prometheus, see their [website](prometheus.io).

## Installation
```
pip install flask_prometheus
```

## Basic Usage
```
from flask import Flask
from prometheus_client import monitor 

app = Flask(__name__)

@app.route('/')
def hello()
return 'Hello'

monitor(app)
app.run()
```
