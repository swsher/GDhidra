idList = ""
with open("id_list.txt", "r") as file:
    idList = file.read()

idDict = {}
isKey = True
curKey = ""
for token in idList.split("\n"):
    if isKey:
        curKey = token
    else:
        curValue = token
        idDict[curKey] = curValue
    isKey = not isKey

funcs = ""
endDict = "STR_TRIGGER_BY_ID = {"
for key, value in idDict.items():
    if "Trigger" in value:
        funcName = "str" + value.replace(" ", "")
        funcs += f"# id {key}\ndef {funcName}(trigger, verbose=False):\n"
        funcs += "    if verbose:\n"
        funcs += "        return strUnfinished(verbose)\n"
        funcs += "    else:\n"
        funcs += "        return strUnfinished(verbose)\n\n"

        endDict += f"\n    {key}: {funcName}"

endDict += "\n}"

fullString = funcs + endDict
with open("ctrigger.py", 'w') as file:
    file.write(fullString)




