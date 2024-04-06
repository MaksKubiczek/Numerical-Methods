from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

class QuadTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = [None] * 4

def load_jpg_to_array(file_name):
    with Image.open(file_name) as img:
        img = img.convert('1')  # konwertujemy na obraz dwukolorowy
        width, height = img.size
        width_pow2 = int(2 ** np.ceil(np.log2(width)))
        height_pow2 = int(2 ** np.ceil(np.log2(height)))
        img = img.resize((width_pow2, height_pow2))  # Dostosowanie rozmiaru obrazu do potęgi dwójki
        pixel_array = np.array(img)
        return pixel_array, width_pow2, height_pow2

def quadtree(pixel_array):
    def is_homogeneous(x, y, size):
        return len(set(pixel_array[y:y+size, x:x+size].flatten())) == 1

    def build_quadtree(x, y, size):
        if size == 1 or is_homogeneous(x, y, size):
            return QuadTreeNode(pixel_array[y][x])
        node = QuadTreeNode(None)
        sub_size = size // 2
        node.children[0] = build_quadtree(x, y, sub_size)
        node.children[1] = build_quadtree(x + sub_size, y, sub_size)
        node.children[2] = build_quadtree(x, y + sub_size, sub_size)
        node.children[3] = build_quadtree(x + sub_size, y + sub_size, sub_size)
        return node
    
    return build_quadtree(0, 0, len(pixel_array))


def plot_quadtree(node, ax, x, y, size):
    if node:
        if node.value is not None:
            color = 'white' if node.value == 1 else 'black'
            ax.fill([x, x+size, x+size, x], [y, y, y+size, y+size], color=color, edgecolor='black')
        else:
            sub_size = size // 2
            plot_quadtree(node.children[0], ax, x, y, sub_size)
            plot_quadtree(node.children[1], ax, x + sub_size, y, sub_size)
            plot_quadtree(node.children[2], ax, x, y + sub_size, sub_size)
            plot_quadtree(node.children[3], ax, x + sub_size, y + sub_size, sub_size)
            ax.plot([x+sub_size, x+sub_size], [y, y+size], color='black', linewidth=0.5)
            ax.plot([x, x+size], [y+sub_size, y+sub_size], color='black', linewidth=0.5)

def main():
    file_path = 'bg.jpg'
    pixel_array, width, height = load_jpg_to_array(file_path)
    print("Szerokosc:", width)
    print("Wysokosc:", height)
    quadtree_array = quadtree(pixel_array)
    
    fig, ax = plt.subplots(figsize=(width/100, height/100))
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    plot_quadtree(quadtree_array, ax, 0, 0, width)
    plt.axis('off')
    plt.gca().invert_yaxis()  # Odwrócenie osi Y, aby wizualizacja była poprawnie wyświetlona
    plt.savefig('quadtree_visualization.png', bbox_inches='tight', pad_inches=0)
    plt.show()

if __name__ == '__main__':
    main()