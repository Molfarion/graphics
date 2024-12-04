import matplotlib.pyplot as plt

def plot_points_from_txt(dataset_path):
    x, y = [], []
    with open(dataset_path, 'r') as file:
        for line in file:
            x_val, y_val = map(int, line.split())
            x.append(x_val)
            y.append(y_val)
    
    plt.figure(figsize=(9.6, 5.4))
    plt.scatter(x, y, c='black', alpha=0.7)
    plt.title("Точки на координатній площині")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()

dataset_path = "DS1.txt"
plot_points_from_txt(dataset_path)

