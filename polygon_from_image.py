import cv2
from PIL import Image
import numpy as np

def polygon(filename):
   # read the input image
   img = cv2.imread(filename)
   #coins=[0,719,959]

   # convert the image to grayscale
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   #cv2.imshow("gray", gray)
   #edged = cv2.Canny(gray, 170, 255)   
   #cv2.imshow("edged", edged)
   """
   Les contours à détecter doivent être en blanc.
   S'il y a plus de blanc que de noir alors le blanc est l'arrière plan
   Donc il faut inverser les couleurs
   """
   filling=np.count_nonzero(gray == 255)
   filling_percentage=round(100*filling/691200)
   if filling_percentage>50:
      # apply thresholding to convert the grayscale image to a binary image
      ret,thresh = cv2.threshold(gray,50,255,cv2.THRESH_BINARY_INV)
      bg="white"
   else:
      ret,thresh = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)
      bg="black"

   # find the contours
   contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
   #cv2.drawContours(img, contours, -1, (0,255,255), 3)
   #print("Number of contours detected:",len(contours))
   big_contours=[]
   for cnt in contours:
      #print(0.005*cv2.arcLength(cnt, True))
      approx = cv2.approxPolyDP(cnt, 1, True)#avec une précision de 1 on passe de 1800 à 151 points du contour.

      if len(approx) >=3:
         img = cv2.drawContours(img, [approx], -1, (0,255,255), 3)
         print("nombre de points",len(approx))
         big_contours.append(approx)
   #cv2.imshow("Polygon", img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()

   return big_contours, bg


if __name__ == '__main__':
   #result,fond=polygon('C:/Users/jeanb/OneDrive/Documents/Python/Bad-Apple-Mesh/pomme.png')
   #result,fond=polygon('C:/Users/jeanb/OneDrive/Documents/Python/Bad-Apple-Mesh/silhouette.png')
   #result,fond=polygon('C:/Users/jeanb/OneDrive/Documents/Python/Bad-Apple-Mesh/chateau.png')
   result,fond=polygon('C:/Users/jeanb/OneDrive/Documents/Python/Bad-Apple-circles/Bad Apple frames/4798.png')
