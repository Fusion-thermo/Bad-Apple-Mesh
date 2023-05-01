from PIL import Image, ImageDraw
from mesh_from_polygon import meshing_main
from polygon_from_image import polygon
import os

path=os.path.realpath(__file__)
fin=path.rfind('\\')
chemin=path[:fin+1]
fin=chemin[:-1].rfind('\\')
chemin_frames=path[:fin+1]


def picture(texte, fond, contours, numero="test"):
    lignes=texte.split('\n')

    #gets the coordinates of each point of each triangle
    triangles=[]
    triangle=[]
    for ligne in lignes:
        if "vertex" in ligne:
            vertex=ligne.split(" ")
            coos=(float(vertex[5]),float(vertex[6]))
            triangle.append(coos)
            if len(triangle)==3:
                triangles.append(triangle[:])
                triangle=[]

    picture=Image.new("RGB",(1920,1440),fond)
    dessin = ImageDraw.Draw(picture)

    if fond=="white":
        couleur="black"
    else:
        couleur="white"
    epaisseur=3
    #draws the triangles
    for triangle in triangles:
        dessin.line((triangle[0][0]*2,triangle[0][1]*2,triangle[1][0]*2,triangle[1][1]*2),fill=couleur,width=epaisseur)
        dessin.line((triangle[0][0]*2,triangle[0][1]*2,triangle[2][0]*2,triangle[2][1]*2),fill=couleur,width=epaisseur)
        dessin.line((triangle[1][0]*2,triangle[1][1]*2,triangle[2][0]*2,triangle[2][1]*2),fill=couleur,width=epaisseur)

    #draws the contours
    for contour in contours:
        for i in range(1,len(contour)):
            dessin.line((contour[i-1][0][0]*2, contour[i-1][0][1]*2,contour[i][0][0]*2, contour[i][0][1]*2),fill=couleur,width=epaisseur)
        dessin.line((contour[-1][0][0]*2, contour[-1][0][1]*2,contour[0][0][0]*2,contour[0][0][1]*2),fill=couleur,width=epaisseur)
	

    #picture.show()
    #picture.save(chemin+"Meshed frames test/"+numero+".png")
    picture.save(chemin+"Meshed frames/"+numero+".png")
    #picture.save(chemin+"Meshed frames 2/"+numero+".png")



if __name__ == '__main__':
    #contours,fond=polygon(chemin+'pomme.png')
    #contours,fond=polygon(chemin+'silhouette.png')
    #contours,fond=polygon(chemin+'chateau.png')
    contours,fond=polygon(chemin_frames+'Bad-Apple-circles/Bad Apple frames/65.png')
    texte=meshing_main(contours)
    picture(texte,fond,contours)