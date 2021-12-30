
from datetime import datetime, timedelta

if __name__ == '__main__':
    format = '%a %d %b %Y %H:%M:%S %z'                          # create a time format
    n = int (input ())
    for i in range (n):
        t_1 = datetime.strptime (input (), format)              # convert the given string in to made time format
        t_2 = datetime.strptime (input (), format)

        print (int (abs ((t_1 - t_2).total_seconds ())))        # get the time different in seconds
