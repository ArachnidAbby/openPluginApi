from OpenPluginApi import ApiCreator
import pygame
scheduler = ApiCreator.Schedule.scheduler()

global foo
foo = "p"

class myCustomPluginApi(ApiCreator.ApiTemplates.EnableDisableApi):
    def __init__(self,v,n):
        super().__init__(version = v,name = n)
    def start(self):
        self.FUNCS['ENABLE']()
        self.FUNCS['DISABLE']()
    def pinky(self):
        global foo
        print(foo)
        foo+="+"
    def render(self, func):
        scheduler.schedule("render",self,func)
        print("added render task")
    
def main():
    scheduler.addEvent("render")
    display = pygame.display.set_mode((600,600))
    clock = pygame.time.Clock()
    d = dict(locals(), **globals())
    ApiCreator.PluginLoader.load("examplePlugin.py",d,d)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
        for s in scheduler.getScheduled("render"):
            s["func"]()
        pygame.display.update()

main()
print(Nugget)