import scipy.io
import PIL

mat = scipy.io.loadmat('/home/pi/Downloads/test_32x32.mat')

for i in range(1000):
    img = PIL.Image.new('RGB',(32,32))
    img.putdata([tuple(pixel) for row in mat['X'][:,:,:,i] for pixel in row])
    img.save('imgs/svhn_%d.png' %i)
    if (i%100==0):
        print 'Finished',i,' out of requested 1000'

