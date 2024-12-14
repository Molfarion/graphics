import numpy as np
import matplotlib.pyplot as plt

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def graham_scan(points):
    points = sorted(points, key=lambda p: (p[0], p[1])) 
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1]

x, y = [], []
dataset_path = 'DS1.txt'

with open(dataset_path, 'r') as file:
    for line in file:
        x_val, y_val = map(int, line.split())
        x.append(x_val)
        y.append(y_val)

points = np.array([x, y]).T  

hull = graham_scan(points)

hull_dataset_path = 'convex_hull.txt'
np.savetxt(hull_dataset_path, hull, fmt='%d')

plt.figure(figsize=(9.6, 5.4))
points = np.array(points)
plt.plot(points[:, 0], points[:, 1], 'go', label='Точки датасету')  

hull = np.array(hull)
plt.plot(hull[:, 0], hull[:, 1], 'b-', label='Опукла оболонка')

for i in range(len(hull)):
    plt.plot([hull[i][0], hull[(i + 1) % len(hull)][0]], 
             [hull[i][1], hull[(i + 1) % len(hull)][1]], 'b-', lw=2)

plt.title('Опукла оболонка (Алгоритм Грехема)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

output_image_path = 'convex_hull_graham.png'
plt.savefig(output_image_path)  
plt.show()
