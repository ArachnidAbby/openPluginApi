from OpenPluginApi import ApiCreator

global Nugget
Nugget = "p"

class myCustomPluginApi(ApiCreator.ApiTemplates.EnableDisableApi):
    def __init__(self):
        super().__init__('0.1','my first api')
    def start(self):
        self.FUNCS['ENABLE']()
        self.FUNCS['DISABLE']()
    def pinky(self):
        global Nugget
        print(Nugget)
        Nugget+="+"
    
def main():
    d = dict(locals(), **globals())
    ApiCreator.PluginLoader.load("examplePlugin.py",d,d)

main()
print(Nugget)