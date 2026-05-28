"""Redis-backed cache layer."""


class Cache:
    """Thin Redis-backed cache.

    Reviewer feedback addressed: fleshing out get/set so the interface is
    visible. Actual Redis wiring still lands in a follow-up.
    """

    def __init__(self):
        self._store = {}

    def get(self, key):
        """Return the cached value for `key`, or None if absent."""
        return self._store.get(key)

    def set(self, key, value, ttl=None):
        """Cache `value` under `key`. `ttl` is in seconds (unused for now)."""
        self._store[key] = value

    def delete(self, key):
        """Remove `key` from the cache. No-op if absent."""
        self._store.pop(key, None)
