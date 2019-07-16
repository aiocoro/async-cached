import functools


def asynccached(cache, key):
    """ Returns decorator function to cache async function results.
    """
    def decorator(func):
        if cache is None:
            async def wrapper(*args, **kwargs):
                return await func(*args, **kwargs)
        else:
            async def wrapper(*args, **kwargs):
                k = key(*args, **kwargs)
                try:
                    return cache[k]
                except KeyError:
                    pass
                v = await func(*args, **kwargs)
                try:
                    cache[k] = v
                except ValueError:
                    pass
                return v
        return functools.update_wrapper(wrapper, func)
    return decorator

