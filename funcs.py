import numpy as np


def image_value(image):
    value = 1
    for i in range(len(image)):
        if image[i]:
            value += 1
    return value


def binary_search_closest(num, array):
    left_line = 0
    right_line = len(array)-1
    if num < array[left_line][0]:
        return left_line
    if num > array[right_line][0]:
        return right_line
    while True:
        middle = int((left_line + right_line) / 2)
        if num > array[middle][0] and num > array[middle+1][0]:
            left_line = middle+1
            continue
        if num < array[middle][0] and num < array[middle-1][0]:
            right_line = middle-1
            continue
        return middle


def index_of_max(array):
    maximum = -10**6
    index = 0
    for i in range(len(array)):
        if array[i] > maximum:
            maximum = array[i]
            index = i
    return index


def knn(k, array, index):
    neighbours = np.zeros(10)
    if index-int(k/2) >= 0:
        left_range = int(k/2)+1
    else:
        left_range = index+1
    if index+k-int(k/2) < len(array):
        right_range = k-int(k/2)+1
    else:
        right_range = len(array)-index-1
    for i in range(index, index-left_range, -1):
        neighbours[array[i][1]] += 1
    for i in range(index+1, index+right_range):
        neighbours[array[i][1]] += 1
    return index_of_max(neighbours)
