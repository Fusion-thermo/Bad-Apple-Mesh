# import required libraries
import cv2

# read the input image
img = cv2.imread('C:/Users/jeanb/OneDrive/Documents/Python/Bad Apple meshing/pomme.png')
#img = cv2.imread('C:/Users/jeanb/OneDrive/Documents/Python/Bad Apple meshing/silhouette.png')
#img = cv2.imread('C:/Users/jeanb/OneDrive/Documents/Python/Bad Apple meshing/chateau.png')
maxpoints=[0,719,959]

# convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("gray", gray)
edged = cv2.Canny(gray, 170, 255)   
#cv2.imshow("edged", edged)

# apply thresholding to convert the grayscale image to a binary image
ret,thresh = cv2.threshold(gray,50,255,0)

# find the contours
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img, contours, -1, (0,255,255), 3)
print("Number of contours detected:",len(contours))
for cnt in contours:
   #print(0.005*cv2.arcLength(cnt, True))
   approx = cv2.approxPolyDP(cnt, 1, True)
   (x,y)=cnt[0,0]
   print("nombre de points",len(approx))#avec une précision de 1 on passe de 1800 à 151 points du contour.

   if len(approx) >= 5:
      img = cv2.drawContours(img, [approx], -1, (0,255,255), 3)
cv2.imshow("Polygon", img)
cv2.waitKey(0)
cv2.destroyAllWindows()