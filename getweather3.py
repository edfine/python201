from threading import Thread
import json
from urllib.request import urlopen
import time

cities = ['Boulder', 'Atlanta',
          'Reno', 'Honolulu', 'Zurich', 'Dubai',
          'Dublin','Stuttgart', 'Rome']

class TempGetter(Thread):
    def __init__(self, city):
        """Initialize our thread

In the previous example, our class which extended Thread did not
need an __init__ method, because there was no per-thread information
to store. Which means that the __init__ method from the superclass
(Thread) was called automatically. Here, because we need to store
per-thread information (the city), we have to explicitly call the
__init__ method of Thread.
        """
        super().__init__()
        self.city = city

    def run(self):
        url_template = (
            'http://api.openweathermap.org/data/2.5/' 
            'weather?q={}&units=imperial'
                        '&&APPID=10d4440bbaa8581bb8da9bd1fbea5617')
        response = urlopen(url_template.format(self.city))
        data = json.loads(response.read().decode())
        self.temperature = data['main']['temp']
        global shared_int
        shared_int = round(self.temperature)

shared_int = 0
threads = [TempGetter(c) for c in cities]
start = time.time()

# start all 10 threads
for thread in threads:
    thread.start()

# wait for all 10 threads to complete
for thread in threads:
    thread.join()

for thread in threads:
    print("it is {0.temperature:.0f}°F in {0.city}"
          .format(thread))
print("Got {} temps in {} seconds"
      .format(len(threads), time.time() - start))

print(shared_int)
