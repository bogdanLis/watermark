from PIL import Image
import os

def watermark_with_transparency(input_image_path,
                                output_image_path,
                                watermark_image_path):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    base_image = base_image.resize((400,400), Image.ANTIALIAS)

    width, height = base_image.size
 
    transparent = Image.new('RGBA', (width, height), (0,0,0,0))
    try:
        transparent.paste(base_image, (0,0), mask=base_image)
    except:
        transparent.paste(base_image, (0,0))

    pixdata = transparent.load()
    for y in range(transparent.size[1]):
        for x in range(transparent.size[0]):
            if pixdata[x, y][0] <= 10 and pixdata[x, y][1] <= 10 and pixdata[x, y][2] <= 10:
                pixdata[x, y] = (0, 0, 0, 0)

    transparent.paste(watermark, (int((width/2)-100),int((height/2)-100)), mask=watermark)
    alpha = Image.new('L', transparent.size, 255)
    transparent.putalpha(alpha)
    transparent = transparent.convert('RGB')
    transparent.save(output_image_path,'png')
 
 
if __name__ == '__main__':

    wm = 'watermark.png'
    for file in os.listdir("./from"):
        try:
            watermark_with_transparency("./from/{}".format(file), './to/{}'.format(file), wm)
            print("вотермарка добавлена на {}".format(file))
        except IOError:
            print("не изображение")
