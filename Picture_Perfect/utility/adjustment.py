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

    bright_mask = np.full(img_input.shape, 30)
    
    def func1(list1, list2, mode, iter):
        temp = Projection(transform(img_input, list1, list2, scale, shear), mode) # 1
        img_arr.append(temp)
        temp = Projection(img_arr[iter].img + bright_mask, img_arr[iter].title+'_bright+')
        img_arr.append(temp)
        temp = Projection(img_arr[iter].img - bright_mask, img_arr[iter].title+'_bright-')
        img_arr.append(temp)
        print(type(img_input))
        print(len(img_arr))

    # toolbar for progress tracking
    toolbar_width = len(img_arr)
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

    tr1 = threading.Thread(target=func1, args=([45,0,15], [0,10,0], 'image_vertical_ax_rot+', 0))
    tr2 = threading.Thread(target=func1, args=([45,0,15], [0,10,0], 'image_vertical_ax_rot-', 1))
    tr3 = threading.Thread(target=func1, args=([0,45,15], [10,0,0], 'image_horiz_ax_rot+', 2))
    tr4 = threading.Thread(target=func1, args=([0,45,15], [10,0,0], 'image_vertical_ax_rot-', 3))
    tr5 = threading.Thread(target=func1, args=(trans, [0,0,15], 'image_rotate+', 4))
    tr6 = threading.Thread(target=func1, args=(trans, [0,0,15], 'image_rotate-', 5))
    tr7 = threading.Thread(target=func1, args=([0,0,-25], rot, 'image_zoom+', 6))
    tr8 = threading.Thread(target=func1, args=([0,0,-25], rot, 'image_zoom-', 7))

    tr1.start()
    tr2.start()
    tr3.start()
    tr4.start()
    tr5.start()
    tr6.start()
    tr7.start()
    tr8.start()

    tr1.join()
    tr2.join()
    tr3.join()
    tr4.join()
    tr5.join()
    tr6.join()
    tr7.join()
    tr8.join()

    sys.stdout.write("]\n") # this ends the progress bar

    # fig.add_subplot(rows, columns, count)
    img_arr.sort(key=lambda x: x.score, reverse=True)

    print('='*70)
    print('For optimization, you need to :', img_arr[0].title)
    print('Optimization: ', img_arr[0].score/brisque.score(img_input))
    return img_arr[0].title, img_arr[0].score/brisque.score(img_input)
