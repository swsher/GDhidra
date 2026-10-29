from trigger_str import *
# helper suite for triggers

def isObjStrTrigger(obj):
    return int(obj.get("1")) in STR_TRIGGER_BY_ID

def isObjFuncTrigger(obj):
    return int(obj.get("1")) in FUNC_TRIGGER_BY_ID

def isObjTrigger(obj):
    return isObjStrTrigger(obj) or isObjFuncTrigger(obj) 

def getTriggerStr(trigger, verbose=False):
    strFunc = STR_TRIGGER_BY_ID.get(int(trigger.get("1")))
    if strFunc is None:
        raise Exception("getTriggerStr called with object that is not a trigger")
    return strFunc(trigger, verbose)
