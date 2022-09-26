import numpy as np
from flask import Flask, request, render_template
import pickle
import math
from sklearn import preprocessing 

path_to_encoders = './class_encoders/'

#Create Flask app
app = Flask(__name__)

#Load the trained model. (Pickle file)
model = pickle.load(open('./models/RandomForestClassifier.pkl', 'rb'))

def get_classname(prediction):
    if prediction == 0:
        class_name = 'edibile'
    if prediction == 1:
        class_name = 'poisonous'
    return class_name

def encoding_features(feature):
    feature_value = request.form[feature]
    encoder = preprocessing.LabelEncoder()
    encoder.classes_ = np.load(path_to_encoders+feature+'_encoder.npy', allow_pickle=True)
    feature_value = encoder.transform([feature_value])
    for value in feature_value:
        value = value
    return value

@app.route('/')
def home():
    return render_template('index.html')

#POST: Used to send HTML form data to the server.
@app.route('/predict',methods=['POST'])
def predict():
    input_encoding = ['cap-shape', 'cap-color', 'does-bruise-or-bleed',
                    'gill-color','stem-color','has-ring', 'habitat',
                    'season','ring-type']
    encoded_feature_values = []
    encoded_feature_values.append(request.form['cap-diameter'])
    encoded_feature_values.append(request.form['stem-height'])
    encoded_feature_values.append(request.form['stem-width'])
    for feature_to_encode in input_encoding:
        value = encoding_features(feature_to_encode)
        encoded_feature_values.append(value)
        #print(encoded_feature_values)

    encoded_feature_values = [np.array(encoded_feature_values)]
    prediction = model.predict(encoded_feature_values)
    prediction = np.round(prediction) # round to either 0(E) or 1(P)  poisonous=p, edibile=e
    class_name = get_classname(prediction)
    return render_template('index.html', prediction_model='Model prediction is: ' + class_name)

if __name__ == "__main__":
    app.run(port=5000)