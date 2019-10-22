from json import JSONDecoder
from dataHandler import templatesFileTemplate as name

def getJsonValue(template, value):
    decoder = JSONDecoder()
    data = ''
    with open(name.format('default'), 'r') as file:
        for line in file.readlines():
            data+=line
    return decoder.decode(data)[value]
