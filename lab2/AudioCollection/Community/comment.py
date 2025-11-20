
class Comment:
    """
    Comment class
    """
    def __init__(self, comment: str):
        """
        Constructor
        :param comment: str
        """
        self.__comment = comment

    def __str__(self):
        return self.__comment

    def edit_comment(self, new_comment: str):
        """
        Edits the comment
        :param new_comment: str
        :return: updated comment
        """
        self.__comment = new_comment
