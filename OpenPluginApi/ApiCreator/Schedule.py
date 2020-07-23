def help():
    message = """
Lets your create a "scheduled event"
Once you have an event created you can check if there is anything scheduled under that even.
"""
    print(message)
    return message

class scheduler:
    def __init__(self):
        self.SCHEDULED = {}
    
    def addEvent(self, name: str):
        self.SCHEDULED[name] = []
    
    def schedule(self, eventName : str, pluginObj):
        self.SCHEDULED[eventName].append([pluginObj.INFO["name"],pluginObj.FUNCS])

    def getScheduled(self, eventName: str):
        return self.SCHEDULED[eventName]
    
    def pop(self, eventName: str, index: int):
        self.SCHEDULED[eventName].pop(index)