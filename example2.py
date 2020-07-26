from OpenPluginApi import ApiCreator
import pygame
pygame.init()

scheduler = ApiCreator.Schedule.scheduler()

class ExamplePluginApi(ApiCreator.ApiTemplates.EnableDisableApi):
    def __init__(self, title, desc, ver):
        super().__init__(version = ver, name = title)
        self.INFO["description"] = desc
    
    def start(self):
        self.FUNCS['ENABLE']()
        self.FUNCS['DISABLE']()
    
    def render(self, func):
        scheduler.schedule("render", self, func)

def main():
    display = pygame.display.set_mode((600,600))
    scheduler.addEvent("render")
    clock = pygame.time.Clock()
    d = dict(locals(),**globals())
    ApiCreator.PluginLoader.load("examplePlugin2.py",d,d)
    while True:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.fill((255,255,255))
        for scheduled in scheduler.getScheduled("render"):
            scheduled["func"]()
        pygame.display.update()
main()