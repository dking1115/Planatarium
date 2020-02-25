class planatarium(object):
    
    def __init__ (self):
        self.planets=[]
        Mercury=Planet("Mercury",".055M","Grey")
        Venus=Planet("Venus","4.8675×1024 kg","Tan")
        self.planets.append(Mercury)
        self.planets.append(Venus)
    def __str__ (self):
        for i in self.planets:
            stri+=str(i)
        return(stri)