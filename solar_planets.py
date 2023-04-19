import cv2
import numpy as np

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(95,100),cv2.FONT_HERSHEY_DUPLEX,2,(0,0,255))
cv2.putText(img,"Mercury",(100,300),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255))
cv2.putText(img,"Venus",(190,300),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255))
cv2.putText(img,"Earth",(290,300),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255))
cv2.putText(img,"Mars",(390,300),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255))
cv2.putText(img,"Jupiter",(575,300),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255))
cv2.putText(img,"Saturn",(770,300),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255))
cv2.putText(img,"Uranus",(970,300),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255))
cv2.putText(img,"Neptune",(1120,300),cv2.FONT_HERSHEY_DUPLEX,0.5,(255,255,255))

cv2.imshow("Output",img)

cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)