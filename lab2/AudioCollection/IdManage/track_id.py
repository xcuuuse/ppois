from IdManage.id_generator import IdGenerator

class TrackId(IdGenerator):
    """
    Track id class
    """
    __track_id = 0

    @classmethod
    def generate_id(cls):
        """
        Generates track id
        :return: track id
        """
        cls.__track_id += 1
        return cls.__track_id
