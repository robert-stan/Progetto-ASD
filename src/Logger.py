import logging
import csv
import io
import math

lgr = logging.getLogger('AETA Output Info')
lgr.setLevel(logging.DEBUG)

fh = logging.FileHandler('src/Output.csv')
fh.setLevel(logging.DEBUG)

frmt = logging.Formatter('%(asctime)s,%(name)s,%(levelname)s,%(message)s')
fh.setFormatter(frmt)

lgr.addHandler(fh)

def WriteLog(test_time, run_number, elapsed_time, iteration):
    lgr.debug("TEST #" + str(test_time) + 
              ", RUN #" + str(run_number) + 
              ", TIME " + str(truncate(elapsed_time, 2)) + 
              " seconds, ITERATIONS #" + str(iteration) + ", TIME_QS: " + str(truncate((elapsed_time/iteration) * 1000, 3)) + " ms")

def truncate(number, digits) -> float:
    # Improve accuracy with floating point operations, to avoid truncate(16.4, 2) = 16.39 or truncate(-1.13, 2) = -1.12
    nbDecimals = len(str(number).split('.')[1]) 
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper