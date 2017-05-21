from collections import OrderedDict


cached = OrderedDict()


def lru_cache(max_size=100):
    def decorator(function):
        def wrapper(key, value):
            if key in cached:
                cached.pop(key)

            function(key, value)

            cached[key] = value
            if len(cached) > max_size:
                lru_key = cached.keys()[0]
                cached.pop(lru_key)

            return cached[key]
        return wrapper
    return decorator


@lru_cache(max_size=2)
def set_cache_key(key, value):
    pass
