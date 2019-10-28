import time

import dataHandler

def startCounter(project):
    if dataHandler.doesTempFileExist(project):
        raise FileExistsError("Counter already started for this project")
    with dataHandler.getProjectTempFile(project, 'w+') as file:
        currentTimestamp = int(time.time())
        file.write(str(currentTimestamp))

def stopCounter(project, percentage):
    if not dataHandler.doesTempFileExist(project):
        raise FileNotFoundError("This projects counter was not started in this session")
    currentTimestamp = int(time.time())
    startTime = _getStartTimeOfProject(project)
    timeSpent = currentTimestamp - startTime
    dataHandler.removeProjectTempFile(project)
    _saveNewRecordToDataFile(project, startTime, currentTimestamp, timeSpent,percentage)

def _saveNewRecordToDataFile(project, startTime, endTime, timeSpent, percentage):
    with dataHandler.getProjectDataFile(project) as file:
        data = dataHandler.dataFileRecordTemplate.format(
            startTime,
            endTime,
            timeSpent,
            percentage
        )
        file.write(data)

def _getStartTimeOfProject(project):
    with dataHandler.getProjectTempFile(project,'r') as file:
        data = file.readlines()
        return int(data[0])


