import matplotlib.pyplot as plt
import pandas as pd
import os

def get_data(img_path):
    img = plt.imread(img_path)
    #img -> 150x150 input image
    output_pixel = img[45][75][0] # last index is to be corrected
    neighbours = [
        img[50][55][0],
        img[50][65][0],
        img[50][75][0],
        img[50][85][0],
        img[50][95][0]
    ]
    cropped_img = img[50:100, 50:100]
    return neighbours, output_pixel

def get_df(dir):
    df = pd.DataFrame(columns=['input_1', 'input_2', 'input_3', 'input_4', 'input_5', 'output'])
    for i in os.listdir(dir):
        row = get_data(dir+i)
        df.loc[len(df.index)] = row[0] +[row[1]]
    return df

d = get_df('/home/anirudh/Desktop/images/')
print(d)