import skimage
from skimage import io, transform

path_meat='FOODSET/images/test/meat'
path_chocolate='FOODSET/images/test/chocolate'
path_eggs='FOODSET/images/test/chocolate'
path_fish='FOODSET/images/test/fish'
path_fruitsveg='FOODSET/images/test/fruitsveg'
path_pastarice='FOODSET/images/test/pastarice'

#read images
collMeat = skimage.io.ImageCollection(path_meat + '/*.jpg')
collChocolate = skimage.io.ImageCollection(path_chocolate + '/*.jpg')
collEggs = skimage.io.ImageCollection(path_eggs + '/*.jpg')
collFish = skimage.io.ImageCollection(path_fish + '/*.jpg')
collFruitsVeg = skimage.io.ImageCollection(path_fruitsveg + '/*.jpg')
collPastaRice = skimage.io.ImageCollection(path_pastarice + '/*.jpg')

foodDict = {'Meat':collMeat,'Chocolate':collChocolate,'Eggs':collEggs,'Fish':collFish,'FruitsVeg':collFruitsVeg,'PastaRice':collPastaRice}

#resize to 300x300
for name,collection in foodDict.items():
    for i in range(len(collection)):
        image = skimage.transform.resize(foodDict[name][i],[300,300])
        skimage.io.imsave('assets/%s %s.jpg'%(name,str(i)),image)
