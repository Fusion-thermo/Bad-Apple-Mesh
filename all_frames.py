from PIL import Image
from mesh_from_polygon import meshing_main
from polygon_from_image import polygon
from picture_from_stl import picture
import glob
import os

path=os.path.realpath(__file__)
fin=-1
while path[fin]!="\\":
    fin-=1
chemin=path[:fin+1].replace('\\','/')
fin-=1
while path[fin]!="\\":
    fin-=1
chemin_frames=path[:fin+1].replace('\\','/')
path=chemin_frames+'Bad-Apple-circles/Bad Apple frames/'
meshedframes=chemin+'Meshed frames'
all_meshed=glob.glob(meshedframes+'/*')

#to start again from the last meshed
#meshedframes2=chemin+'Meshed frames 2'
#all_meshed2=glob.glob(meshedframes2+'/*')
#nombres=[int(filepath[filepath.find('\\')+1:filepath.find('.')]) for filepath in all_meshed2]
#nombres.sort()
#start=nombres[-1]+2 

test_frames=["1","300","500","1246","4798","6238","418","2171"]
#test_frames=["6238"]
start=1

# Main
#for testname in test_frames:
    #filename=path+testname+".png"
for frame in range(start,6573):
    print("frame n°",frame)
    if meshedframes+'\\'+str(frame)+".png" in all_meshed:
        continue
    filename=path+str(frame)+".png"

    contours,fond=polygon(filename)
    texte=meshing_main(contours)
    picture(texte,fond,contours,str(frame))


""" # Last missing frames (70)
for frame in range(1,6573):
    if meshedframes+'\\'+str(frame)+".png" not in all_meshed:
        print("frame n°",frame)
        picture= Image.open(chemin+'Meshed frames/'+str(frame-1)+".png")
        picture.save(chemin+'Meshed frames/'+str(frame)+".png") """