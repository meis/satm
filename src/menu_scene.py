# -*- encoding: utf-8 -*-
import scene

class MenuScene(scene.Scene):

    def __init__(self, director, node):
        scene.Scene.__init__(self, director)

    def update(self):
        pass

    def event(self):
        pass

    def draw(self, screen):
        pass

	def quit(self):
		self.director.quit()
