# pip install flask

from flask import Flask, render_template, request
import requests
import requests
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
import requests
# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "nFFWACn7pVNTQWlnb7pusoXVa63g0vFEq_8Y2x2pxZSE"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
app = Flask(__name__)
@app.route('/')
def index():
return render_template('water1.html')
@app.route('/predict', methods = ['POST'])
def predict():
ph = request.form['D.O. (mg/l)']
Hardness = request.form['CONDUCTIVITY (µmhos/cm)']
Solids = request.form['B.O.D. (mg/l)']
Chloramines = request.form['NITRATENAN N+ NITRITENANN (mg/l)']
Sulfate = request.form['FECAL COLIFORM (MPN/100ml)']
Conductivity = request.form['TOTAL COLIFORM (MPN/100ml)Mean']
t = [[float(D.O. (mg/l)),float(CONDUCTIVITY (µmhos/cm)),int(B.O.D. (mg/l)),float(NITRATENAN N+ NITRITENANN (mg/l)),float(FECAL COLIFORM (MPN/100ml)),float(TOTAL COLIFORM (MPN/100ml)Mean)]]
payload_scoring = {"input_data": [{"fields": [["f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12","f13","f14"]], "values":t }]}
response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/94d69d4c-4e12-4662-aba9-fe193faa3d90/predictions?version=2022-11-07', json=payload_scoring,
headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
payload_scoring = {"input_data": [{"fields": [["f0","f1","f2","f3","f4","f5","f6"]], "values":t }]}
pred= response_scoring.json()
output=pred['predictions'][0]['values'][0][0]
print(output)
return render_template("water1.html", prediction_text = output)
if __name__=='__main__':
app.run(debug = False)