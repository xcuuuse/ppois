from IdManage.id_generator import IdGenerator


class AlbumId(IdGenerator):
    """
    Album id class
    """
    __album_id = 0

    @classmethod
    def generate_id(cls):
        """
        A method to generate album id
        :return:
        """
        cls.__album_id += 1
        return cls.__album_id
