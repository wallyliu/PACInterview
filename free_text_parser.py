# -*- utf-8 -*-
import re, sys, pprint, json

def parser(tpath):
    f = open(tpath, 'r')
    raw_data = f.read().split('\n')

    result = []
    for index, value in enumerate(raw_data):
        if re.findall(r'[0-9]{4} -', value) != []:
            result.append(raw_data[index-1].replace('[HTML] ', ''))
    return json.dumps({'paper_title': result})

if __name__ == '__main__':
    tpath = sys.argv[1]
    result = parser(tpath)
    pprint.pprint(result)
