import time
import cv2
import matplotlib.pyplot as plt
import cvlib
from cvlib.object_detection import draw_bbox


images = []
for i in range (3):
    photo = input()
    img = cv2.imread(str(photo))
    images.append(photo)

for image in images:
    startTime = time.time()
    img = cv2.imread(image)
    box, label, count = cvlib.detect_common_objects(img)
    output = draw_bbox(img,box, label,count)
    output = cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
    plt.figure(figsize = (10,10))
    plt.axis("off")
    plt.imshow(output)
    plt.show()
    stopTime = time.time()
    duration = stopTime - startTime
    print("Na zdjęciu jest " + str(len(label)) + " ludzi. Analiza trwała " + str(duration) + " sekund")
