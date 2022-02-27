from datetime import timedelta
import requests_cache
import time

start = time.time()
session = requests_cache.CachedSession(
    # Save files in the default user cache dir
    'demo_cache', use_cache_dir=True,
    # Use Cache-Control headers for expiration, if available
    cache_control=True,
    # Otherwise expire responses after one day
    expire_after=timedelta(days=1),
    # Cache POST requests to avoid sending the same data twice
    allowable_methods=['GET', 'POST'],
    # Cache 400 responses as a solemn reminder of your failures
    allowable_codes=[200, 400],
    # Don't match this param or save it in the cache
    ignored_parameters=['api_key'],
    match_headers=True,                # Match all request headers
    stale_if_error=True, )

for i in range(10):
    session.get('http://httpbin.org/delay/1')
    print(f'Finished {i + 1} requests')
end = time.time()
print('Cost time', end - start)
