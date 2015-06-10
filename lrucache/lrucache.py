from collections import OrderedDict
import threading

DEFAULT_SIZE = 100

class LRUCache(object):
    """
    OrderedDict is used to invalidate LRU (least recently used) item from cache (http://code.activestate.com/recipes/576693/). Alternative is using linkedlist and hashmap (http://stackoverflow.com/questions/12808387/regarding-lru-cache-design-using-hashmap-and-linked-list-combination or http://www.programcreek.com/2013/03/leetcode-lru-cache-java/) or splay tree (http://en.wikipedia.org/wiki/Splay_tree).
    """
    def __init__(self, size=DEFAULT_SIZE, nonExistVal=None):
        #print "LRUCache.__init__(size=%s,  nonExistVal=%s)" % (size, nonExistVal)
        size = int(size)
        if size < 1:
            size = DEFAULT_SIZE

        self.size = size
        self.nonExistVal = nonExistVal
        self.lock = threading.Lock()
        self.dict = OrderedDict()


    def get(self, key):
        with self.lock:
            if self.dict.has_key(key):
                oldVal = self.dict.pop(key)
                self.dict[key] = oldVal
            return self.dict.get(key, self.nonExistVal)


    def put(self, key, val):
        with self.lock:
            if self.dict.has_key(key):
                oldVal = self.dict.pop(key)
            else:
                if len(self.dict) >= self.size:
                    #print "invalidating key=%s" % key
                    #print "invalidating cache size=%s" % len(self.dict)
                    self.dict.popitem(last=False) # item first inserted will get popped out
            self.dict[key] = val

        
    def size(self):
        return len(self.dict)



class lrucache_decorator(object):
    def __init__(self, *args, **kwargs):
        self.cache = LRUCache(*args, **kwargs)
        try:
            self.nonExistVal = kwargs.get('nonExistVal', None) or args[1]
        except Exception as e:
            self.nonExistVal = None
#            print "Warning: nonExistVal set to None at lrucache_decorator.__init__. %s" % e


    def __call__(self, func):
        def wrapped_func(*args):
            key = args[-1]
            if self.cache.get(key) is not self.nonExistVal:
                return self.cache.get(key)

            val = func(*args)
            self.cache.put(key, val)
            return val            
        return wrapped_func
