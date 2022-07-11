import cv2
import numpy as np
import glob
import os
# Часть 1. Накладывание маски на все изображения
i = 0
while i <= 69:
    if i < 10:
        name_img = 'images/0000' + str(i) + '.png'
        name_mask = 'masks/0000' + str(i) + '.png'
    else:
        name_img = 'images/000' + str(i) + '.png'
        name_mask = 'masks/000' + str(i) + '.png'
    # Считывание исходного изображения
    img = cv2.imread(name_img)
    # Считывание маски
    mask = cv2.imread(name_mask, 0)
    # Наложение маски, получение нового изображения
    res = cv2.bitwise_and(img, img, mask=mask)
    name_res = 'withmasksboth/New' + str(i) + '.png'
    # Помещаем полученное изображение в папку
    cv2.imwrite(name_res, res)
    # Увеличение счетчика
    i = i + 1
# Часть 2. Составление видео из кадров (кадры берет произвольные, не все по порядку)
image_folder = 'withmasksboth'
video_name = 'newvideoboth.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

#video_name - имя выходного видео, 1 - частота кадров (у нас 69 изображений, видео длится 1 с.), (width, height) - размер
video = cv2.VideoWriter(video_name, 0, 69, (width, height))
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))
cv2.destroyAllWindows()
video.release() # Закрытие VideoWriter