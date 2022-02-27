import time
import requests
import requests_cache

requests_cache.install_cache('demo_cache', backend='filesystem', use_temp=True)
# requests_cache.install_cache('demo_cache', backend='filesystem', use_cache_dir=True=True)

start = time.time()
session = requests.Session()
for i in range(10):
    session.get('http://httpbin.org/delay/1')
    print(f'Finished {i + 1} requests')
end = time.time()
print('Cost time', end - start)
