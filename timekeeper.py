import argumentsParsing
import commandExecutor

def main():
    parser = argumentsParsing.getDefaultParser()
    data = vars(parser.parse_args())
    command = data['command']
    if command == 'start':
        commandExecutor.commandStart(data)
    elif command == 'stop':
        commandExecutor.commandStop(data)
    elif command == 'new':
        commandExecutor.commandNew(data)
    elif command == 'remove':
        commandExecutor.commandRemove(data)
    elif command == 'list':
        commandExecutor.commandList(data)
    elif command == 'report':
        commandExecutor.commandReport(data)


if __name__ == "__main__":
    main()

