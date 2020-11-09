
# This problem takes in two calendars written in military time, and returns an free times the two can both meet.
def between(cal1, cal2):
    freeTimes = []
    calendar = allTaken(cal1, cal2)
    for i in range(len(calendar)-1):
        time1 = calendar[i][1].split(':')
        time2 = calendar[i+1][0].split(':')
        freehour = int(time2[0])-int(time1[0])
        freeminute = int(time2[1]) - int(time1[1])
        if int(time2[1]) < int(time1[1]):
            freehour = freehour - 1
            freeminute = 60 - freeminute
        freeTimes.append((freehour, freeminute, calendar[i][1], calendar[i+1][0]))
    return freeTimes

def combine(calendar1, calendar2):
    cal1 = calendar1
    cal2 = calendar2
    allTimes = []
    i, j = 0, 0
    while i < len(cal1) and j < len(cal2):
        time1 = cal1[i][0].split(':')
        time2 = cal2[j][0].split(':')
        timecheck1 = int(''.join(time1))
        timecheck2 = int(''.join(time2))
        addTime1 = cal1[i]
        addTime2 = cal2[j]

        if timecheck1 < timecheck2:
            allTimes.append(addTime1)
            i += 1
        elif timecheck1 > timecheck2:
            allTimes.append(addTime2)
            j += 1
        elif timecheck1 == timecheck2:
                allTimes.append(addTime2)
                allTimes.append(addTime1)
                i += 1
                j += 1
    while i < len(cal1):
        allTimes.append(cal1[i])
        i += 1
    while j < len(cal2):
        allTimes.append(cal2[j])
        j += 1
    return allTimes

def allTaken(cal1, cal2):
    calendar = combine(cal1, cal2)
    newList = calendar[:]
    i = 0
    while i < (len(newList)-1):
        time1 = newList[i][1].split(':')
        time2 = newList[i+1][0].split(':')
        time3 = newList[i + 1][1].split(':')

        timecheck1 = int(''.join(time1))
        timecheck2 = int(''.join(time2))
        timecheck3 = int(''.join(time3))

        if timecheck1 > timecheck3:
            newend = newList[i][1]
        else:
            newend = newList[i+1][1]

        if timecheck1 >= timecheck2:
            newList[i] = (newList[i][0],newend)
            del newList[i+1]
        else:
            i += 1
    return newList







class calendarMatch:
    def __init__(self, calendar1, calendar2):
        self.calendar1 = calendar1
        self.calendar2 = calendar2
    def match(self):
        free = between(self.calendar1, self.calendar2)
        for f in free:
            print(("you both are free to meet for %s hours and %s minutes from %s to %s" %(f[0], f[1], f[2], f[3])))















cal1 = [('9:25', '10:00'), ('12:30', '13:30'),('14:30',"14:45")]
daylen1 = ('9:00', "18:00")
cal2 = [('8:00','9:00'), ('9:00', '10:00'), ('12:00', '14:22')]
cal = calendarMatch(cal1,cal2)
# print(combine(cal1, cal2))
print(cal.match())





