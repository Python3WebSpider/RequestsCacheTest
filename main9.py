import requests_cache
import requests
import time

urls_expire_after = {'*.site_1.com': 30, 'site_2.com/static': -1}
requests_cache.install_cache(
    'demo_cache2', urls_expire_after=urls_expire_after)
