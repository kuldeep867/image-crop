import cv2
import numpy as np
black=np.zeros((1000 , 1000))
cv2.imshow("ab" , black)
cv2.waitKey()
cv2.destroyAllWindows()

r=black[400:600 , 400:600]
cv2.imshow("ab" , r)
cv2.waitKey()
cv2.destroyAllWindows()
white=np.ones((1000 , 1000))

cv2.imshow("ab" , white)
cv2.waitKey()
cv2.destroyAllWindows()

s=white[400:600 , 400:600]
cv2.imshow("ab" , s)
cv2.waitKey()
cv2.destroyAllWindows()

black=np.zeros((1000 , 1000))
black[400:600 , 400:600]=s
cv2.imshow("ab" , black)
cv2.waitKey()
cv2.destroyAllWindows()

white=np.ones((1000 , 1000))
white[400:600 , 400:600]=r
cv2.imshow("ab" , white)
cv2.waitKey()
cv2.destroyAllWindows()
