class TrackId:
    __track_id = 0

    @classmethod
    def generate_id(cls):
        cls.__track_id += 1
        return cls.__track_id