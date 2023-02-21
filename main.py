import numpy as np 
import matplotlib.pyplot as plt 
from Minimap.minimap import *

PlayersAInfo = {
    'cb_right': {'Name': 'Jordan Thompson', 'Color': 'red', 'Location': (20,25)},
    'rb': {'Name': 'Haleigh Washington', 'Color': 'red', 'Location': (20,10)},
    'mf_left': {'Name': 'Andrea Drews', 'Color': 'red', 'Location': (35,53)},
    'mf_center': {'Name': 'Chiaka Ogbogu', 'Color': 'red', 'Location': (35,35)},
    'mf_right': {'Name': 'Kelsey Robinson', 'Color': 'red', 'Location': (35,17)},
    'cb_left': {'Name': 'Lauren Carlini', 'Color': 'red', 'Location': (20,45)}
}

PlayersBInfo = {
    'cb_right': {'Name': 'Jordyn Poulter', 'Color': 'blue', 'Location': (100,45)},
    'rb': {'Name': 'Justine Wong', 'Color': 'blue', 'Location': (100,60)},
    'mf_left': {'Name': 'Foluke Akinradewo', 'Color': 'blue', 'Location': (85,17)},
    'mf_center': {'Name': 'Dana Rettke', 'Color': 'blue', 'Location': (85,35)},
    'mf_right': {'Name': 'Micha Hancock', 'Color': 'blue', 'Location': (85,53)},
    'cb_left': {'Name': 'Anna Hall', 'Color': 'blue', 'Location': (100,25)}
}

ballInfo = {'ball': {'Name': 'ball', 'Color': 'green', 'Location': (90,35)}
}

if __name__ == "__main__":
    mini = Minimap(TeamA = "BotA", TeamB = "BotB")
    mini.PlayersAInfo, mini.PlayersBInfo, mini.ballInfo = PlayersAInfo, PlayersBInfo, ballInfo
    fig = mini.CreateMinimap()
    fig.savefig('image/snookers.png', dpi=100) 
    plt.show()