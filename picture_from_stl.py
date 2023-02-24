from PIL import Image, ImageDraw

with open("C:/Users/jeanb/OneDrive/Documents/Python/Bad-Apple-Mesh/GFG.stl") as stl:
    texte=stl.read()
lignes=texte.split('\n')

#récupère les coos de chaque point de chaque triangle
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

print(len(triangles),triangles)

picture=Image.new("RGB",(1920,1440),"black")
dessin = ImageDraw.Draw(picture)

couleur="white"
epaisseur=3
for triangle in triangles:
    dessin.line((triangle[0][0]*2,triangle[0][1]*2,triangle[1][0]*2,triangle[1][1]*2),fill=couleur,width=epaisseur)
    dessin.line((triangle[0][0]*2,triangle[0][1]*2,triangle[2][0]*2,triangle[2][1]*2),fill=couleur,width=epaisseur)
    dessin.line((triangle[1][0]*2,triangle[1][1]*2,triangle[2][0]*2,triangle[2][1]*2),fill=couleur,width=epaisseur)

picture.show()

