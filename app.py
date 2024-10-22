from turtle import shape
from sketchpy import canvas
import cv2
im =cv2.imread('img/ata.jpg')
print(im.shape)
object=canvas.sketch_from_image('img/ata.jpg')
object.draw(threshold=50)