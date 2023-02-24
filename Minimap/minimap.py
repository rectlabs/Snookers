
import numpy as np 
import matplotlib.pyplot as plt 
from .soccer_module import SoccerModule, annotate

class Minimap:
    def __init__(self,TeamA = 'TeamA', TeamB = 'TeamB', ScoreA = 0, ScoreB = 0):
        self.TeamA = TeamA
        self.TeamB = TeamB
        self.ScoreA = ScoreA
        self.ScoreB = ScoreB

        return


    def CreateMinimap(self, court_type = "snookers"):
        soc = SoccerModule(x = 120,y = 70, unity = 'meters', linecolor = 'r', court_type = court_type)
        fig, ax = soc.CreatePitch()
        fig.set_facecolor('green')
        title = "{}: {} , {}:{}".format(self.TeamA, self.ScoreA, self.TeamB, self.ScoreB)
        ax.set_title(title, fontsize = 20)
        ann = annotate()
        fig.set_size_inches(12, 7)
        return fig

