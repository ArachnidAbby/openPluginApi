plugin = myCustomPluginApi('0.1', 'my plugin')
name = plugin.INFO["name"]
version = plugin.INFO["version"]

@plugin.Enable
def onEnable():
    print(f"loaded {name} version {version}")
    plugin.pinky()

@plugin.render
def render():
    display.fill((255,255,255))

@plugin.Disable
def DisableFunction():
    plugin.pinky()
    print('pluginDisable')

plugin.start()