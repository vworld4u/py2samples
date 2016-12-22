'''
Created on 04-Dec-2016

@author: venkatesh
'''



import random
import multiprocessing
import logging
import time

def list_append(count, id, out_list):
    """
    Creates an empty list and then appends a 
    random number to the list 'count' number
    of times. A CPU-heavy operation!
    """
    logger = logging.getLogger("abc")
    logger.info("listappend: id = " + str(id))
    for i in range(count):
        out_list.append(random.random())
        logger.info("listappend(" + str(id) + ") Index: " + str(i) + ": Appending:" + str(out_list[-1]))

def main():
    print "MultiProcess Demo"
    size = 100   # Number of random numbers to add
    procs = 2   # Number of processes to create

    # Create a list of jobs and then iterate through
    # the number of processes appending each process to
    # the job list 
    
    logger = logging.getLogger("abc")
    handler = logging.FileHandler("test.log", mode="w", encoding="utf-8")
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    consolehandler = logging.StreamHandler()
    consolehandler.setLevel(logging.DEBUG)
    logger.addHandler(consolehandler)
    jobs = []
    for i in range(0, procs):
        logger.info("initProcess: " + str(i))
        out_list = list()
        process = multiprocessing.Process(target=list_append, 
                                          args=(size, i, out_list))
        jobs.append(process)

    # Start the processes (i.e. calculate the random number lists)        
    for j in jobs:
        logger.info("startProcess: " + str(jobs.index(j)))
        j.start()

    # Ensure all of the processes have finished
    for j in jobs:
        logger.info("waitProcess: " + str(jobs.index(j)))
        j.join()

    logger.info("doneProcess: " + str(time.time()))
    print "List processing complete."

if __name__ == '__main__': main()