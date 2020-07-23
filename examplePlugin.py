plugin = myCustomPluginApi()

@plugin.Enable
def onEnable():
    plugin.pinky()

@plugin.Disable
def DisableFunction():
    plugin.pinky()
    print('pluginDisable')

plugin.start()