import OpenPluginApi
import pygame
pygame.init()

scheduler = OpenPluginApi.Schedule.scheduler()

class ExamplePluginApi(OpenPluginApi.ApiTemplates.EnableDisableApi):
    def __init__(self, title, desc, ver):
        super().__init__(version = ver, name = title)
        self.INFO["description"] = desc
    
    def start(self):
        self.FUNCS['ENABLE']()
        self.FUNCS['DISABLE']()
    
    def render(self, func):
        scheduler.schedule("render", self, func)
    def eventListener(self, func):
        scheduler.schedule("event", self, func)

def main():
    display = pygame.display.set_mode((600,600))
    scheduler.addEvent("render")
    scheduler.addEvent("event")
    clock = pygame.time.Clock()
    d = dict(locals(),**globals())
    OpenPluginApi.PluginLoader.loadFolder("TestPluginsFolder",d,d, recursive = True)
    while True:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            for scheduled in scheduler.getScheduled("event"):
                scheduled["func"](event)
        display.fill((255,255,255))
        for scheduled in scheduler.getScheduled("render"):
            scheduled["func"]()
        pygame.display.update()
main()