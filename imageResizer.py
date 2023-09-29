#install pillow
#import pilloe
#open up the image we want to resize using python
#print the current size of the image
#specify the size we want to change it to
#save the new size

from PIL import Image

def resize_image(size1, size2):
    image = Image.open('test.jpg')

    print(f'current size: {image.size}')

    resized_image = image.resize((size1, size2))

    resized_image.save('test-' + str(size1) + '-by-' + str(size2) + '.jpg')
size1 = int(input('Enter Width: '))
size2 = int(input('Enter Length: '))


resize_image(size1, size2)


