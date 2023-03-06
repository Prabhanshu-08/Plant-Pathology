from flask import Flask, render_template,request
from keras.models import load_model
import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

model = load_model("plant_pathology")

unique_class = ['Healthy','Multiple_diseases','Rust','Scab']

@app.route('/',methods=['GET','POST'])
def index():
	return render_template("index.html")



@app.route("/prediction", methods=["GET","POST"])
def prediction():
	
	img = request.files['img']
	img.save("static/img.jpg")


	image_1 = cv2.imread('static/img.jpg')
	image_1 = cv2.cvtColor(image_1,cv2.COLOR_BGR2RGB)

	image = cv2.resize(image_1, (224,224))

	image = image/255.0

	image = np.expand_dims(image,axis=0)

	pred = model.predict(image,verbose=0)

	predicted_class = unique_class[np.argmax(pred)]

	if predicted_class=='Healthy':

		return render_template("index_1.html",prediction_text=predicted_class)

	else:

		return render_template("index_1.html",prediction_text_1=predicted_class)


	
if __name__ == "__main__":
	app.run(debug=True)