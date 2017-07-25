from os import getcwd


class Settings:
    def __init__(self):
        self.save_location = None

    def getLocation(self):
        """ Returns the location where the logs will be saved
        """
        return self.save_location if self.save_location else getcwd()

    def modLocation(self, location):
        """ Allows the user to specify the location where logs will be saved
        """
        self.save_location = location



