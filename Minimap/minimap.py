
import numpy as np 
import matplotlib.pyplot as plt 
from .soccer_module import SoccerModule, annotate

def randomColor():
    return np.random.choice([i for i in range(0,255)])

class Minimap:
    def __init__(self,TeamA = 'TeamA', TeamB = 'TeamB', ScoreA = 0, ScoreB = 0):
        self.TeamA = TeamA
        self.TeamB = TeamB
        self.ScoreA = ScoreA
        self.ScoreB = ScoreB

        return
    
    def start(self):
        PCircle = []
        diameter = 2
        positions = [(80,35), (82,34), (82,36), (84, 33), (84, 35), (84, 37), (86, 32), (86, 34), (86, 36), (86, 38), (88, 31), (88, 33), (88, 35), (88, 37), (88, 39)]
        for (x,y) in positions:
            color = (randomColor(), randomColor(), randomColor())
            passCircle = ann.CreateIdentity(x, y, color, diameter = diameter)
            PCircle.append(passCircle)
        return PCircle


    def CreateMinimap(self, court_type = "snookers"):
        soc = SoccerModule(x = 120,y = 70, unity = 'meters', linecolor = 'r', court_type = court_type)
        fig, ax = soc.CreatePitch()
        fig.set_facecolor('black')
        title = "{}: {} , {}:{}".format(self.TeamA, self.ScoreA, self.TeamB, self.ScoreB)
        ax.set_title(title, fontsize = 20)
        #ann = annotate()
        PCircles = self.start()
        for balls in PCircles:
            ax.add_patch(balls) 
        fig.set_size_inches(12, 7)
        return fig

