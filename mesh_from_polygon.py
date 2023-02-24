import gmsh
import sys
from polygon_from_image import polygon

#contours=polygon('C:/Users/jeanb/OneDrive/Documents/Python/Bad-Apple-Mesh/pomme.png')
#contours=polygon('C:/Users/jeanb/OneDrive/Documents/Python/Bad-Apple-Mesh/silhouette.png')
contours=polygon('C:/Users/jeanb/OneDrive/Documents/Python/Bad-Apple-Mesh/chateau.png')
 
# Initialize gmsh:
gmsh.initialize()
 
lc = 1e-2 #si mis en 4è argument définit la densité de la grille

faces=[]
for contour in contours:
	lignes=[]
	#points=[]
	debut=gmsh.model.geo.add_point(contour[0][0][0], contour[0][0][1], 0)
	for i in range(1,len(contour)):
		coos=gmsh.model.geo.add_point(contour[i][0][0], contour[i][0][1], 0)
		#coos2=gmsh.model.geo.add_point(contour[i+1][0][0], contour[i+1][0][1], 0)
		ligne=gmsh.model.geo.add_line(coos-1,coos)
		lignes.append(ligne)
	#fin=gmsh.model.geo.add_point(contour[-1][0][0], contour[-1][0][1], 0)
	ligne=gmsh.model.geo.add_line(coos,debut)#segment entre le dernier et le premier élément
	lignes.append(ligne)
	print(len(lignes),lignes)

	face=gmsh.model.geo.add_curve_loop(lignes)
	faces.append(face)

gmsh.model.geo.add_plane_surface(faces)#connecte les faces qui lui sont données donc il faire chaque contour séparément
 
# Create the relevant Gmsh data structures
# from Gmsh model.
gmsh.model.geo.synchronize()
 
# Generate mesh:
gmsh.model.mesh.generate()
 
# Write mesh data:
gmsh.write("C:/Users/jeanb/OneDrive/Documents/Python/Bad-Apple-Mesh/GFG.msh")
gmsh.write("C:/Users/jeanb/OneDrive/Documents/Python/Bad-Apple-Mesh/GFG.stl")
