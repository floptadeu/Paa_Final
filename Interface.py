import numpy as np
import cv2
from Trapezio import Trapezio
from Leitor import Leitor, Pecas, exeEncaixar

def gerar_cor_aleatoria():
    """Gera uma cor BGR aleatória."""
    return (np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256))

def ccw(A, B, C):
    return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])

def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

# Function to check if a polygon has any intersecting lines
def has_intersecting_lines(points):
    num_points = len(points)
    for i in range(num_points):
        for j in range(i+1, num_points):
            if i != j:
                A, B = points[i], points[(i + 1) % num_points]
                C, D = points[j], points[(j + 1) % num_points]
                if intersect(A, B, C, D):
                    return True
    return False

def draw_trapezoid(trapezoid, image_size=(100, 300), color= gerar_cor_aleatoria()):

    # Create a blank black image
    image = np.zeros((image_size[0], image_size[1], 3), np.uint8)

    # Calculate the points of the trapezoid
    pts = np.array([
        [trapezoid.inferiorEsquerdo[0]+ 100, trapezoid.inferiorEsquerdo[1]],
        [trapezoid.superiorEsquerdo[0] + 100, trapezoid.superiorEsquerdo[1]],
        [trapezoid.superiorDireito[0]+ 100, trapezoid.superiorDireito[1]],
        [trapezoid.inferiorDireito[0]+ 100, trapezoid.inferiorDireito[1]]
    ], np.int32)
    # print(pts)
    if has_intersecting_lines(pts):
        print(f"Warning: Trapezoid {a} has intersecting lines and may not be drawn correctly.")
        pts = np.array([
            [trapezoid.inferiorDireito[0] + 100, trapezoid.inferiorDireito[1]],
            [trapezoid.inferiorEsquerdo[0] + 100, trapezoid.inferiorEsquerdo[1]],
            [trapezoid.superiorDireito[0] + 100, trapezoid.superiorDireito[1]],
            [trapezoid.superiorEsquerdo[0] + 100, trapezoid.superiorEsquerdo[1]],


        ], np.int32)

        # Draw the trapezoid
        cv2.polylines(image, [pts], isClosed=True, color=color, thickness=2)

        # Alternatively, fill the trapezoid
        cv2.fillPoly(image, [pts], color)

        return image
    else:
        # Reshape the points in the format required by polylines
        pts = pts.reshape((-1, 1, 2))

        # Draw the trapezoid
        cv2.polylines(image, [pts], isClosed=True, color=color, thickness=2)

        # Alternatively, fill the trapezoid
        cv2.fillPoly(image, [pts], color)

        return image

def Interface(pecas):
    pts = list()

    distanciasDeVertices = exeEncaixar(pecas)

    distanciasDeVertices.insert(0,0)
    total_width = sum(distanciasDeVertices)


    ix = 2000
    iy = 100
    image = np.zeros((iy, ix, 3), np.uint8)

    isClosed = True
    thickness = 2
    color = gerar_cor_aleatoria()
    start_point = (ix - total_width) // 2

    pontoReferencia = float(ix/3)

    for w,trapezoid in enumerate(pecas):
        color = gerar_cor_aleatoria()

        ponto = np.array([
        [trapezoid.inferiorEsquerdo[0], trapezoid.inferiorEsquerdo[1]],
        [trapezoid.superiorEsquerdo[0], trapezoid.superiorEsquerdo[1]],
        [trapezoid.superiorDireito[0], trapezoid.superiorDireito[1]],
        [trapezoid.inferiorDireito[0], trapezoid.inferiorDireito[1]]
        ], np.int32)

        pontoReferencia = pontoReferencia - distanciasDeVertices[w]

        if has_intersecting_lines(ponto):
            pts.append(
                np.array([
                    [trapezoid.inferiorDireito[0] + pontoReferencia, trapezoid.inferiorDireito[1]],
                    [trapezoid.inferiorEsquerdo[0] + pontoReferencia, trapezoid.inferiorEsquerdo[1]],
                    [trapezoid.superiorDireito[0] + pontoReferencia, trapezoid.superiorDireito[1]],
                    [trapezoid.superiorEsquerdo[0] + pontoReferencia, trapezoid.superiorEsquerdo[1]],

                ], np.int32)
            )
            cv2.fillPoly(image, [pts[w]], color)
        else:
            pts.append(
                np.array([
                [trapezoid.inferiorEsquerdo[0] + pontoReferencia, trapezoid.inferiorEsquerdo[1]],
                [trapezoid.superiorEsquerdo[0] + pontoReferencia, trapezoid.superiorEsquerdo[1]],
                [trapezoid.superiorDireito[0] + pontoReferencia, trapezoid.superiorDireito[1]],
                [trapezoid.inferiorDireito[0] + pontoReferencia, trapezoid.inferiorDireito[1]]
            ], np.int32)
            )
            cv2.fillPoly(image, [pts[w]], color)

    #cv2.fillPoly(image, pts, color)
    cv2.imshow('Black Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



# Example usage
# Assume trapezoid is an instance of the Trapezio class with correct vertex coordinates
pecas = Pecas(Leitor())
# a = 1
# for trapezoid in pecas:
#     print(a)
#     a+=1
#     color = gerar_cor_aleatoria()
#     trapezoid_image = draw_trapezoid(trapezoid,color= color)
#     cv2.imshow("Trapezoid", trapezoid_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

Interface(pecas)
