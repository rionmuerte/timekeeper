import argparse
version='0.2.0'
description = '''TimeKeeper small tool to keep track of time spent on different activities'''

parser = argparse.ArgumentParser(description=description)
subparser = parser.add_subparsers(title='Commands', dest='command')
###########################################################################################
startParser = subparser.add_parser('start', help='Starts counter selected project')
startParser.add_argument('project',nargs=1)
###########################################################################################
stopParser = subparser.add_parser('stop', help='Stops counter selected project')
###########################################################################################
newParser = subparser.add_parser('new', help='Creates new project')
###########################################################################################
removeParser = subparser.add_parser('remove', help='Deletes project data')
###########################################################################################
listParser = subparser.add_parser('list', help='Lists all projects')
###########################################################################################
raportParser = subparser.add_parser('raport', help='Generates raport for selected project')



aa = parser.parse_args()
print(vars(aa))