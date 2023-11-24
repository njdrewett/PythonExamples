#! python3

# Draw Text for Images

from PIL import Image, ImageDraw, ImageFont
import os


image = Image.new('RGBA', (200,200),'white')

draw = ImageDraw.Draw(image)

draw.text((20,150), 'Hello', fill ='purple')

fontsFolder = 'C:\Windows\Fonts'

arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)

draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)

image.save('text.png')
print("Done")


