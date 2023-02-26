import cv2
from PIL import Image
import numpy as np
from Chemin import chemin

def polygon(filename):
   # read the input image
   img = cv2.imread(filename)

   # convert the image to grayscale
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   #cv2.imshow("gray", gray)
   #edged = cv2.Canny(gray, 170, 255)
   #cv2.imshow("edged", edged)
   """
   Contours must be in white to be detected
   So if there is more white than black then white is the background
   So we have to reverse the colors
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
   cv2.drawContours(img, contours, -1, (0,255,255), 3)#draws all detected contours (parameter -1)
   #print("Number of contours detected:",len(contours))
   big_contours=[]
   for cnt in contours:
      #with a precision of 1 we go from 1800 to 151 for the number of points of a contours.
      #increasing the number reduces the number of points so the meshing is less likely to fail.
      approx = cv2.approxPolyDP(cnt, 1, True)

      if len(approx) >=10:
         img = cv2.drawContours(img, [approx], -1, (0,255,255), 3)
         print("Numbers of points of the contour",len(approx))
         big_contours.append(approx)
   cv2.imshow("Polygon", img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()

   return big_contours, bg


if __name__ == '__main__':
   #result,fond=polygon(chemin+'Bad-Apple-Mesh/pomme.png')
   #result,fond=polygon(chemin+'Bad-Apple-Mesh/silhouette.png')
   #result,fond=polygon(chemin+'Bad-Apple-Mesh/chateau.png')
   result,fond=polygon(chemin+'Bad-Apple-circles/Bad Apple frames/54.png')
