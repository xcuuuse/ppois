class Favourite:
    """
    Favourite objects base class
    """
    def __init__(self):
        self._objects: list[object] = []

    @property
    def objects(self):
        return self._objects

    def add(self, obj: object):
        """
        Adds object to favourite
        :param obj: Object to add
        :return: updated favourite objects
        """
        if obj not in self._objects:
            self._objects.append(obj)

    def remove(self, obj: object):
        """
        Removes the object from favourite
        :param obj: Object to remove
        :return: updated favourite objects
        """
        if obj in self._objects:
            self._objects.remove(obj)
