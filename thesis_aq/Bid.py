class Bid(object):
    def __init__(self, task, cost, user, quality):
        self.task = task
        self.cost = cost
        self.user = user
        self.quality = quality
        self.utility = 10000
        self.payment = 10000
    def print_bid(self):
        print ("task {} cost {} user {} quality {}".format(self.task, self.cost, self.user, self.quality))
    def comparator_utility(b1, b2):
        if (b1.utility == b2.utility):
            return 0
        elif (b1.utility<b2.utility):
            return -1
        else:
            return 1
    def comparator_payment(b1, b2):
        if (b1.payment == b2.payment):
            return 0
        elif (b1.payment<b2.payment):
            return -1
        else:
            return 1
