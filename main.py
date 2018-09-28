import  mnist
mndata = mnist.MNIST('./images')
train_images, train_labels = mndata.load_training()
test_images, test_labels = mndata.load_testing()