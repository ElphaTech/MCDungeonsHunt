import json

inFile = open('sampleData.txt', 'r')
outDict = {}

for line in inFile:
    line = line.strip()
    if "| {{DuItemLink" in line:
        outDict[line.split('|')[-1][:-2]] = ''
        lastDictItem = line.split('|')[-1][:-2]
    
    elif "| data-sort-value=\"1\"" in line:
        outDict[lastDictItem] = f'{outDict[lastDictItem]}{line.split("|")[-1][:-2]}'


inFile.close()
importedJson=open("output.json","w")
importedJson.write(json.dumps(outDict))
importedJson.close()