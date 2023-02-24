import numpy as np 
from .FCPython import *
import matplotlib.pyplot as plt 


class annotate:
    def __init__(self):
        return

    def CreateIdentity(self, x, y, color, name = 'E', nameloc = 'up', diameter = 2):
        passCircle=plt.Circle((x,y),diameter,color=color)
        # if nameloc == 'up':
        #     plt.text(x,y+3,name) 
        # elif nameloc == 'down':
        #     plt.text(x,y-3, name)
        # else:
        #     plt.text(x,y, name)   
        passCircle.set_alpha(.2) 
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
