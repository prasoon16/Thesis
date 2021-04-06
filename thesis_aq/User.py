import utility as utl

class User(object):
    """class for user doing bid"""
    def __init__(self, index, longitude, latitude, datetime):
        self.index = index
        self.longitude = longitude
        self.latitude = latitude
        self.datetime = datetime
        self.cost = self.get_trac_cost()
    def get_trac_cost(self):
        mu = int(utl.uniform(15,50,1))
        sigma = int(utl.uniform(2,3,1))
        return int(utl.normal(mu, sigma, 1))
    def print_user(self):
        print ("index {} longitude {} latitude {} datetime {} cost {}".format(self.index, self.longitude, self.latitude, self.datetime, self.cost))
