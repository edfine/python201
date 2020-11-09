from celery import Celery

#app = Celery('tasks', broker='amqp://guest@localhost//')
app = Celery('tasks', backend='rpc://', broker='amqp://')

@app.task
def add(x, y):
    return x + y

@app.task
def exc():
    raise ValueError
