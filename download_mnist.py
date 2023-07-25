#download mnist image
#location:C:/users/ccllab/desktop/mnist
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from PIL import Image

# 下載MNIST數據集到本地
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# 指定保存路径
save_path = 'C:/Users/ccllab/Desktop/mnist/'

# 保存訓練數據
for i in range(len(train_images)):
    image_path = save_path + f'train_image_{i}.png'
    img = Image.fromarray(train_images[i])
    img.save(image_path)

# 保存測試數據
for i in range(len(test_images)):
    image_path = save_path + f'test_image_{i}.png'
    img = Image.fromarray(test_images[i])
    img.save(image_path)