import pygame

from threading import Thread
pygame.init()
class Window():
    def __init__(self,window_size=(500,500),display=None):
        if display == None:
            self.display = pygame.display.set_mode(window_size)
        else:
            self.display = display

        self.loops = []
        self.start = False
        self.render = {}

        self.build()
    def add_widget(self,widget):

        self.render[widget.name] = widget

    def run(self):
        while True:
            self.main_loop()
    def stop(self):
        pygame.quit()
    def add_loop(self,loop):
        print(loop)
        self.loops.append(loop)
    def main_loop(self):
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            self.update_widget(ev)
        th = Thread(target=self.start_loop)
        th.start()
        th = Thread(target=self.show_widget)
        th.start()

        pygame.display.update()
    def update_widget(self,ev):
        for i in self.render:
            #print(self.render[i])
            self.render[i].update(self.display,ev)
    def show_widget(self):
        for j in self.render:
            #print(self.render[i])

            self.render[j].draw(self.display)
    def start_loop(self):
        for loop in self.loops:

            th = Thread(target=loop)
            th.start()
