import glob
import os
import cv2

# function for renaming and resizing images
def rename(images, path, ext, j):
    for i in range(len(images)):
        t = 'image' + str(j) +'.' +ext #new name
        j=j+1
        image = cv2.imread(images[i])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        res = cv2.resize(image,(64, 64), interpolation = cv2.INTER_CUBIC)
        cv2.imwrite((path+'{}').format(t), cv2.cvtColor(res,cv2.COLOR_BGR2RGB))
        

extensions=['jpg', 'png', 'jpeg']
dirs=['bulbasaur','jigglypuff', 'mewto', 'pikachu', 'squirtle']
for dir in dirs:
    l=0
    for i, ext in enumerate(extensions):
        print(ext)
        images= glob.glob("/home/ibtissem/intilaq_academy/deep_learning/CNN/pokemon_project/data/pokemon_data/test/"+dir+"/*."+ext)
        if not(os.path.exists("/home/ibtissem/intilaq_academy/deep_learning/CNN/pokemon_project/data/pokemon_data/test_data/"+dir)):
            os.makedirs("/home/ibtissem/intilaq_academy/deep_learning/CNN/pokemon_project/data/pokemon_data/test_data/"+dir)
        rename(images, "/home/ibtissem/intilaq_academy/deep_learning/CNN/pokemon_project/data/pokemon_data/test_data/"+dir+"/",ext, l)
        l+=(len(images))
