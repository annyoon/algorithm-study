def solution(n, t, m, timetable):
    for i in range(len(timetable)):
        timetable[i] = int(timetable[i][:2]) * 60 + int(timetable[i][3:])
    timetable.sort(reverse = True)
    
    busList = []
    start = 9 * 60
    
    for i in range(n):
        bus = []
        busTime = start + t * i
        for _ in range(m):
            if len(timetable) <= 0 or timetable[len(timetable) - 1] > busTime:
                break
            bus.append(timetable.pop())
        bus.append(busTime)
        busList.append(bus)
        
    lastBus = busList[len(busList) - 1]
    if len(lastBus) <= m:
        return convert(lastBus[len(lastBus) - 1])
    return convert(lastBus[len(lastBus) - 2] - 1)

def convert(time):
    return '{0:0>2}'.format(str((time // 60))) + ':' + '{0:0>2}'.format(str((time % 60)))
