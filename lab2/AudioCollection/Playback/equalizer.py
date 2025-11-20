from Exceptions.equalizer_settings_error import EqualizerSettingsError

class Equalizer:
    """
    Equalizer class
    """
    def __init__(self, bass=0, mid=0, treble=0):
        """
        Constructor
        :param bass: Low frequency
        :param mid: Mid frequency
        :param treble: High frequency
        """
        self.__bass = bass
        self.__mid = mid
        self.__treble = treble

    def adjust(self, bass=None, mid=None, treble=None):
        """
        Changes equalizer settings
        :param bass: Bass
        :param mid: Mid
        :param treble: Treble
        :return: Updated equalizer settings
        """
        values = [i for i in range(0, 11)]
        if bass not in values or mid not in values or treble not in values:
            raise EqualizerSettingsError("Set the value from 0 to 10")
        self.__bass = bass
        self.__mid = mid
        self.__treble = treble

    def __str__(self):
        return f"Bass:{self.__bass}, Mid:{self.__mid}, Treble:{self.__treble}"
