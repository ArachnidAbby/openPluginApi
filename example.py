from OpenPluginApi import ApiCreator
class myCustomPluginApi(ApiCreator.ApiTemplates.EnableDisableApi):
    def __init__(self):
        super().__init__('0.1','my first api')
    def start(self):
        self.FUNCS['ENABLE']()
        self.FUNCS['DISABLE']()
    def print_funcs(self):
        print(self.FUNCS)