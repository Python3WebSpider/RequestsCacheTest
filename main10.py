import time
import requests
import requests_cache

requests_cache.install_cache('demo_cache3', cache_control=True)

start = time.time()
session = requests.Session()
for i in range(10):
    session.get('http://httpbin.org/delay/1',
                headers={
                    'Cache-Control': 'no-store'
                })
    print(f'Finished {i + 1} requests')
end = time.time()
print('Cost time for get', end - start)
start = time.time()
