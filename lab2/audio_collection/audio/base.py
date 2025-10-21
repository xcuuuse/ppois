from audio.formats import AudioFormat


class AudioFile:
    def __init__(self, path: str, duration: int, audio_format: AudioFormat, size: int):
        self.__path = path
        self.__duration = duration
        self.__audio_format = audio_format
        self.__size = size

    @property
    def path(self):
        return self.__path

    @property
    def duration(self):
        return self.__duration

    @property
    def audio_format(self):
        return self.__audio_format.extension

    @property
    def size(self):
        return self.__size

    def set_format(self, form: AudioFormat):
        self.__audio_format = form


    def get_duration_formated(self):
        minutes = self.duration // 60
        seconds = self.duration - ((self.duration // 60) * 60)
        if seconds < 10:
            return f"{minutes}:0{seconds}"
        return f"{minutes}:{seconds}"

    def get_size_formated(self):
        if self.size < 1000:
            return f"{self.size}B"
        elif 1000 <= self.size <= 10 ** 6:
            return f"{self.size / 1000}Kb"
        else:
            return f"{self.size / 10 ** 6}Mb"

    def get_info(self):
        return (f"File: {self.path}, Duration: {self.get_duration_formated()}, "
                f"Format: {self.audio_format}, Size: {self.get_size_formated()}")

    def set_path(self, new_path):
        self.__path = new_path


class Converter:
    def __init__(self, supported_formats: list[AudioFormat]):
        self.__supported_formats = supported_formats

    @property
    def supported_formats(self):
        return self.__supported_formats

    def get_formats(self):
        forms = []
        for i in self.supported_formats:
            forms.append(i.extension)
        return forms

    def convert_file(self, audio: AudioFile, form: AudioFormat):
        if form in self.supported_formats:
            audio.set_format(form)
        for i in range(len(audio.path)):
            if audio.path[i] == '.':
                audio.set_path(audio.path[:i])
                break
        audio.set_path(audio.path + form.extension)





