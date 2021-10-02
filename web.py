from flask import Flask, request, render_template
import pickle
import pandas as pandas
import numpy as np

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', JURUSAN=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    JENIS_KELAMIN, KABUPATEN_KOTA, PROVINSI, JENJANG, TAHUN_LULUS= [x for x in request.form.values()]

    data = []
    JENIS_KELAMIN=str(request.form['JENIS_KELAMIN'])
    KABUPATEN_KOTA=str(request.form['KABUPATEN_KOTA'])
    PROVINSI=str(request.form['KABUPATEN_KOTA'])
    JENJANG=str(request.form['JENJANG'])
    data.append(int(TAHUN_LULUS))




    prediction = model.predict([data])
    output = prediction 
    
    return render_template('index.html', JURUSAN=output, JENIS_KELAMIN=JENIS_KELAMIN, KABUPATEN_KOTA=KABUPATEN_KOTA, 
                            PROVINSI=PROVINSI, JENJANG=JENJANG, TAHUN_LULUS=TAHUN_LULUS )


if __name__ == '__main__':
    app.run(debug=True)