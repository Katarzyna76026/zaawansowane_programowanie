import cv2
import matplotlib.pyplot as plt
import cvlib
from cvlib.object_detection import draw_bbox

img1 = cv2.imread('C:/Users/Huawei/PycharmProjects/LiczenieLudzi/ZaawansowaneProgramowanie/img.png')
img2 = cv2.imread('C:/Users/Huawei/PycharmProjects/LiczenieLudzi/ZaawansowaneProgramowanie/img2.png')
img3 = cv2.imread('C:/Users/Huawei/PycharmProjects/LiczenieLudzi/ZaawansowaneProgramowanie/img3.png')

img1_cvtClolor = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2_cvtClolor = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
img3_cvtClolor = cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)


box, label, count = cvlib.detect_common_objects(img1)
output = draw_bbox(img1,box, label,count)
output = cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
plt.figure(figsize = (10,10))
plt.axis("off")
plt.imshow(output)
plt.show()

print("Na zdjęciu jest " + str(len(label)) + " ludzi")

box, label, count = cvlib.detect_common_objects(img2)
output = draw_bbox(img2,box, label,count)
output = cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
plt.figure(figsize = (10,10))
plt.axis("off")
plt.imshow(output)
plt.show()

print("Na zdjęciu jest " + str(len(label)) + " ludzi")

box, label, count = cvlib.detect_common_objects(img3)
output = draw_bbox(img3,box, label,count)
output = cv2.cvtColor(output,cv2.COLOR_BGR2RGB)
plt.figure(figsize = (10,10))
plt.axis("off")
plt.imshow(output)
plt.show()

print("Na zdjęciu jest " + str(len(label)) + " ludzi")
