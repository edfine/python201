from celery import Celery

app = Celery('celery_lab', broker='amqp://guest@localhost//')

@app.task
def write_file(filename, data):
    with open(filename, 'w') as f:
        print(data, file=f)


