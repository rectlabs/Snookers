
import numpy as np 
import matplotlib
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
        positions = [(80,35), (84,33), (84,37), (88, 31), (88, 35), (88, 39), (92, 29), (92, 33), (92, 37), (92, 41), (96, 27), (96, 31), (96, 35), (96, 39), (96, 43)]
        for (x,y) in positions:
            passCircle = ann.CreateIdentity(x, y, str(np.random.choice([i for i in range(10)])/10), diameter = diameter)
            PCircle.append(passCircle)

        # insert the trigger ball (white)
        whiteballPos = (34, np.random.choice([i for i in range(10, 60)]))
        circle1 = matplotlib.patches.Circle(whiteballPos, 2, color='white')
        PCircle.append(circle1)
        return PCircle


    def CreateMinimap(self, court_type = "snookers"):
        soc = SoccerModule(x = 120,y = 70, unity = 'meters', linecolor = 'y', court_type = court_type)
        fig, ax = soc.CreatePitch()
        fig.set_facecolor('green')
        title = "{}: {} , {}:{}".format(self.TeamA, self.ScoreA, self.TeamB, self.ScoreB)
        ax.set_title(title, fontsize = 20)
        PCircles = self.start()
        for balls in PCircles:
            ax.add_patch(balls) 
        fig.set_size_inches(12, 7)
        return fig

