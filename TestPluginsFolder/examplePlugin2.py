plugin = ExamplePluginApi("my Plugin", "A cool plugin", '0.1')
plugin.myVar = 20

@plugin.Enable
def OnEnable():
    print(f"enabled {plugin.INFO['name']}")

@plugin.Disable
def OnDisable():
    print(f"Disabled {plugin.INFO['name']}")

@plugin.render
def MyRenderFunction():
    pygame.draw.rect(display, (0,0,0), [0, 0, plugin.myVar, plugin.myVar])
    plugin.myVar+=0.5

@plugin.eventListener
def myEvents(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            print((event.key==pygame.K_a))