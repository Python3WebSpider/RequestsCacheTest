import requests_cache
import time

start = time.time()
session = requests_cache.CachedSession('demo_cache')

for i in range(10):
    response = session.get('http://httpbin.org/delay/1')
    print('response', response)
    print(f'Finished {i + 1} requests')
end = time.time()
print('Cost time', end - start)
