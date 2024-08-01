from PIL import Image
import numpy as np


frames = 4
framesArray = []
with Image.open("C:\\Users\\usuario\\Documents\\DEV\\TowerDefenceRemaster\\midia\\imagens\\botao\\bandeira\\spriteSheet.png") as im:
        pxImages = []
        imArray = np.array(im.getdata()).reshape(im.size[0], im.size[1], -1)
        widthFrames = [(0, round(im.size[0] / 2)),(round(im.size[0] / 2),round(im.size[0]))]
        heightFrames = [(round(im.size[1] / (frames/2) * x ), round(im.size[1] / (frames/2) * (x+1))) for x in range(0, round(frames/2))]

        for height in heightFrames:
            for width in widthFrames:
                pxImages.append((width,height))

        for px in pxImages: 
            spriteFrame = imArray[px[0][0]:px[0][1]][px[1][0]:px[1][1]]
            spriteFrame =  Image.fromarray(np.uint8(spriteFrame)).convert('RGB')
            framesArray.append(spriteFrame)

        for i,frame in enumerate(framesArray):
            print('\n\n\n\n________________________',frame)