import argparse
version='0.2.0'
description = '''TimeKeeper small tool to keep track of time spent on different activities'''

def getDefaultParser():
    parser = argparse.ArgumentParser(description=description)
    subparser = parser.add_subparsers(title='Commands', dest='command')
    ###########################################################################################
    startParser = subparser.add_parser('start', help='Starts selected activity counter')
    startParser.add_argument('activity',
                            help='Name of activity to start counter for')
    startParser.add_argument('-c', '--create', action='store_true', dest='force',
                            help='Create activity with that name and start it at te same time')
    startParser.add_argument('-f', '--force', action='store_true', dest='force',
                            help='See above')
    startParser.add_argument('-u','--update', action='store_true', dest='update',
                            help='Reset counter on activity, discarding time spent before')
    ###########################################################################################
    stopParser = subparser.add_parser('stop', help='Stops selected activity counter')
    stopParser.add_argument('activity',
                            help='Name of activity to stop counter for')
    stopParser.add_argument('-p', '-percent', dest='percent', type=int, default=100, metavar='N',
                            help='Percent of time spent on activity (default 100)')
    ###########################################################################################
    newParser = subparser.add_parser('new', help='Creates new activity')
    newParser.add_argument('activity',
                            help='Name of activity to create counter for, name should consist of leters, numbers or underscores ("_")')
    newParser.add_argument('-f', '--force', action='store_true', dest='force',
                            help='If activity with that name already exist clear its data and create new at its place')
    newParser.add_argument('-r', '--reset', action='store_true', dest='reset',
                            help='Reset all data from selected activity')
    ###########################################################################################
    removeParser = subparser.add_parser('remove', help='Deletes activity data')
    removeParser.add_argument('activity',
                            help='Cleares data from selected activity')
    ###########################################################################################
    listParser = subparser.add_parser('list', help='Lists all activities')
    listParser.add_argument('target', choices=['all','active','inactive','templates'],
                            help='Displays list of available activities or report templates.')
    listParser.add_argument('-n', '--name', dest='name', metavar='name',
                            help='Searches for substring with "name" in possible results and displays only matching ones')
    ###########################################################################################
    reportParser = subparser.add_parser('report', help='Generates report for selected activity')
    reportParser.add_argument('activity',
                            help='Activity to generate report from')                    
    reportParser.add_argument('-b', '--from', dest='startDate', default='default', metavar='dd.mm.yyyy',
                            help='Date from which to start collecting raports (default - beginning of previous month)')
    reportParser.add_argument('-e', '--to', dest='endDate', default='default', metavar='dd.mm.yyyy',
                            help='End date of the raport (default - end of previous month)')
    reportParser.add_argument('-t', '--template', dest='template', default='default', metavar='name',
                            help='Template name which should be used to genarate name of the report')
    reportParser.add_argument('-o', '--name', dest='name', default='default', metavar='name',
                            help='Output name of generated report (default - "raport-[current date]")')
    return parser
