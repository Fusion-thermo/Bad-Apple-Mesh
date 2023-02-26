from PIL import Image
from mesh_from_polygon import meshing_main
from polygon_from_image import polygon
from picture_from_stl import picture
import glob
from Chemin import chemin

path=chemin+'Bad-Apple-circles/Bad Apple frames/'
meshedframes=chemin+'Bad-Apple-Mesh/Meshed frames'
all_meshed=glob.glob(meshedframes+'/*')

#to start again from the last meshed
#meshedframes2=chemin+'Bad-Apple-Mesh/Meshed frames 2'
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


""" # Last missing framese (70)
for frame in range(1,6573):
    if meshedframes+'\\'+str(frame)+".png" not in all_meshed:
        print("frame n°",frame)
        picture= Image.open(chemin+'Bad-Apple-Mesh/Meshed frames/'+str(frame-1)+".png")
        picture.save(chemin+'Bad-Apple-Mesh/Meshed frames/'+str(frame)+".png") """