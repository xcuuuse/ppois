class AudioFormat:
    def __init__(self, extension: str):
        self.__extension = extension

    @property
    def extension(self):
        return self.__extension


class Codec:
    def __init__(self, name: str, supported_formats: list[AudioFormat]):
        self.__name = name
        self.__supported_formats = supported_formats

    @property
    def name(self):
        return self.__name

    @property
    def supported_formats(self):
        return self.__supported_formats

    def get_formats(self):
        forms = []
        for i in self.supported_formats:
            forms.append(i.extension)
        return forms

# find the usage of codec








