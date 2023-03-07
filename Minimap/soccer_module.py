import numpy as np 
from .FCPython import *
import matplotlib.pyplot as plt 
import matplotlib

class annotate:
    def __init__(self, n = 100):
        self.colors = plt.cm.rainbow(np.linspace(0, 1, n))
        self.n = n
        return

    def CreateIdentity(self, x, y, color, name = 'E', nameloc = 'up', diameter = 2):
        choice = np.random.choice([i for i in range(self.n)])
        passCircle=plt.Circle((x,y),diameter,color=self.colors[choice])
        # passCircle.set_alpha(.2) 
        # passCircle = matplotlib.patches.Circle((x, y), radius=int(diameter/2))# linewidth=7, edgecolor="orange"

        return passCircle 

    def CreateArrow(self, x, y, destx, desty, start_end):
        dx=destx - x
        dy= desty - y
        passArrow=plt.Arrow(x,y,dx,dy,width=3,color="blue")
        return passArrow


class SoccerModule:
    def __init__(self, x = 120, y = 75, unity = 'meters', linecolor = 'blue', court_type = "volleyball"):
        self.xpitch = x 
        self.ypitch = y 
        self.unity = unity
        self.linecolor = linecolor 
        self.court_type = court_type
        return 

    def CreatePitch(self):
        x = self.xpitch
        y = self.ypitch 
        court_type = self.court_type
        unity = self.unity 
        linecolor = self.linecolor  
        fig, ax = createPitch(120,75, unity = 'meters', linecolor = linecolor)
        fig.set_size_inches(10, 7)
        #fig.savefig('sonalysis_imag1.png', dpi=100)
        return fig, ax


    def CreatePitchOld(self):
        fig, ax = createPitchOld(linecolor ='red')
        fig.set_size_inches(10, 7)
        #fig.savefig('sonalysis_imag2.png', dpi=100)
        return fig , ax


    def CreateGoalMouth(self):
        fig, ax = createGoalMouth()
        fig.set_size_inches(10, 7)
        #fig.savefig('sonalysis_imag3.png', dpi=100) 
        return fig, ax
