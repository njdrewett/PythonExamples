#!python3

# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

# 1. Load the logo image.
# 2. Loop over all .png and.jpg files in the working directory.
# 3. Check whether the image is wider or taller than 300 pixels.
# 4. If so, reduce the width or height (whichever is larger) to 300 pixels and
#    scale down the other dimension proportionally.
# 5. Paste the logo image into the corner.
# 6. Save the altered images to another folder.

from PIL import Image
import os

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

# 1. Load the logo image.

logoImage = Image.open(LOGO_FILENAME)
logoImage = logoImage.resize((100,200))
logoWidth, logoHeight = logoImage.size
print("logowidth = %s , logo height = %s" % (logoWidth, logoHeight))

# TODO: Loop over all files in the working directory.
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue
    image = Image.open(filename)
    width,height = image.size
    print("filename: %s image width = %s , Image height = %s" % (filename , width, height))

    # TODO: Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # TODO: Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        # TODO: Resize the image.
        print('Resizing image...')
        image = image.resize((width,height))

        # TODO: Add the logo.
        print('Adding logo to %s...' % (filename))
        image.paste(logoImage, (width - logoWidth, height - logoHeight), logoImage)

        # TODO: Save changes
        image.save(os.path.join('withlogo',filename))







