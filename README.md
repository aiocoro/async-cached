# Caching decorator for async functions

This is a replacement for `@cached()` decorator from `cachetools`. `cachetools` does not support async at the time of writing.


# Installation

```
    pip install async-cached
```


# Example

```
    from cachetools import LRUCache
    from asynccached import asynccached

    
    _cache = LRUCache(maxsize=1)


    @asynccached(cache=_cache, key=lambda arg: arg)
    async def func(arg):
        pass

```

