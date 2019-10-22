import datetime
import dataHandler
import templateReader

def printTheReport(project, dateFrom, dateTo, template):
    try:
        if not dataHandler.doesDataFileExist(project):
            return print("Selected project does not yet have history to report")
        report = _prepareReport(project, dateFrom, dateTo, template)
        print(report)
    except NameError as error:
        print(error.value)

def saveTheReport(project, dateFrom, dateTo, template):
    try:
        if not dataHandler.doesDataFileExist(project):
            return print("Selected project does not yet have history to report")
        report = _prepareReport(project, dateFrom, dateTo, template)
        with dataHandler.getReportFile(project, template) as file:
            file.write(report)

    except NameError as error:
        print(error.value)

def _prepareReport(project, dateFrom, dateTo, template):
    try:
        if not dataHandler.doesDataFileExist(project):
            return print("Selected project does not yet have history to report")
        listOfRecords = _getListOfRecords(project, dateFrom, dateTo)
        reportString = _generateReportString(project, dateFrom, dateTo, template, listOfRecords)
        return reportString
    except NameError as error:
        print(error.value)
    
def _generateReportString(project, dateFrom, dateTo, template, listOfRecords):
    reportString = ''
    header = templateReader.getJsonValue(template, 'header')
    header = header.format(
        dateFrom=dataHandler.getDateFromeTimestamp(dateFrom),
        dateTo=dataHandler.getDateFromeTimestamp(dateTo),
        project=project)
    reportString += header
    rowString = templateReader.getJsonValue(template, 'row')
    timeSpent = 0
    effectiveTimeSpent = 0
    for row in listOfRecords:
        dFrom, dTo, dur, perc = row
        date = dataHandler.getDateFromeTimestamp(dFrom)
        start = dataHandler.getTimeFromeTimestamp(dFrom)
        end = dataHandler.getTimeFromeTimestamp(dTo)
        etime = dur * perc / 100
        effective = dataHandler.durationFromSeconds(etime)
        timeSpent += dur
        effectiveTimeSpent += etime
        parsedRow = rowString.format(
            date=date,
            startTime=start,
            endTime=end,
            totalDuration=dataHandler.durationFromSeconds(dur),
            effectiveDuration=effective,
            percentage=perc
        )
        reportString += parsedRow
    footer = templateReader.getJsonValue(template,'footer')
    footer = footer.format(
        timeSpent=dataHandler.durationFromSeconds(timeSpent),
        effectiveTimeSpent=dataHandler.durationFromSeconds(effectiveTimeSpent))
    reportString += footer
    return reportString

def _getListOfRecords(project, dateFrom, dateTo):
    listOfRecords = []
    with dataHandler.getProjectDataFile(project,'r') as file:
        for record in file.readlines():
            start, end, duration, percentage = [int(text) for text in record.split('|')]
            if start >= dateFrom and end <= dateTo: listOfRecords.append((start,end,duration,percentage))
    return listOfRecords
