# -*- encoding: utf-8 -*-
class Scene:

    def __init__(self, director):
        self.director = director

    def update(self):
        raise NotImplemented("Tiene que implementar el método update.")

    def event(self):
        raise NotImplemented("Tiene que implementar el método event.")

    def draw(self, screen):
        raise NotImplemented("Tiene que implementar el método draw.")
	
	def quit(self):
		self.director.quit()
