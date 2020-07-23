class blankApi:
    def __init__(self, version  = "0.0.1", name = "My Plugin"):
        self.API_INFO = {'type':'blank', 'version':version, 'api-name':name}
    
    def start(self):
        None

class EnableDisableApi:
    def __init__(self, version  = "0.0.1", name = "My Plugin"):
        self.API_INFO = {'type':'Enable-Disable', 'version':version, 'api-name':name}
        self.FUNCS = {}
    def start(self):
        None
    def Enable(self, func):
        self.FUNCS['ENABLE'] = func
    def Disable(self, func):
        self.FUNCS['DISABLE'] = func