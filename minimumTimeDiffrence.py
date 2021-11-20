# Given a list of 24-hour clock time points in "HH:MM" format,
# return the minimum minutes difference between any two time-points in the list.
from datetime import datetime


def findMinDifference(timePoints):
    timeList = []
    for time in timePoints:
        minutes = int(time[0:2]) * 60 + int(time[3:5])
        timeList.append(minutes)

    timeList.sort()
    print(timeList)
    diff = float('inf')
    for i in range(len(timeList) - 1):
        diff = min(diff, timeList[i + 1] - timeList[i])
    # add a day to 1st element and substract  and compare to the last


    return diff



if __name__ == '__main__':

    print (findMinDifference(["23:59", "00:01", "02:00"]))
