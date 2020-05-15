'''
 Calendar Matching

 # Problem Statement

Imagine that you want to schedule a meeting of a certain duration with a co-worker. You have access to your calendar and your co-worker's
calendar (both of which contain your respective meetings for the day, in the form of [startTime, endTime] ), as well as both of your daily
bounds (i.e., the earliest and latest times at which you're available for meetings every day, in the form of [earliestTime, latestTime].

Write a function that takes in your calendar, your daily bounds, your co-worker's calendar, your co-worker's daily bounds, and the
duration of the meeting that you want to schedule, and that returns a list of all the time blocks (in the form of [startTime, endTime]
during which you could schedule the meeting, ordered from earliest time block to latest.

Note that times will be given and should be returned in military time. For example: 8:30 , 9:01 , and 23:56

Sample Input:

calendarl = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
dailybounds1 = ['9:00','20:00']
calendar2 = [['10:007, '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
dailyBounds2 = ['10:00', '18:30']
meetingDuration = 30

Sample Output :
[['11:30', '12:00'], ['15:00', '16:00'], ['18:00', '18:30']]


'''



def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    updatedCalender1 = updateCalender(calendar1, dailyBounds1)
    updatedCalender2 = updateCalender(calendar2, dailyBounds2)
    mergedCalender = mergeCalenders(updatedCalender1, updatedCalender2)
    flattenedCalender = flattenCalender(mergedCalender)
    return getMatchingAvailabilities(flattenedCalender, meetingDuration)


def updateCalender(calendar, dailyBounds):
    updatedCal = []
    updatedCal.append(["0:00", dailyBounds[0]])
    updatedCal.extend(calendar)
    updatedCal.append([dailyBounds[1], "23:59"])
    return list(map(lambda m: [timeToMinuites(m[0]), timeToMinuites(m[1])], updatedCal))


def timeToMinuites(time):
    hour, mins = list(map(int, time.split(":")))
    return hour * 60 + mins


def mergeCalenders(calender1, calender2):
    merged = []
    i, j = 0, 0
    while i < len(calender1) and j < len(calender2):
        meeting1, meeting2 = calender1[i], calender2[j]
        if meeting1[0] < meeting2[0]:
            merged.append(meeting1)
            i += 1
        else:
            merged.append(meeting2)
            j += 1

    if i < len(calender1):
        merged.extend(calender1[i:])
    if j < len(calender2):
        merged.extend(calender2[j:])
    return merged


def flattenCalender(calender):
    flattened = [calender[0][:]]
    for i in range(1, len(calender)):
        currMeetingStart, currMeetingEnd = calender[i]
        prevMeeringStart, prevMeeringEnd = flattened[-1]
        if prevMeeringEnd >= currMeetingStart:
            newPrevMeeting = [prevMeeringStart, max(prevMeeringEnd, currMeetingEnd)]
            flattened[-1] = newPrevMeeting
        else:
            flattened.append(calender[i])
    return flattened


def getMatchingAvailabilities(calender, meetingDuration):
    availabilities = []
    for i in range(1, len(calender)):
        start = calender[i - 1][1]
        end = calender[i][0]
        duration = end - start
        if duration >= meetingDuration:
            availabilities.append([start, end])
    return list(map(lambda m: [minuitesToTime(m[0]), minuitesToTime(m[1])], availabilities))


def minuitesToTime(minuites):
    hours = minuites // 60
    mins = minuites % 60
    minsStr = "0" + str(mins) if mins < 10 else str(mins)
    return "{}:{}".format(str(hours), minsStr)






