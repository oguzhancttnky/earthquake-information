class Earthquake:
    def __init__(self, d=[""]):
        self.__data = d

    def getDate(self):
        return self.__data[0]

    def getLatitude(self):
        return self.__data[1]

    def getLongitude(self):
        return self.__data[2]

    def getDepth(self):
        return self.__data[3]

    def getType(self):
        return self.__data[4]

    def getMagnitude(self):
        return self.__data[5]

    def getLocation(self):
        return self.__data[6]
