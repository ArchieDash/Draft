import numpy as np


def create_matrix(height, width, high):
    """Generate a matrix with given height, width and maximum element value.""" 
    data = [np.random.randint(low=1, high=high, size=width) for n in range(height)]
    matrix = np.concatenate(data).reshape(height, width)
    return matrix


if __name__ == "__main__":
    width = int(input("Set the width of the matrix: "))
    height = int(input("Set the height of the matrix: "))
    high = input("Set the limit for each element (10 by default): ")
    try:
        high = int(high)
    except ValueError:
        high = 10
    print(create_matrix(height, width, high))
    
    # Powered by Archie Dash.
