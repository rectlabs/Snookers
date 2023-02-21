import numpy as np 
from copy import deepcopy
class network:

    def __init__(self):
        self.count = 0
        self.updateScore = False
        self.TeamAScore = 0
        self.TeamBScore = 0
        self.game_status = ''
        self.superDict = {}
        x, y = 0, 0
        return

    def StraightLineDistance(self, x1, x2, y1, y2):
        # returns the straight line distance between coordinate (x1, y1) and coordinate (x2, y2)
        x = pow(np.abs(x1 - x2), 2)
        y = pow(np.abs(y1 - y2), 2)

        distance = np.sqrt(x+y)

        try:
            distance= int(distance)
        except:
            distance = 0

        return distance

    def setplayersLocation(self, coordinates, defaultPlayer='ball'):
        """
        x and y are lists of 50 different positions for the specific 'player'
        updates a new location for the player passed in as defaultPlayer
        """
        x = coordinates[0]
        y = coordinates[1]

        if defaultPlayer in self.superDict.keys():
            self.superDict[defaultPlayer].positionx = x
            self.superDict[defaultPlayer].positiony = y
        else:
            pass
        return

    def move(self, x1, y1, x2, y2):
        slope = (y2 - y1)/(x2 - x1)
        c = y2 - slope *x2
        xnext = (x1 + x2)/2
        ynext = slope * xnext + c
        return xnext, ynext



    def GetplayersLocation(self, defaultPlayer='ball'):
        """
        updates a new location for the player passed in as defaultPlayer
        """
        x = self.superDict[defaultPlayer].positionx
        y = self.superDict[defaultPlayer].positiony

        return x, y



class Regression:
    def __init__(self):
        return

    def network(self, xsource, ysource, Xnew, Ynew, divisor=50):
        slope = 0
        intercept = 0

        #Slope and intercept
        while True:

            try:
                slope = (ysource - Ynew)/(xsource - Xnew)
                intercept = ysource - (slope*xsource)
            except ZeroDivisionError:
                slope = 0
                pass

            if (slope != np.inf) and (intercept != np.inf):
                break
            else:
                slope = 0
                break

        # randomly select 50 new values along the slope between xsource and xnew (monotonically decreasing/increasing)
        XNewList = [xsource]
        if slope != 0 and slope != np.nan and intercept != 0 and intercept != np.nan:
            if xsource < Xnew:
                differences = Xnew - xsource
                increment = differences / divisor
                newXval = xsource
                for i in range(divisor):

                    newXval += increment
                    XNewList.append(int(newXval))
            else:
                differences = xsource - Xnew
                decrement = differences / divisor
                newXval = xsource
                for i in range(divisor-1):

                    newXval -= decrement
                    XNewList.append(int(newXval))

            # determine the values of y, from the new values of x, using y= mx + c
            yNewList = []
            for i in XNewList:
                findy = (slope * i) + intercept  # y = mx + c
                yNewList.append(int(findy))

        else:
            XNewList = [xsource]*50
            yNewList = [ysource]*50
        return XNewList[:50], yNewList[:50]



