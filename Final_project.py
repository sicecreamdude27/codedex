import imageio.v3 as iio
filenames = ['1.png','2.png', '3.png', '4.png']
images= []
for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('luffy.gif', images, duration = 500, loop =0)