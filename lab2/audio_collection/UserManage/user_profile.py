from MainEntities.date import Date


class UserProfile:
    """
    User profile class
    """
    def __init__(self, bio: str, birthdate: Date, country:str=""):
        """
        Constructor
        :param bio: Bio
        :param birthdate: Birthdate
        :param country: Country
        """
        self.birthdate = birthdate
        self.bio = bio
        self.country = country

    def __str__(self):
        return f"{self.bio}. {self.country}. {self.birthdate}"