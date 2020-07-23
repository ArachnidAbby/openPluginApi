import example
myPlugin = example.myCustomPluginApi()

@api.Enable
def onEnable():
    api.print_funcs()

@api.Disable
def DisableFunction():
    print('pluginDisable')

api.start()