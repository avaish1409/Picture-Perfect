import imquality.brisque as brisque
import matplotlib.pyplot as plt

class Projection:
    def __init__(self, img_arr, title='r+', desc='Rotate +45 for optimisation'):
        self.img = img_arr
        self.title = title
        self.desc = desc
        self.score = brisque.score(self.img)
        
    def display(self):
        plt.imshow(self.img)
        plt.axis('off')
        plt.title(self.title)