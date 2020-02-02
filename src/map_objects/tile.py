class Tile:
    """
    Represents a tile on a map
    """
    def __init__(self, blocked, block_sight=None):
        """
        User may have a blocking tile that does NOT block sight,
        or a Non-blocking tile that blocks sight
        """
        self._blocked = blocked

        if block_sight is None:
            # By default, a blocking tile blocks sight, and vice versa
            block_sight = blocked
        
        self._block_sight = block_sight

    # BEGIN getters and setters

    @property
    def blocked(self):
        return self._blocked

    @blocked.setter
    def blocked(self, blocked: bool):
            self._blocked = blocked

    @property
    def block_sight(self):
        return self._block_sight

    @block_sight.setter
    def block_sight(self, block_sight: bool):
            self._block_sight = block_sight

    # END getters and setters