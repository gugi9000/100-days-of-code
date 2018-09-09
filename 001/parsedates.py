'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
from datetime import timedelta
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    return datetime.strptime(line.split()[1], '%Y-%m-%dT%H:%M:%S')


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object.'''
    timestamps = ['', ''] 
    found = 0
    for line in loglines:
        if line.split()[3] == 'Shutdown' and line.split()[4] == 'initiated.':
            # print (f'Found shutdown at {line.split()[1]}')
            timestamps[found] = line.split()[1]
            found = found + 1
    first = datetime.strptime(timestamps[0], '%Y-%m-%dT%H:%M:%S')
    second = datetime.strptime(timestamps[1], '%Y-%m-%dT%H:%M:%S')
    
    return (second - first)
    #print (f'Found shutdown {found} times')
    

# for line in loglines:
#     print(f'{convert_to_datetime(line)}')

# print (time_between_shutdowns(loglines))



