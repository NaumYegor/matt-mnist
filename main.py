import mnist
import test
import train
import time

K = 997
mndata = mnist.MNIST('./images')
train_images, train_labels = mndata.load_training()
test_images, test_labels = mndata.load_testing()
results = []
start_time = time.time()
results = train.train(train_images, train_labels, results)
results = sorted(results, key=lambda image: image[0])  # Sorts by value

print("Accuracy: " + str(test.test(test_images, test_labels, results, K)))
print("Time: " + str(time.time()-start_time))


