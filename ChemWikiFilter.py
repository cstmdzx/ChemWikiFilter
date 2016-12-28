import os
import re
from urllib import unquote
from HtmlToLine import html_to_line

patternParagraph = re.compile('<p>(.+?)</p>')
patternRemoveTag = re.compile('<(.+?)>')

fileInstance = open('Instance', 'w')

listFileNames = os.listdir('storage')  # [0:3]
intCount = 0
for eachFileName in listFileNames:
    if eachFileName.find('Category') != -1:
        continue
    if eachFileName.find('Template') != -1:
        continue

    strDecodeFileName = unquote(eachFileName)
    print strDecodeFileName

    fileTemp = open('./storage/' + eachFileName, 'r')
    linesTemp = fileTemp.readlines()
    lineTemp = html_to_line(linesTemp)

    matchRes = patternParagraph.findall(lineTemp)
    listRes = list()
    for eachRes in matchRes:
        eachRes, number = patternRemoveTag.subn('', eachRes)
        listRes.append(eachRes)
        # print eachRes

    # print res
    decision = raw_input('K/J/H(right/false/detail): ')
    if decision == 'j':
        continue
    if decision == 'k':
        fileInstance.write(strDecodeFileName + '\n')
        # fileInstance.write(str)
        intCount += 1
        for eachRes in listRes:
            eachRes = eachRes.replace('\n', '')
            fileInstance.write(eachRes)

        fileInstance.write('\n')
        fileInstance.write('\n')
        print intCount
        continue
    if decision == 'h':
        for eachRes in listRes:
            eachRes = eachRes.replace('\n', '')
            # fileInstance.write(eachRes)
            print eachRes
        decision = raw_input('K/J(right/false): ')
        if decision == 'j':
            continue
        if decision == 'k':
            fileInstance.write(strDecodeFileName + '\n')
            # fileInstance.write(str)
            intCount += 1
            for eachRes in listRes:
                eachRes = eachRes.replace('\n', '')
                fileInstance.write(eachRes)

            fileInstance.write('\n')
            fileInstance.write('\n')
            print intCount
            continue
        else:
            print 'you fucking idiot'
            continue

    else:
        print 'you fucking idiot'
        continue


print intCount

