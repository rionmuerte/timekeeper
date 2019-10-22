import os

rootPath = os.path.dirname(os.path.abspath(__file__))
dataPath = os.path.join(rootPath, '.data')
if not os.path.isdir(dataPath):
    os.mkdir(dataPath)
projectFolderDataRoot = os.path.join(dataPath,'{}')
tempFileTemplate = os.path.join(projectFolderDataRoot,'data.temp')
dataFileTemplate = os.path.join(projectFolderDataRoot,'data.dat')


def doesProjectExist(project):
    return os.path.isdir(os.path.join(dataPath,project))

def listAllProjects():
    return [dir for dir in os.listdir(dataPath) if doesProjectExist(dir)]

def doesTempFileExist(project):
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
    return os.path.isfile(dataFileTemplate.format(project))

def getProjectDataFile(project, fileArgs):
    if not doesProjectExist(project): raise NameError('Project of that name does not exist')
    filePath = dataFileTemplate.format(project)
    return open(filePath, fileArgs)
