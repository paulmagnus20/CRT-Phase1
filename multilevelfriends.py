class SKP():
    def Suraj(self,rage):
        self.r=rage
        print(self.r)
class MKT(SKP):
    def Mohana(self,clever):
        self.cl=clever
        print(self.cl)
    def Karun(self,strength):
        self.st=strength
        print(self.st)
class Dhosth(MKT):
    def us(self,compassion):
        self.co=compassion
        print(self.co)
    def pyaar(self,love):
        self.l=love
        print(self.l)
amigo=Dhosth()
amigo.pyaar("love")
amigo.Suraj("rage")
amigo.Karun("strength")
amigo.us("compassion")