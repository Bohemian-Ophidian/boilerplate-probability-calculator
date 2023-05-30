import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**orbs):
        self.keys=list(orbs.keys())
        self.values=list(orbs.values())
        self.contents=[]
        for key, value in orbs.items():
            self.key=value
            self.contents.extend([key]*value)
        self.duplicate = copy.deepcopy(self.contents)
        
    def draw(self, draw_num):
        drawn = []
        index =0

        for i in range(draw_num):
            if len(self.contents)==0:
                self.contents = copy.deepcopy(self.duplicate)
            index = random.randint(1,len(self.contents))
            drawn.append(self.contents.pop(index-1)) 
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    desired = 0
    for i in range(num_experiments):
        hat.contents = copy.deepcopy(hat.duplicate)
        drawn = hat.draw(num_balls_drawn)
        if matching(drawn, expected_balls):
            desired+=1
    return (desired/num_experiments)

def matching(drawn, expected):
    for key, val in expected.items():
        if drawn.count(key)>=val:
            continue
        else:
            return False
    return True
    