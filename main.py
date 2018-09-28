import  mnist
mndata = mnist.MNIST('./images')
images, labels = mndata.load_training()
print(images, labels)