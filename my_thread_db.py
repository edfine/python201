from time import sleep
from threading import Thread
from random import randint

running = True

class DatabaseServer(Thread):
    """process imaginary database requests"""
    def run(self):
        """
        Whatever is in the run method (or called from
        it, is executed in a separate thread
        """
        while running:
            sec = randint(10, 20)
            print('Processing database request for', sec, 'seconds')
            sleep(sec)
            print('Finished processing database request')
        print('The user has requested the database server stop running.')        

if __name__ == '__main__':
    input('Are you ready? When you hit return the thread will start.')
    thread = DatabaseServer() # create thread object
    thread.start() 

    while thread.is_alive():
        text = input('Enter some text: ')
        print(text.title()[::-1])
        if text == 'qqq':
            running = False
            break

