from flask import Flask

from .health import health

app = Flask(__name__)

@app.route('/')
def index():
    return {'service': 'acme-api', 'version': '0.1.0'}

@app.route('/health')
def health_route():
    return health()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
