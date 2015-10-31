# -*- encoding: utf-8 -*-
import scene

class PauseScene(scene.Scene):

    def __init__(self, director, current_scene):
        scene.Scene.__init__(self, director)
		

    def update(self):
        pass

    def event(self):
        pass

    def draw(self, screen):
        pass
	
	def quit(self):
		self.director.quit()
