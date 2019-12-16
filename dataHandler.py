import os
import datetime

rootPath = os.path.dirname(os.path.abspath(__file__))
dataPath = os.path.join(rootPath, '.data')
if not os.path.isdir(dataPath):
    os.mkdir(dataPath)
projectFolderDataRoot = os.path.join(dataPath,'{}')
tempFileTemplate = os.path.join(projectFolderDataRoot,'data.temp')
dataFileTemplate = os.path.join(projectFolderDataRoot,'data.dat')
dataFileRecordTemplate = '{}|{}|{}|{}\n'
templatesRoot = os.path.join(rootPath,'templates')
templatesFileTemplate = os.path.join(templatesRoot,'{}.json')

def doesProjectExist(project):
    return os.path.isdir(os.path.join(dataPath,project))

def listAllProjects():
    return [dir for dir in os.listdir(dataPath) if doesProjectExist(dir)]

def listAllTemplates():
    return [file.split('.')[0] for file in os.listdir(templatesRoot) if os.path.isfile(os.path.join(templatesRoot, file))]

def createProject(project):
    if doesProjectExist(project): raise NameError('Project of that name already exists')
    os.mkdir(projectFolderDataRoot.format(project))

def removeProject(project):
    if not doesProjectExist(project): raise NameError('Project of that name does not exist')
    directory = projectFolderDataRoot.format(project)
    os.remove(directory)

def doesTempFileExist(project):
    if not doesProjectExist(project): raise NameError('Project of that name does not exist')
    return os.path.isfile(tempFileTemplate.format(project))

def getProjectTempFile(project, fileArgs):
    if not doesProjectExist(project): raise NameError('Project of that name does not exist')
    filePath = tempFileTemplate.format(project)
    return open(filePath, fileArgs)

def removeProjectTempFile(project):
    if not doesProjectExist(project): raise NameError('Project of that name does not exist')
    filePath = tempFileTemplate.format(project)
    os.remove(filePath)

def doesDataFileExist(project):
    if not doesProjectExist(project): raise NameError('Project of that name does not exist')
    return os.path.isfile(dataFileTemplate.format(project))

def getProjectDataFile(project, fileArgs='a+'):
    if not doesProjectExist(project): raise NameError('Project of that name does not exist')
    filePath = dataFileTemplate.format(project)
    return open(filePath, fileArgs)

def getReportFile(project, template, customName = None):
    if not doesProjectExist(project): raise NameError('Project of that name does not exist')
    import templateReader
    extension = templateReader.getJsonValue(template,'extension')
    if customName is not None:
        fileName = customName + extension
    else: 
        reportDate = str(datetime.datetime.now().date())
        fileName = 'report-' + project + '-' + reportDate + extension
    return open(fileName,'w+')

def getDateFromeTimestamp(timestamp):
    return str(datetime.datetime.fromtimestamp(timestamp).date())

def getTimeFromeTimestamp(timestamp):
    return str(datetime.datetime.fromtimestamp(timestamp).time())

def durationFromSeconds(seconds):
    return str(datetime.timedelta(seconds=seconds)).split('.')[0]

def getEndDateFromString(date):
    if date ==  'default':
        import time
        d1 = datetime.datetime.fromtimestamp(time.time()).replace(day=1).timestamp()-datetime.timedelta(days = 1).total_seconds()-1
        return getEndDateFromString(datetime.datetime.fromtimestamp(d1).strftime('%d.%m.%Y'))
    return datetime.datetime.strptime(date, '%d.%m.%Y').timestamp() + datetime.timedelta(days = 1).total_seconds() - 1

def getStartDateFromString(date):
    if date == 'default':
        import time
        d1 = datetime.datetime.fromtimestamp(datetime.datetime.fromtimestamp(time.time()).replace(day=1).timestamp()-datetime.timedelta(days=1).total_seconds()).replace(day=1)
        return getStartDateFromString(d1.strftime('%d.%m.%Y'))
    return datetime.datetime.strptime(date, '%d.%m.%Y').timestamp()