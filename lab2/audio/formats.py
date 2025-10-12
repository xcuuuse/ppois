from audio.base import Audiofile


class AudioFormat:
    def __init__(self, extension: str): # 13
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


class Converter:
    def __init__(self, default_codec: Codec):
        self.__default_codec = default_codec

    @property
    def default_codec(self):
        return self.__default_codec

    def convert(self, audio: Audiofile, target_format: AudioFormat):
        pass





