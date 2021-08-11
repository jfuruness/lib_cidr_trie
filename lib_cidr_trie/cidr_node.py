class CIDRNode:
    def __init__(self, prefix=None, left=None, right=None):
        """Left is 0. Right is 1. Node in CIDR tree"""

        self.prefix = prefix
        self.left = left
        self.right = right

    def add_data(self, prefix):
        """Adds data to node class

        Easy to inherit for things like ROAs
        """

        self.prefix = prefix
