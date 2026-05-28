"""Data-layer repositories.

Skeleton only. The plan is to split the monolithic data-access module into
focused query objects, one per aggregate root. See issue #1.
"""


class UserRepository:
    """Read/write access to User aggregates."""

    def get(self, user_id):
        raise NotImplementedError

    def save(self, user):
        raise NotImplementedError


class OrderRepository:
    """Read/write access to Order aggregates."""

    def get(self, order_id):
        raise NotImplementedError

    def save(self, order):
        raise NotImplementedError
