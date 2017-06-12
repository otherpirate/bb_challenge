from collections import OrderedDict


LRU_SET = 'SET'
LRU_GET = 'GET'

cached = OrderedDict()


def lru_cache(typo, max_size=100):
    def decorator(function):
        def wrapper(key, value=None):
            if key in cached:
                value = cached.pop(key) if typo == LRU_GET else value

            if typo == LRU_SET:
                function(key, value)
            elif typo == LRU_GET and not value:
                value = function(key)

            cached[key] = value
            if len(cached) > max_size:
                lru_key = cached.keys()[0]
                cached.pop(lru_key)

            return cached[key]
        return wrapper
    return decorator


@lru_cache(typo=LRU_SET, max_size=2)
def set_cache_key(key, value):
    print 'Saving in database...'


@lru_cache(typo=LRU_GET, max_size=2)
def get_cache_key(key):
    print '{} not in cached, loading from database...'.format(key)
    return 'Value from database to key {}'.format(key)
