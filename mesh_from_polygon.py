import gmsh
import sys
from polygon_from_image import polygon
import os

path=os.path.realpath(__file__)
fin=-1
while path[fin]!="\\":
    fin-=1
chemin=path[:fin+1].replace('\\','/')

def meshing(contour):
	# Initialize gmsh:
	gmsh.initialize()
	
	faces=[]
	lignes=[]
	debut=gmsh.model.geo.add_point(contour[0][0][0], contour[0][0][1], 0)
	for i in range(1,len(contour)):
		coos=gmsh.model.geo.add_point(contour[i][0][0], contour[i][0][1], 0)
		ligne=gmsh.model.geo.add_line(coos-1,coos)
		lignes.append(ligne)
	ligne=gmsh.model.geo.add_line(coos,debut)#line between first and last element
	lignes.append(ligne)
	#print(len(lignes),lignes)

	face=gmsh.model.geo.add_curve_loop(lignes)
	faces.append(face)
	gmsh.model.geo.add_plane_surface(faces)#connect the faces that are given so here each contour must be meshed separately and not one face per contour
	
	# Create the relevant Gmsh data structures
	# from Gmsh model.
	gmsh.model.geo.synchronize()
	# Generate mesh:
	gmsh.model.mesh.generate(2)
	# Write mesh data:
	#gmsh.write(chemin+"GFG.msh")
	gmsh.write(chemin+"GFG.stl")
	gmsh.clear()
	gmsh.finalize()

def meshing_main(contours):
	texte=""
	for contour in contours:
		try:
			print("Longueur contour",len(contour))
			meshing(contour)
			with open(chemin+"GFG.stl") as stl:
				texte+=stl.read()
		except:
			print("ERREUR")
			gmsh.clear()
			gmsh.finalize()
			pass
	return texte


if __name__ == '__main__':
	#contours,fond=polygon(chemin+'pomme.png')
	#contours,fond=polygon(chemin+'silhouette.png')
	contours,fond=polygon(chemin+'chateau.png')
	texte=meshing_main(contours)