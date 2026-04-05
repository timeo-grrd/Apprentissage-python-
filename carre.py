import sys
import math
import matplotlib.pyplot as plt

DRAW_NSTEPS = 10240

# Canvas de pixel sur lequel vous pouvez dessiner
class Paint:
    def __init__(self, width=1000, height=1000):
        self.canvas = []
        for line in range(height):
            line_data = list()
            for col in range(width):
                line_data.append([255, 255, 255])
            self.canvas.append(line_data)

    # Modifie la valeur d'un pixel sur le canvas
    def set_pixel(self, x, y, r=0, g=0, b=0):
        if x < 0 or y < 0:
            return
        if y >= len(self.canvas):
            return
        if x >= len(self.canvas[y]):
            return

        self.canvas[y][x] = [r, g, b]

    # Affiche le résultat du canvas dans une fenêtre
    def show(self):
        plt.gca().invert_yaxis()
        plt.imshow(self.canvas)
        plt.show()
        sys.exit(0)

# Point sur le canvas
class Point:

    # Définit par ses coordonnées carthésiennes
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Calcule la distance avec un autre point
    def dist(self, autre):
        s =  (autre.x - self.x) ** 2
        s += (autre.y  - self.y) ** 2
        return math.sqrt(s)

# Classe représentant une ligne entre 2 points
class Ligne:
    # Chaque paramètre est un objet de la classe Point
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Longueur de cette ligne
    def get_length(self):
        return self.a.dist(self.b)

    # Dessiner l'objet sur le canvas de pixel
    # Méthode prenant en paramètre le canvas de pixels à afficher
    def draw(self, paint):
        dx = (self.b.x - self.a.x) / DRAW_NSTEPS
        dy = (self.b.y - self.a.y) / DRAW_NSTEPS

        x = float(self.a.x)
        y = float(self.a.y)
        for step in range(DRAW_NSTEPS):
            paint.set_pixel(int(round(x, 0)), int(round(y, 0)))
            x += dx
            y += dy

paint = Paint()

#### Début du sujet
### Définition de classes ici

class Polygone:
    def __init__(self, a, b, c, d):
        self.ligne_a_b= Ligne(a, b)
        self.ligne_b_c= Ligne(b, c)
        self.ligne_c_d= Ligne(c, d)
        self.ligne_d_a= Ligne(d, a)
    def draw(self, paint):
        self.ligne_a_b.draw(paint)
        self.ligne_b_c.draw(paint)
        self.ligne_c_d.draw(paint)
        self.ligne_d_a.draw(paint)

# r=Polygone(Point(50, 300),Point(100, 50),Point(200, 150),Point(150, 250))
# r.draw(paint)

class Parallelogramme(Polygone):
    def __init__(self, a, b, c):
        self.d_x= c.x+(a.x-b.x)
        self.d_y= c.y+(a.y-b.y)
        self.pointD=Point(self.d_x,self.d_y)
        self.a,self.b,self.c = a,b,c
        Polygone.__init__(self, self.a, self.b, self.c, self.pointD)

# r=Parallelogramme(Point(50,300), Point(100, 50), Point(200, 50))
# r.draw(paint)

class Rectangle(Parallelogramme):
    def __init__(self, a, b, bc):
        self.c_x= b.x + bc *((a.y-b.y)/a.dist(b))
        self.c_y= b.y - bc *((a.x-b.x)/a.dist(b))
        self.pointC=Point(self.c_x,self.c_y)
        Parallelogramme.__init__(self, a, b, self.pointC)       
# r=Rectangle(Point(50,350),Point(80,25),800)
# r.draw(paint)

class Carre(Rectangle):
    def __init__(self, a, b):
        self.bc= a.dist(b)
        Rectangle.__init__(self, a, b, self.bc)
        
r=Carre(Point(50,350),Point(80,25))
r.draw(paint)

        
### Instanciation d'objets géométriques ici
###
paint.show()
