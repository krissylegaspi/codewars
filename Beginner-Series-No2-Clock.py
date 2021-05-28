'''
Beginner Series #2 Clock

Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.
'''

def past(h, m, s):
    hourInMinutes = h * 60
    minutesInSeconds = (hourInMinutes + m) * 60
    ms = (minutesInSeconds + s) * 1000
    return ms