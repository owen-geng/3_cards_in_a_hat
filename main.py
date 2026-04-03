import random

class Card():
    def __init__(self, face1, face2):
        self.faces = [face1, face2]


class Hat():
    def __init__(self):
        self.contents = []
        self.contents.append(Card("red", "red"))
        self.contents.append(Card("blue", "blue"))
        self.contents.append(Card("red", "blue"))
    
    def draw(self):
        
        rand = random.randint(0,2)
        face = random.randint(0,1)

        return self.contents[rand].faces[face], self.contents[rand].faces[1-face]
    

if __name__ == "__main__":
    
    hat = Hat()

    trials = 100000

    red_count = 0
    blue_count = 0

    for i in range(trials):
        
        seen_face, unseen_face = hat.draw()

        if seen_face == "red":
            if unseen_face == "red":
                red_count += 1
            else:
                blue_count += 1
    
    print(f"Number of times the other face was red: {red_count}")
    print(f"Number of times the other face was blue: {blue_count}")
    print(f"Total number of times the seen face is red: {red_count+blue_count}")
    print(f"Probability of unseen face being red: {red_count/(red_count+blue_count)}")
