
def commandStart(parserArguments):
    activity = parserArguments['activity']
    createNew = parserArguments['force']
    restartCounter = parserArguments['update']
    if createNew:
        _createNewAndStart(activity)
    elif restartCounter:
        _restartCounter(activity)
    else:
        _startActivity(activity)
        pass

def _startActivity(activity):
    try:
        import counterOperations
        counterOperations.startCounter(activity)
    except Exception as e:
        print('Could not start {}'.format(activity))
        print('Exception that occured')
        print(e)

def _restartCounter(activity):
    try:
        import dataHandler
        import counterOperations
        dataHandler.removeProjectTempFile(activity)
        counterOperations.startCounter(activity)
    except Exception as e:
        print('Could not restart activity {}'.format(activity))
        print('Exception that occured:')
        print(e)

def _createNewAndStart(activity):
    try:
        import dataHandler
        import counterOperations
        if not dataHandler.doesProjectExist(activity):
            _createNewActivity(activity)
        counterOperations.startCounter(activity)
    except Exception as e:
        print("Could not start activity {}".format(activity))
        print("Exception that occured:")
        print(e)
    pass

def commandStop(parserArguments):
    activity = parserArguments['activity']
    percent = parserArguments['percent']
    _stopActivity(activity, percent)
    pass

def _stopActivity(activity, percent):
    try:
        if percent < 0: raise ValueError('Percent value should be above 0, but was {}.'.format(percent))
        import counterOperations
        counterOperations.stopCounter(activity,percent)
    except Exception as e:
        print('Could not stop counter on activity {}'.format(activity))
        print('Exception that occured:')
        print(e)

def commandNew(parserArguments):
    activity = parserArguments['activity']
    force = parserArguments['force']
    reset = parserArguments['reset']
    if force:
        _forceCreateNew(activity)
    elif reset:
        _resetActivity(activity)
    else:
        _createNewActivity(activity)

def _createNewActivity(activity):
    try:
        import dataHandler
        dataHandler.createProject(activity)
    except Exception as e:
        print('Could not create new activity')
        print('Make sure that id does not already exist')
        print('Exception that occured:')
        print(e)

def _resetActivity(activity):
    import dataHandler
    if dataHandler.doesProjectExist(activity):
        _forceCreateNew(activity)
    else:
        print('Activity with given name does not exist.')
        print('Make sure that project you try to reset\nexists and try again.')

def _forceCreateNew(activity):
    import dataHandler
    if dataHandler.doesProjectExist(activity):
        _removeAllData(activity)
    dataHandler.createProject(activity)


def commandRemove(parserArguments):
    activity = parserArguments['activity']
    _removeAllData(activity)

def _removeAllData(activity):
    try:
        import dataHandler
        dataHandler.removeProject(activity)
    except Exception as e:
        print('Exception occured while trying to delete activity data')
        print('Make sure that activity exists and are not used anywhere')
        print('Exception that occured:')
        print(e)

def commandList(parserArguments):
    target = parserArguments['target']
    name = parserArguments['name']
    if target == 'all':
        _showAllActivities(name)
    elif target == 'active':
        _showActiveActivities(name)
    elif target == 'inactive':
        _showInactiveActivities(name)
    elif target == 'templates':
        pass
    pass

def _showTemplates(name):
    import dataHandler
    templates = dataHandler.listAllTemplates()
    print('List of templates:')
    if len(templates) == 0:
        print("You have no templates available")
        return
    for template in templates:
        print(template)
    pass

def _showInactiveActivities(name):
    import dataHandler
    activities = dataHandler.listAllProjects()
    print('List of active activities:')
    counter = 0
    for activity in activities:
        if (name is None or name in activity) and not dataHandler.doesTempFileExist(activity):
            counter+=1
            print(activity)
    if counter == 0: print('Currently you have no active activities')

def _showActiveActivities(name):
    import dataHandler
    activities = dataHandler.listAllProjects()
    print('List of active activities:')
    counter = 0
    for activity in activities:
        if (name is None or name in activity) and dataHandler.doesTempFileExist(activity):
            counter+=1
            print(activity)
    if counter == 0: print('Currently you have no active activities')


def _showAllActivities(name):
    import dataHandler
    activities = dataHandler.listAllProjects()
    print('List of all activities:')
    if len(activities) == 0: print('Currently you have no activities')
    for activity in activities:
        if name is None or name in activity:
            print(activity)

def commandReport(parserArguments):
    import reportingTool
    arguments = reportingTool.prepareArguments(parserArguments)
    print(arguments)