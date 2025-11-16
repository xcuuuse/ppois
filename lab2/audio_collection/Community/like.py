class Like:
    """
    Like class
    """
    def __init__(self, target: object):
        """
        Constructor
        :param target: object
        """
        self.target = target

    def __repr__(self):
        return f"<Like to {type(self.target).__name__}>"

