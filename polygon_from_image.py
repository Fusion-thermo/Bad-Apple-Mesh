import cv2

def polygon(filename):
   # read the input image
   img = cv2.imread(filename)
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
   big_contours=[]
   for cnt in contours:
      #print(0.005*cv2.arcLength(cnt, True))
      approx = cv2.approxPolyDP(cnt, 20, True)#avec une précision de 1 on passe de 1800 à 151 points du contour.

      if len(approx) >10:
         img = cv2.drawContours(img, [approx], -1, (0,255,255), 3)
         print("nombre de points",len(approx))
         big_contours.append(approx)
   cv2.imshow("Polygon", img)
   cv2.waitKey(0)
   cv2.destroyAllWindows()

   return big_contours


if __name__ == '__main__':
   #result=polygon('C:/Users/jeanb/OneDrive/Documents/Python/Bad-Apple-Mesh/pomme.png')
   #result=polygon('C:/Users/jeanb/OneDrive/Documents/Python/Bad-Apple-Mesh/silhouette.png')
   result=polygon('C:/Users/jeanb/OneDrive/Documents/Python/Bad-Apple-Mesh/chateau.png')
   # for i in result:
   #    for j in i:
   #       print(j[0],j[0][0],j[0][1],type(j[0][0]))