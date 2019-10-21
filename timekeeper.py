import time
import sys
import os
import datetime

filePath = os.path.dirname(os.path.abspath(__file__))
tempFile = filePath+'/data.temp'
dataFile = filePath+'/data.dat'

dataFileRecordTemplate = '{}|{}|{}|{}\n'

def parse(data):
    if data[1].lower() == 'start': parseStart()
    elif data[1].lower() == 'stop': parseStop(data)
    elif data[1].lower() == 'raport': parseRaport(data)
    else: returnError()

def parseStart():
    if os.path.exists(tempFile): return parseContinue()
    with open(tempFile, 'w') as file:
        file.write(str(int(time.time())))

def parseStop(data):
    if not os.path.exists(tempFile): return returnError()
    percentage = 100
    startTime = 0
    timestamp = int(time.time())
    timeSpent = 0
    if len(data) == 3: percentage = int(data[2])
    with open(tempFile, 'r') as file:
        a = file.readlines()
        startTime = int(a[0])
    os.remove(tempFile)
    timeSpent = timestamp - startTime
    with open(dataFile, 'a+') as file:
        file.write(dataFileRecordTemplate.format(startTime,timestamp,timeSpent,percentage))
    
def parseRaport(data):
    if len(data) < 3: return returnError()
    dateFrom = parseDate(data[2])
    dateTo = int(time.time())
    listOfRecords = []
    if len(data) == 4: dateTo = parseDate(data[3])
    with open(dataFile, 'r') as file:
        for record in file.readlines():
            start, end, duration, percentage = [int(i) for i in record.split('|')]
            if start >= dateFrom and end <= dateTo: listOfRecords.append((start,end,duration,percentage))
    with open('raport'+str(datetime.datetime.fromtimestamp(time.time())).split()[0]+'.txt','w') as file:
        startText = "Raport for period from {} to {}".format(datetime.datetime.fromtimestamp(dateFrom).date(),datetime.datetime.fromtimestamp(dateTo).date())
        linebreak = 97*'_'
        file.write(linebreak+'\n')
        print(linebreak)
        header = "|{0:^95}|".format(startText)
        file.write(header+'\n')
        print(header)
        inlinebreak = '|'+95*'_'+'|'
        file.write(inlinebreak+'\n')
        print(inlinebreak)
        columnTop = "|{0:^10}|{1:^15}|{2:^15}|{3:^20}|{4:^20}|{5:^10}|".format('Date','Start Time','Finish Time','Total Duration','Effective Duration','Percentage')
        file.write(columnTop+'\n')
        print(columnTop)
        totalDuration = 0
        for record in listOfRecords:
            start,end,duration,percentage = record
            totalDuration += duration*percentage/100
            line = "|{0:>10}|{1:>15}|{2:>15}|{3:>20}|{4:>20}|{5:>10}|".format(str(datetime.datetime.fromtimestamp(start).date()),
                                            str(datetime.datetime.fromtimestamp(start).time()),
                                            str(datetime.datetime.fromtimestamp(end).time()),
                                            str(datetime.timedelta(seconds=duration)).split('.')[0],
                                            str(datetime.timedelta(seconds=duration*percentage/100)).split('.')[0],
                                            str(percentage))
            file.write(line+'\n')
            print(line)
        file.write(inlinebreak+'\n')
        print(inlinebreak)
        endText = 'Total time spent working: {}'.format(str(datetime.timedelta(seconds=totalDuration)))
        footer = "|{0:>95}|".format(endText)
        file.write(footer+'\n')
        print(footer)

def parseDate(date):
    return int(datetime.datetime.timestamp(datetime.datetime.strptime(date,'%d.%m.%Y')))
# print(sys.argv, len(sys.argv))

if len(sys.argv) >= 2:
    parse(sys.argv)

