# from flask import Flask
# app = Flask(__name__)

# @app.route("/")
# def index():
#     return "<h1>Hello Azure!</h1>"

from flask import Flask, render_template
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16

app = Flask(__name__)

@app.route('/')
def hello_world():
    # return 'Hello, World!'

    # load the model
    model = VGG16()
    # load an image from file
    filename = 'input.jpg'
    image = load_img('static/img/'+filename, target_size=(224, 224))
    # convert the image pixels to a numpy array
    image = img_to_array(image)
    # reshape data for the model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # prepare the image for the VGG model
    image = preprocess_input(image)
    # predict the probability across all output classes
    yhat = model.predict(image)
    # convert the probabilities to class labels
    label = decode_predictions(yhat)
    # retrieve the most likely result, e.g. highest probability
    label = label[0][0]
    # print the classification
    print('%s (%.2f%%)' % (label[1], label[2]*100))

    pc = label[2]*100
    pc = "%3.2f" % (pc)
    return render_template("index.html",_class=label[1], _prediction=pc, filename=filename)

if __name__ == '__main__':
    app.run()