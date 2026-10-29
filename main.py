import requests
import base64
import zlib

from trigger import *

SPEEDS = [251.16, 311.58, 387.42, 468.00, 576.00]

def printI(indentLevel, string):
    print(indentLevel*"  " + string, end="")

# time.sleep does block but oh well its just pseudocode anyway
# maybe improve and restructure later

def hereWeGo(speed, objList):

    # usedIDs = set()

    iL = 0
    # for spawnDict in spawnDictList:
    #     if not spawnDict.get("51") in usedIDs:
    #         printI(iL, f"def async spawn_{spawnDict.get("51")}(delay):")
    #         iL = 1
    #         printI(iL, f"time.sleep(delay)")
    #         if not spawnDict.get("441"):
    #             for objDict in groupIDs[int(spawnDict.get("51"))]:
    #                 if not objDict.get("62"):
    #                     continue
    #                 if objDict.get("1") == "901":
    #                     printI(iL, f"group{objDict.get("51")}.move(x={objDict.get("28")}, y={objDict.get("29")}, duration={objDict.get("10")})")
    #                 elif objDict.get("1") == "1268":
    #                     delay = objDict.get("63") if objDict.get("63") else 0.0
    #                     printI(iL, f"spawn_{objDict.get("51")}({delay})")
    #         else:
    #             leftmostX = 99999999999999999.0
    #             for objDict in groupIDs[int(spawnDict.get("51"))]:
    #                 if float(objDict.get("2")) < leftmostX:
    #                     leftmostX = int(objDict.get("2"))

    #             currentTime = 0.0
    #             for objDict in groupIDs[int(spawnDict.get("51"))]:
    #                 if not objDict.get("62") or (objDict.get("1") != "901" and objDict.get("1") != "1268"):
    #                     continue

    #                 objTime = (float(objDict.get("2"))-leftmostX)/ speed
    #                 deltaT = objTime - currentTime
    #                 if deltaT > 0.0:
    #                     printI(iL, f"time.sleep({deltaT})")

    #                 currentTime += deltaT

    #                 if objDict.get("1") == "901":
    #                     printI(iL, f"group{objDict.get("51")}.move(x={objDict.get("28")}, y={objDict.get("29")})")
    #                 elif objDict.get("1") == "1268":
    #                     delay = objDict.get("63") if objDict.get("63") else 0.0
    #                     printI(iL, f"spawn_{objDict.get("51")}({delay})")
                    

    #         iL = 0
    #         printI(iL, "")
    #         usedIDs.add(spawnDict.get("51"))
    
    printI(iL, "def _level_start(): ")
    iL = 1
    sortedTimedTriggers = []
    for obj in objList:
        if isObjStrTrigger(obj) and (not (obj.get("11") or obj.get("62"))):
            timeOfActivation = max(0.0, float(obj.get("2")))/speed
            sortedTimedTriggers.append([timeOfActivation, obj])

    sortedTimedTriggers.sort(key=lambda x: x[0])
    currentTime = 0.0
    for timedTrigger in sortedTimedTriggers:
        deltaT = timedTrigger[0] - currentTime
        if deltaT > 0.0:
            printI(iL, f"time.sleep({deltaT})\n\n")
        printI(iL, getTriggerStr(timedTrigger[1]))
        currentTime = timedTrigger[0]

# sourced from https://flowvix.github.io/gd-info-explorer/ids
def loadIdsIntoDict():
    fullIdListString = ""
    with open("id_list.txt", 'r') as file:
        fullIdListString = file.read()

    idDict = {}
    isKey = True
    curKey = ""
    for token in fullIdListString.split("\n"):
        if isKey:
            curKey = token
        else:
            curValue = token
            idDict[curKey] = curValue
        isKey = not isKey

    return idDict

OBJECT_ID_DICT = loadIdsIntoDict()
groupIDs = [[] for i in range(0, 10000)] # 0th will never be looked up but who cares]

def getGroupListString(groupID):
    nameArray = [OBJECT_ID_DICT.get(obj.get("1")) for obj in groupIDs[groupID]]
    return f"{groupID}: {nameArray}"


def main():
    # headers = {"User-Agent": ""}
    # data = {"secret": "Wmfd2893gb7", "levelID": 97459496}
    # url = "http://www.boomlings.com/database/downloadGJLevel22.php"
    # request = requests.post(url, data, headers=headers)
    # levelString = request.text.split("#")[0]
    # with open("level.txt", 'w') as file:
    #     file.write(levelObjString)

    levelObjString = ""
    with open("level.txt", 'r') as file:
        levelObjString = file.read()

    levelArray = levelObjString.split(":")

    levelDict = {}
    isKey = True
    curKey = ""
    for token in levelArray:
        if isKey:
            curKey = token
        else:
            curValue = token
            levelDict[curKey] = curValue
        isKey = not isKey

    base64LevelString = levelDict.get("4")
    base64Decoded = base64.urlsafe_b64decode(base64LevelString)
    levelString = zlib.decompress(base64Decoded, 15 | 32).decode()
    objectStringList = levelString.split(";")

    specialInfo = {}
    isKey = True
    curKey = ""
    for token in objectStringList[0].split(","):
        if isKey:
            curKey = token
        else:
            curValue = token
            specialInfo[curKey] = curValue
        isKey = not isKey


    objectDictList = []
    for objectString in objectStringList[1:]:
        objectArray = objectString.split(",")
        
        objectDict = {}
        isKey = True
        curKey = ""
        for token in objectArray:
            if isKey:
                curKey = token
            else:
                curValue = token
                objectDict[curKey] = curValue
            isKey = not isKey

        if objectDict:
            objectDictList.append(objectDict)

    # 901 - move trigger
    # 1268 - spawn trigger

    for objectDict in objectDictList:
        if objectDict.get("57"):
            for group in objectDict.get("57").split("."):
                groupIDs[int(group)].append(objectDict)

    spawnDictList = []
    for objectDict in objectDictList:
        if objectDict.get("1") == "1268":
            spawnDictList.append(objectDict)

    speed = SPEEDS[int(specialInfo.get("kA4"))]
    #for moveDict in moveDictList:
        #print(f"Move Trigger on group {getGroupListString(int(moveDict.get("51")))}, x = {moveDict.get("28")}, y = {moveDict.get("29")}, duration = {moveDict.get("10")}")

    hereWeGo(speed, objectDictList)

if __name__=="__main__":
    main()