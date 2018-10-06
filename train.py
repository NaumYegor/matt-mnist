import funcs


def train(train_images, train_labels, results):
    for i in range(len(train_images)):
        label = train_labels[i]
        img_value = funcs.image_value(train_images[i])
        results.append((img_value, label))
    return results
