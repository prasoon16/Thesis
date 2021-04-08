import utility as utl

class Task(object):
    """Task published to users"""

    def __init__(self, index, place, longitude, latitude):
        self.index = index
        self.place = place
        self.longitude = longitude
        self.latitude = latitude
        self.expected_quality = self.get_expected_quality()
    def get_expected_quality(self):
        mu = int(utl.uniform(35,50,1))
        sigma = int(utl.uniform(2,3,1))
        return int(utl.normal(mu,sigma,1)[0])
    def print_task(self):
        print ("index {} place {} longitude {} latitude {} quality {}".format(self.index, self.place, self.longitude, self.latitude, self.expected_quality))
