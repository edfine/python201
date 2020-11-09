
from multiprocessing import Process, cpu_count
import time
import os

class MuchCPU(Process):
    def run(self):
        print(os.getpid())
        print(__name__)
        for i in range(200_000_000):
            result = i * i

if __name__ == '__main__':
    print('Running...')
    procs = [MuchCPU() for f in range(cpu_count())]
    t = time.time()
    for p in procs:
        p.start()
    
    for p in procs:
        p.join()
    
    print('work took {} seconds'.format(time.time() - t))
