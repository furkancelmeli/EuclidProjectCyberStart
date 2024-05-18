import math

points = [(2, 3), (7, 9), (8, 15), (4, 9)]


def euclideanDistance(point1, point2):
    """

    :param point1:
    :param point2:
    :return:
    """
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


distances = []
n = len(points)

for i in range(n):
    for j in range(i + 1, n):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)
min_distance = min(distances)
print("Minimum mesafe:", min_distance)
