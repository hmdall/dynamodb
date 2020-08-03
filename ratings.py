import simplejson as json
import os
import sys


def formatJSON(l, cols):
    json = {}

    for i in range(len(l)):
        json[cols[i]] = {"S": l[i]}

    return json

def process(fileStr):

    f = open('/Users/walkerrowe/Documents/imdb/'+ fileStr, 'r')
    o = open('/Users/walkerrowe/Documents/imdb/' + fileStr + '.json', 'w')

    print('processing ' + fileStr)

    cols = []

    o.write('{ "title": [' + '\n')

    i = 0
    filePos=0
    f.seek(0, os.SEEK_END)
    f.seek(0)

    for l in f:
        ln = l.strip("\\N").strip("\n")
        filePos = filePos + len(l)
        f.seek(filePos)
        line = ln.split('\t')
        if i == 0:
            i = 1
            cols = line
        else:
            if filePos < os.stat(fileStr).st_size:
                o.write ('{ "PutRequest": {"Item":')
                str = json.dumps(formatJSON(line, cols)) + '}},\n'
                o.write(json.dumps(formatJSON(line, cols)) + '}},\n')
            else:
                o.write('{ "PutRequest": {"Item":')
                str = json.dumps(formatJSON(line, cols)) + '}}'
                o.write(str)

    o.write(']}')
    o.close()



if __name__ == "__main__" :

    process(sys.argv[1])
