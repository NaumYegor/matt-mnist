import funcs
import numpy as np


def test(test_images, test_labels,
         results, k):
    success = 0
    for i in range(len(test_images)):
        img_value = funcs.image_value(test_images[i])
        real_label = test_labels[i]
        closest_index = funcs.binary_search_closest(img_value, results)
        prediction = funcs.knn(k, results, closest_index)
        if real_label == prediction:
            success += 1
        print(real_label, prediction, closest_index)
    print(results)
    return 100*success/len(test_images)