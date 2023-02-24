
import numpy as np 
import matplotlib.pyplot as plt 
from .soccer_module import SoccerModule, annotate

def randomColor():
    return np.random.choice([i for i in range(100,255)])

class Minimap:
    def __init__(self,TeamA = 'TeamA', TeamB = 'TeamB', ScoreA = 0, ScoreB = 0):
        self.TeamA = TeamA
        self.TeamB = TeamB
        self.ScoreA = ScoreA
        self.ScoreB = ScoreB

        return
    
    def start(self):
        ann = annotate()
        PCircle = []
        diameter = 2
        positions = [(80,35), (84,33), (84,37), (88, 31), (88, 33), (88, 35), (92, 29), (92, 31), (92, 33), (92, 35), (96, 27), (96, 29), (96, 31), (96, 33), (96, 35)]
        for (x,y) in positions:
            passCircle = ann.CreateIdentity(x, y, str(np.random.choice([i for i in range(30)])/30), diameter = diameter)
            PCircle.append(passCircle)
        return PCircle


    def CreateMinimap(self, court_type = "snookers"):
        soc = SoccerModule(x = 120,y = 70, unity = 'meters', linecolor = 'r', court_type = court_type)
        fig, ax = soc.CreatePitch()
        fig.set_facecolor('black')
        title = "{}: {} , {}:{}".format(self.TeamA, self.ScoreA, self.TeamB, self.ScoreB)
        ax.set_title(title, fontsize = 20)
        PCircles = self.start()
        for balls in PCircles:
            ax.add_patch(balls) 
        fig.set_size_inches(12, 7)
        return fig

