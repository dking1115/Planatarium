from Planet import Planet
class Planatarium(object):
    
    def __init__ (self):
        self.planets=[]
        Mercury=Planet("Mercury",".055M","Grey")
        Venus=Planet("Venus","4.8675x10^24 kg","Tan")
        Earth=Planet("Earth","5.97237×10^24 kg","Blue")
        Mars=Planet("Mars","6.4171×10^23 kg","Red")
        Jupiter=Planet("Jupiter","1.8982×10^27 kg","Redish")
        Saturn=Planet("Saturn","5.6834×10^26 kg","Green")
        Uranus=Planet("Uranus","(8.6810±0.0013)×10^25 kg","Blue")
        Neptune=Planet("Neptune","1.02413×10^26 kg","Blue")
        
        self.planets.append(Mercury)
        self.planets.append(Venus)
        self.planets.append(Earth)
        self.planets.append(Mars)
        self.planets.append(Jupiter)
        self.planets.append(Saturn)
        self.planets.append(Uranus)
        self.planets.append(Neptune)
    def __str__ (self):
        stri=""
        for i in self.planets:
            stri+=str(i)
        return(stri)