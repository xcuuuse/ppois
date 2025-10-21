from audio.base import AudioFormat, AudioFile, Converter

form = AudioFormat(".wav")
form2 = AudioFormat(".flac")
file = AudioFile("e:/numb.wav", 183, form, 1024)
print(file.get_info())

converter = Converter([form, form2])
converter.convert_file(file, form2)
print(file.get_info())


# maybe do the logic of file size changing
