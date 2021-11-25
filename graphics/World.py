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
        self.build()
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

        th = Thread(target=self.start_loop)
        th.start()

        pygame.display.update()
    def start_loop(self):
        for loop in self.loops:

            th = Thread(target=loop)
            th.start()
