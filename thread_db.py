from threading import Thread
import random
import time

running = True

class DatabaseServer(Thread):
    """process imaginary database requests"""
    
    def run(self):
        """
        Whatever is in the run method (or called from
        it, is executed in a separate thread
        """
        while running:
            sec = random.randint(10, 20)
            print('Processing database request for', sec, 'seconds')
            time.sleep(sec)
            print('Finished processing database request')
        print('mp has requested the database server stop running.')

thread = DatabaseServer()
thread.start()

while True:
    text = input('Enter some text: ')
    if text == 'qqq':
        running = False
        while thread.is_alive():
            pass
        break
    print(text[::-1], 'deretne uoY ')

