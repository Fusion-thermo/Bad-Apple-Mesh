# Import modules:
import gmsh
import sys
 
# Initialize gmsh:
gmsh.initialize()
 
# square points:
lc = 1e-2 #si mis en 4è argument définit la densité de la grille
point1 = gmsh.model.geo.add_point(0.1, 0.1, 0)
point2 = gmsh.model.geo.add_point(0.5, 0.1, 0)
point3 = gmsh.model.geo.add_point(0.5, 0.3, 0)
point4 = gmsh.model.geo.add_point(0.1, 0.3, 0)
 
# Edge of square:
line1 = gmsh.model.geo.add_line(point1, point2)
line2 = gmsh.model.geo.add_line(point2, point3)
line3 = gmsh.model.geo.add_line(point3, point4)
line4 = gmsh.model.geo.add_line(point4, point1)
 
# face of square:
face1 = gmsh.model.geo.add_curve_loop([line1, line2, line3, line4])
 
# surfaces of square:
gmsh.model.geo.add_plane_surface([face1])
 
# Create the relevant Gmsh data structures
# from Gmsh model.
gmsh.model.geo.synchronize()
 
# Generate mesh:
gmsh.model.mesh.generate()
 
# Write mesh data:
gmsh.write("GFG.msh")
gmsh.write("GFG.stl")
 
# # Creates  graphical user interface
# if 'close' not in sys.argv:
#     gmsh.fltk.run()
 
# # It finalize the Gmsh API
# gmsh.finalize()