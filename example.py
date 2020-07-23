from OpenPluginApi import ApiCreator
import pygame
scheduler = ApiCreator.Schedule.scheduler()

global Nugget
Nugget = "p"

class myCustomPluginApi(ApiCreator.ApiTemplates.EnableDisableApi):
    def __init__(self,v,n):
        super().__init__(version = v,name = n)
    def start(self):
        self.FUNCS['ENABLE']()
        self.FUNCS['DISABLE']()
    def pinky(self):
        global Nugget
        print(Nugget)
        Nugget+="+"
    def render(self, func):
        self.FUNCS["render"] = func
        scheduler.schedule("render",self)
        print("toilet")
    
def main():
    scheduler.addEvent("render")
    display = pygame.display.set_mode((600,600))
    d = dict(locals(), **globals())
    ApiCreator.PluginLoader.load("examplePlugin.py",d,d)
    while True:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()
            for s in scheduler.getScheduled("render"):
                s[1]["render"]()
            pygame.display.update()

main()
print(Nugget)