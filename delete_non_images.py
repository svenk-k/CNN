import os
from PIL import Image

path = 'Images/Person/'
images = os.listdir(path)
deleted_images = 0

for image_name in images:
    file = path + image_name
    size = os.path.getsize(file)

    if size == 2051:
        os.remove(file)
        deleted_images = deleted_images + 1

    try:
        img = Image.open(file)  # open the image file
        img.verify()
    except Exception as e:
        if os.path.exists(file):
            os.remove(file)
            deleted_images = deleted_images + 1

print(f'{deleted_images} images were deleted.')
