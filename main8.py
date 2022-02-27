import time
import requests
import requests_cache

requests_cache.install_cache('demo_cache2', allowable_codes=(200,))

start = time.time()
session = requests.Session()
for i in range(10):
    session.get('http://httpbin.org/delay/1')
    print(f'Finished {i + 1} requests')
end = time.time()
print('Cost time for get', end - start)
start = time.time()
