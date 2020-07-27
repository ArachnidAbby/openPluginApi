plugin = myCustomPluginApi('0.1', 'my plugin')
plugin.x = 0
name = plugin.INFO["name"]
version = plugin.INFO["version"]

@plugin.Enable
def onEnable():
    print(f"loaded {name} version {version}")
    plugin.pinky()

@plugin.render
def render():
    display.fill((255,255,255))
    pygame.draw.rect(display,(0,0,0),[plugin.x,plugin.x,50,50])
    plugin.x+=0.5

@plugin.Disable
def DisableFunction():
    plugin.pinky()
    print('pluginDisable')

plugin.start()