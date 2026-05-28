import time

from flask import Flask

app = Flask(__name__)


def check_token(token, now=None):
    """Return True if the token has not expired.

    Tokens are encoded as `payload.expires_at` where expires_at is a
    Unix timestamp. Previously we compared as strings, which caused
    tokens to be treated as valid past their expiry. Compare as ints.
    """
    if not token or '.' not in token:
        return False
    _, _, expires_at = token.rpartition('.')
    try:
        expires_at = int(expires_at)
    except ValueError:
        return False
    if now is None:
        now = int(time.time())
    return now < expires_at


@app.route('/')
def index():
    return {'service': 'acme-api', 'version': '0.1.0'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
