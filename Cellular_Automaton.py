from matplotlib import pyplot as plt
from matplotlib import colors
import numpy as np

X, Y = 25, 25
NMin, NMax = 3, 4
def cell_field():
    data = np.zeros((Y, X))
    random_array = np.random.rand(Y, X)
    chance = 0.2  # шанс (n*100)%
    data[random_array < chance] = 1
    return data

def field_update(data, ny, nx):
    count_live = 0
    rows, cols = data.shape
    for y in range(-1, 2):
        for x in range(-1, 2):
            if x == 0 and y == 0:
                continue  # пропустить элемент

            ny_neighbor = ny + y
            nx_neighbor = nx + x

            if 0 <= ny_neighbor < rows and 0 <= nx_neighbor < cols:
                if data[ny_neighbor, nx_neighbor] == 1:
                    count_live += 1
                    
    if  count_live < NMin or count_live > NMax: # клетка умирает, если в области от <A или >B соседей
        data[ny, nx] = 0
    else:
        data[ny, nx] = 1

def process_array(data):
    rows, cols = data.shape
    new_data = np.copy(data) # создание копии

    for ny in range(rows):
        for nx in range(cols):
            field_update(new_data, ny, nx)
    return new_data

def field_draw(data, iterations):
    cmap = colors.ListedColormap(['white','black'])
    fig, ax = plt.subplots(figsize=(3, 3))
    img = ax.pcolor(data[::-1], cmap=cmap, edgecolors='k', linewidths=1)
    plt.show(block=False)
    iteration = 0
    while iteration != iterations:
        data = process_array(data) # функция обновления массива
        img.set_array(data[::-1].flatten())
        fig.canvas.draw_idle()
        fig.canvas.flush_events()
        plt.pause(0.1)  # обновляем график каждые 0.1 секунды
        iteration += 1
    plt.show()
        
data = cell_field()
field_draw(data, 10)