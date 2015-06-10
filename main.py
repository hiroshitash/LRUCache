from lrucache import lrucache_decorator

class User(object):

    def __init__(self):
        self.counter = 0

    @lrucache_decorator(3, None)
    def getUser(self, userId):
        self.counter += 1
        return "%s_%s" % (userId, self.counter)


if __name__ == '__main__':
    u = User()
    print "getUser(1) == %s" % u.getUser(1)
    print "getUser(2) == %s" % u.getUser(2)
    print "getUser(3) == %s" % u.getUser(3)
    print "getUser(2) == %s" % u.getUser(2)
    print "getUser(1) == %s" % u.getUser(1)
    print "getUser(4) == %s" % u.getUser(4)
    print "getUser(3) == %s" % u.getUser(3)
    print "getUser(1) == %s" % u.getUser(1)
