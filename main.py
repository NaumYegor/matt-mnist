import mnist
import time
import sklearn.neighbors

mndata = mnist.MNIST('./images')
train_images, train_labels = mndata.load_training()
test_images, test_labels = mndata.load_testing()
result = sklearn.neighbors.KNeighborsClassifier(n_neighbors=3)

print("Test point 1")

fit_time = time.time()

print("Test point 2")
result.fit(train_images, train_labels)
print("Fit time: " + str(time.time()-fit_time))

predict_time = time.time()
accuracy = 0
test_set_length = 100

for i in range(test_set_length):
    if result.predict([test_images[i]])[0] == test_labels[i]:
        accuracy += 1
accuracy /= test_set_length
accuracy = str(accuracy*100) + '%'

print("Prediction time: " + str(time.time()-predict_time))
print("Prediction accuracy: " + accuracy)
