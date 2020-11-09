import concurrent.futures
import urllib.request
import time

URLS = ['https://www.japan.go.jp/',
        'http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://www.python.org',
        'http://www.wikipedia.org',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://www.apple.com',
        'http://blahblahblah.org']

# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

start = time.time()
# We use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # start the load operations and mark each future with its URL
    future_to_url = {
        executor.submit(load_url, url, 60): url for url in URLS }
    
    # asynchronously wait for threads to complete...
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print(f'{url} generated an exception: {exc}')
        else:
            print(f'{url} is {len(data)} bytes')
            
print(f'Completed in {time.time() - start:.2f} seconds')