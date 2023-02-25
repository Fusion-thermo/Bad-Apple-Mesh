from mesh_from_polygon import meshing
from polygon_from_image import polygon
from picture_from_stl import picture
import glob


black = ['#000000']
white = ['#FFFFFF']

path='C:/Users/jeanb/OneDrive/Documents/Python/Bad-Apple-circles/Bad Apple frames/'
all_images=glob.glob(path+'*')

test_frames=["1","300","500","1246","4798","6238","418","2171"]
#test_frames=["6238"]

for testname in test_frames:
    filename=path+testname+".png"
    #filename="Bad Apple frames/"+str(frame)+".png"

    contours,fond=polygon(filename)
    texte=meshing(contours)
    picture(texte,fond,testname)
