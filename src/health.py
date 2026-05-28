"""Health check endpoint helpers."""


def health():
    """Return a simple health status payload."""
    return {'status': 'ok'}
