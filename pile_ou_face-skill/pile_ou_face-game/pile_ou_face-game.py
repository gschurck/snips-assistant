import random
class Pile_ou_face():
    def __init__(self,locale=None):
        pass
    def random_pile_ou_face(self):
        x = random.randint(1, 2)
        if x == 1:
            return "Face !"
        elif x ==2:
            return "Pile !"

if  __name__ == "__main__":
    heysnips = pile_ou_face()
    #heysnips.random_pile_ou_face()
    #print heysnips.random_pile_ou_face()
