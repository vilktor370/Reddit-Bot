from PIL import Image
import glob
import numpy as np
import matplotlib.pyplot as plt
image_list = []
for filename in glob.glob('image/*.png'): #assuming gif
    im=Image.open(filename)
    image_list.append(im)
#print(len(image_list))
img_data=np.array(image_list[0])
#print(ary)
#print('\n\n\n\n')
img_data=img_data
#print(ary)
img_data[:1920,:1080,:]
img_data=np.flip(img_data,axis=1)
test=Image.fromarray(img_data)
test.save("test.png")
