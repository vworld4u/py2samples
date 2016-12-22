# py2samples
Samples in Python2 - Worked to practice and test few things in python 2


## Lesson 1: How to use logging in case of Multi processing?
1. Configure logger at a central place - like the initial place which invokes the other processes. 
    * Configure the logger with basic configuration like FileHandler 
    * Configure the stream handler to handle the logging for only info level logs (see the code for class InfoConsoleHandler for such a handler)
2. Get the instance of the logger configured in the above step in all modules/sub modules/processes that you use further on to get the same logger used
    * Use `logger = logging.getLogger("SamePackageNameUsedAbovewhileconfiguring")` to get the logger
    * Use logger.info/debug/error etc to log whatever you want to log
3. The code is contained within `src/multiprocesssample.py`.
    * It contains the code for sample of multiprocessing 
    * Also a Logger configuration example at central place and using logger in individual modules (like list_append process)
    * Custom Stream Handler for Logging which filters out all but INFO messages to console
    * File Handler which dumps all logs to central single log file.
4. Run the application `python multiprocesssample.py` to see it working.
