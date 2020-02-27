class Planet(object):
    
    def __init__ (self,name,mass,color):
        self.name=name
        self.mass=mass
        self.color=color
    def mass(self):
        return(self.mass)
    def name(self):
        return(self.name)
    def color(self):
        return(self.color)
    def __str__(self):
        string=("{name()},{mass()},{color()}")
        return(string)