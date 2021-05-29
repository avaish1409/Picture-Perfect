from utility.transform import *
from utility.projection import *
import sys

def cam_adjustment(path):
    fig = plt.figure(figsize=(20, 20))
    rows = 11
    columns = 3
    
    img_input = plt.imread(path)
    
    print('processing: ', path)
    
    img_arr = []
    img_arr.append(Projection(img_input, 'original'))
    """img_arr.append(Projection(img[20:(img.shape[0]-20),20:(img.shape[1]-20)], 'zoom')) # crop 20 px
    img_arr.append(Projection(rotate(img, angle=45), 'r+'))
    img_arr.append(Projection(rotate(img, angle=-45), 'r-'))"""
    
    
    trans = [0, 0, 0]
    rot = [0, 0, 0]
    scale = [1, 1, 1]
    shear = [0, 0, 0]
    
    temp = Projection(transform(img_input, trans, rot, scale, shear), 'image_input') # 0
    img_arr.append(temp)
    
    temp = Projection(transform(img_input, [45,0,15], [0,10,0], scale, shear), 'image_vertical_ax_rot+') # 1
    img_arr.append(temp)
    
    temp = Projection(transform(img_input, [45,0,15], [0,10,0], scale, shear), 'image_vertical_ax_rot-') # 2
    img_arr.append(temp)
    
    temp = Projection(transform(img_input, [0,45,15], [10,0,0], scale, shear), 'image_horiz_ax_rot+') # 3
    img_arr.append(temp)
    
    temp = Projection(transform(img_input, [0,45,15], [10,0,0], scale, shear), 'image_horiz_ax_rot-') # 4
    img_arr.append(temp)
    
    temp = Projection(transform(img_input, trans, [0,0,15], scale, shear), 'image_rotate+') # 5
    img_arr.append(temp)
    
    temp = Projection(transform(img_input, trans, [0,0,-15], scale, shear), 'image_rotate-') # 6
    img_arr.append(temp)
    
    temp = Projection(transform(img_input, [0,0,25], rot, scale, shear), 'image_zoom+') # 7
    img_arr.append(temp)
    
    temp = Projection(transform(img_input, [0,0,-25], rot, scale, shear), 'image_zoom-') # 8
    img_arr.append(temp)
    
    img_arr2 = img_arr.copy()
    bright_mask = np.full(img_input.shape, 30)
    
    # toolbar for progress tracking
    toolbar_width = len(img_arr)
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['
    for i in img_arr:
        temp = Projection(i.img + bright_mask, i.title+'_bright+')
        img_arr2.append(temp)
        temp = Projection(i.img - bright_mask, i.title+'_bright-')
        img_arr2.append(temp)
        # update the bar
        sys.stdout.write("-")
        sys.stdout.flush()

    sys.stdout.write("]\n") # this ends the progress bar

    img_arr = img_arr2
    
    # fig.add_subplot(rows, columns, count)
    img_arr.sort(key=lambda x: x.score, reverse=True)

    print('='*70)
    print('For optimization, you need to :', img_arr[0].title)
    print('Optimization: ', img_arr[0].score/brisque.score(img_input))
    return img_arr[0].title, img_arr[0].score/brisque.score(img_input)
