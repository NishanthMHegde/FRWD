import numpy as np
import cv2
import os
sample=0
path="user3train"
imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
for image in imagePaths:
    img = cv2.imread(image)
    cv2.imwrite("user3tdata/user.3." + str(sample) + ".jpg",img)
    sample = sample +1
